import sqlite3
import pandas as pd
from datetime import datetime

def _get_event_count(batch_id, to_email, table, unsub=False):
    """
    Given a table, batch id, an email address, and an unsub boolean, return the
    number of rows that match the given batch id and email address.
    
    Parameters:
    -----------
        batch_id: a batch_id for a group email blast
        to_email: the email address of the recipient
        unsub: a boolean; is this the unsub_event table?
    
    Returns:
    --------
        count : integeter
    """
    if unsub:
        cond1 = table['email'] == to_email
        table = table[cond1]
        count = table.shape[0]
    else:
        cond1 = table['batch_id'] == batch_id
        cond2 = table['to_email'] == to_email
        table = table[cond1 & cond2]
        count = table.shape[0]
    return count

if __name__ == "__main__":
    
    # Open the connection and grab the data from the database
    conn = sqlite3.connect("sqlite.db")
    send_event = pd.read_sql("SELECT * FROM send_event", conn)
    open_event = pd.read_sql("SELECT * FROM open_event", conn)
    bounce_event = pd.read_sql("SELECT * FROM bounce_event", conn)
    click_event = pd.read_sql("SELECT * FROM click_event", conn)
    unsub_event = pd.read_sql("SELECT * FROM unsub_event", conn)
    event_summary_detailed = pd.read_sql("SELECT * FROM event_summary", conn)
    
    
    # Create a new table for the DB that holds the minimized summary
    event_summary = send_event.copy()
    event_summary['open_count'] = 0
    event_summary['bounce_count'] = 0
    event_summary['click_count'] = 0
    event_summary['unsub_count'] = 0
    event_summary['last_updated'] = ' '
    
    # Iterate over the send_event table to update the new event_summary table
    # Note: we iterate over the send table because each row is unique in terms
    # of the combination of batch id and email address
    for row in range(send_event.shape[0]):
        batch_id = send_event.iat[row, 0]
        to_email = send_event.iat[row, 1]
        event_summary.iat[row, 4] = _get_event_count(batch_id, to_email, open_event)
        event_summary.iat[row, 5] = _get_event_count(batch_id, to_email, bounce_event)
        event_summary.iat[row, 6] = _get_event_count(batch_id, to_email, click_event)
        event_summary.iat[row, 7] = _get_event_count(batch_id, to_email, unsub_event, unsub=True)
        event_summary.iat[row, 8] = str(datetime.now())[:-7]
        
    # Commit changes to memory (if given arg 'commit') and close the connection
    try:
        #if sys.argv[1] == 'commit':
        if True: # Uncomment this line and comment line above for in IDE testing
            cursor = conn.cursor()
            cursor.execute("ALTER TABLE event_summary RENAME TO event_summary_detailed")
            event_summary.to_sql('event_summary', conn)
            conn.commit()
    except IndexError:
        print("Done. Update not committed; input 'commit' in arg[1] to commit db")        
    conn.close()