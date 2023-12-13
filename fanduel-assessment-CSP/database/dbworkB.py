import sqlite3
import pandas as pd
from datetime import datetime
import sys

if __name__ == "__main__":
    
    # Open the connection, make a cursor, and grab the data from the database
    conn = sqlite3.connect("sqlite.db")
    open_event = pd.read_sql("SELECT * FROM open_event", conn)
    click_event = pd.read_sql("SELECT * FROM click_event", conn)
    send_event = pd.read_sql("SELECT * FROM send_event", conn)
    try:
        event_summary_detailed = pd.read_sql("SELECT * FROM event_summary_detailed", conn)
    except:
        print("Must run Part A first for this to work. See documentation")
        conn.close()
        sys.exit(1)
    event_summary = pd.read_sql("SELECT * FROM event_summary", conn)
    
    # Grab the last update timestamp
    last_update = str(event_summary.sort_values(by=['last_updated'], ascending=False).iat[0,9])
    
    # Filter new open and click events prior to the last update
    new_open_events = open_event[open_event['open_date'] > last_update]
    new_click_events = click_event[click_event['click_date'] > last_update]
    
    # Make a dictionary to hold the new detailed events summary dataframe
    # components to append to the old dataframe
    new_event_summary_detailed_dict = {
            'columns': list(event_summary_detailed.columns),
            'entries': []
    }
    
    # Reindex event_summary for substantially faster updating (versus iteration)
    event_summary.set_index(['batch_id', 'to_email'], inplace=True)
    
    # Iterate over the new_open_events and new_click_events dataframes
    # to update the event_summary and event_summary_detailed table.
    for row in range(new_open_events.shape[0]):
        batch_id = new_open_events.iat[row,1]
        to_email = new_open_events.iat[row,2]
        open_date = new_open_events.iat[row,3]
        # Add this row to the events_summary_detailed dictionary (The statement
        # is designed to fit the correct structure of the table by column)
        entry = [batch_id, to_email, None, None, open_date, None]
        new_event_summary_detailed_dict['entries'].append(entry)
        # Update the event_summary table
        event_summary.at[(batch_id, to_email), 'open_count'] += 1
        event_summary.at[(batch_id, to_email), 'last_updated'] = str(datetime.now())[:-7]
        
    for row in range(new_click_events.shape[0]):
        batch_id = new_click_events.iat[row,1]
        to_email = new_click_events.iat[row,2]
        click_date = new_click_events.iat[row,3]
        # Add this row to the events_summary_detailed dictionary (The statement
        # is designed to fit the correct structure of the table by column)
        entry = [batch_id, to_email, None, None, None, click_date]
        new_event_summary_detailed_dict['entries'].append(entry)
        # Update the event_summary table
        event_summary.at[(batch_id, to_email), 'click_count'] += 1
        event_summary.at[(batch_id, to_email), 'last_updated'] = str(datetime.now())[:-7]

    # Reformat the event_summary table so it can be stored in the database
    event_summary.reset_index(inplace=True)
    
    # Add new items to the events_summary_detailed table
    new_items = pd.DataFrame(new_event_summary_detailed_dict['entries'],
                             new_event_summary_detailed_dict['columns'])
    event_summary_detailed = event_summary_detailed.append(new_items, ignore_index=True)
    
    # Commit changes to memory (if given arg 'commit') and close the connection
    try:
        if sys.argv[1] == 'commit':
            event_summary_detailed.to_sql('event_summary_detailed', conn)
            event_summary.to_sql('event_summary', conn)
            conn.commit()
    except IndexError:
        print("Not enough args; input 'commit' in arg[1] to commit db")        
    conn.close()