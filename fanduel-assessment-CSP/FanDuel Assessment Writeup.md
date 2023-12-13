# FanDuel Assessment Writeup

Hi FanDuel! Thanks for taking the time to review my work. I want to share a couple things before you get into the projects themselves. In order to make it easier for you to run these scripts, I've created a virtual environment that can be found in the (\fanduel-assessment-CSP\fanduel-env) directory. This environment contains all of the needed modules to run these scripts (I considered using docker but that seemed like a bit much and I'm more familiar with virtual environments than docker althuogh I could learn it). The virtual environment can be activated by navigating to the above directory and running the following command:

    $ Script\activate

You will know that the virtual environment is active by checking for the below prompt in the terminal:

    (fanduel-env) $

## Part 1: REST API

There were some tough choices I had to make in building this API. Conceptually, a REST API is simple but the front end work surrounding making it into a functional, beautiful responsive page is tedious and intricate. I decided to use Flask and Flask-restful to provide the pipeline between the URLs and the back end logic. The data given to me by you was stored in a large dictionary from which I queried information to service the appropriate requests. Ultimately, I decided that this was the most efficient way to deliver what was asked and decided against building out the front-end portion (I can work on this too if asked).

If I were to abstract this a bit for other sports, I would make quite a few changes. First, I'd create directories for each sport and in each directory, I'd have a csv file for teams, players, games, and game stats (so 5 csv files total). The functions requested (getting teams, players, games, etc.) can all be abstracted by requiring a parameter that told you what sport you wanted. It would then take that input sport and load the appropriate data before executing the query. We'd still need to add more endpoints, but this would eliminate the need to rewrite these functions for each inidividual sport by having a uniform structure for the data across sports. The biggest downside to this implementation would be that there would be a bit of processing to first intake all of the data. However, this implementation would allow for a much easier addition of new sports, teams, players, and games, than adding that information to a dictionary (which is the current way I have the data stored in-memory now). Also, by having the data stored in a file or database, the information would persist as ooposed to the in-memory data which resets basically every time you run the default api. You can test this API by running the api script located at (\fanduel-assessment-CSP\fanduel-app\) using the following command:
$ python api.py
From there, you should be able to run simple requests to test the API (using curl or whatever other method you choose). Below are a few samples of what they looked like on my machine so you can just copy them if you'd like:

    curl http://127.0.0.1:5000/nba/teams
    curl http://127.0.0.1:5000/nba/teams/2
    curl http://127.0.0.1:5000/nba/players
    curl http://127.0.0.1:5000/nba/players?date=01022016
    curl http://127.0.0.1:5000/nba/players/3
    curl http://127.0.0.1:5000/nba/players/1/stats
    curl http://127.0.0.1:5000/nba/games
    curl http://127.0.0.1:5000/nba/games?date=01022016
    curl http://127.0.0.1:5000/nba/games/2

## Part 2: Database

For this portion of the assessment, I decided to use Pandas for data analysis and manipulation as I find Pandas to be very strong for those purposes. At any time, you can reset the database by running the following command from the (\fanduel-assessment-CSP\database) directory:
$ python resetdb.py

### Part A

In order to answer this question, I need to describe how I view duplicates. Regarding databases, I believe there are two types of duplicates. The first type I'll call "true duplicates" (t-dupes). T-dupes are two or more records in a database with different primary keys but identical information in the subsequent columns. I will call the second type "false duplicates" (f-dupes). F-dupes are two or more records in a database that refer to similar instances but they may not necessarily have identical information in the subsequent columns; these items should be grouped together as that is how people would typically think of these items. F-dupes occur when we perform certain types of joins (simple/left-outer) for information that is related at which point we would see multiple row items relating to the same person or idea.

** For this problem, I assumed the analyst was seeing false duplicates and not true duplicates\***

For example, let's assume we have a database of two tables that contains individuals and their ages and another table that lists their professions. Furthermore, let's assume that we've tried to join these tables (or we have a script that manually enters rows of an individual, their age, and their career). A t-dupe might look something like this:

| PRIMARY KEY | NAME     | AGE | JOB       |
| ----------- | -------- | --- | --------- |
| 1           | John Doe | 29  | Carpenter |
| 2           | John Doe | 29  | Carpenter |
| 3           | Jane Doe | 24  | Plumber   |

Here, we can see that John Doe has a true duplicate (same data, different primary key, so technically these are different records). Alternatively, a false duplicate might look something like this:

| PRIMARY KEY | NAME     | AGE | JOB         |
| ----------- | -------- | --- | ----------- |
| 1           | John Doe | 29  | Carpenter   |
| 2           | John Doe | 29  | Electrician |
| 3           | Jane Doe | 24  | Plumber     |

This would be considered a false duplicate because if we wanted to see just a single row for John Doe (like in the problem), we'd get multiple rows relating to John for his multiple careers. One possible solution to this problem is to simply store a list of John's possible careers in a seperate column on this table. The issue with that is that we don't want unbounded data in a given column. There are a few ways to rectify this problem and they have their advantages and disadvantages. My biggest concern here was a loss of data, so I decided that in order to fix the problem, we should create another table that contains multiple rows for John's possible career options and place a secondary key in the above table that allows us to return a list of all of John's possible careers from the second table. This is the solution I implemented for this marketing campaign problem.

To elaborate, I renamed the event_summary table to event_summary_detailed, and then duplicated the send_event table (naming the new copy the event_summary table). The event_summary table will now have a single row for each primary key (the batch ID AND email address as the primary key) and columns that list the number respective of events N for each type of event and a last_updated timestamp (this will help for part B). This would allow the analyst to look at the event summary table and quickly see how many actions are taken per an indidivual email within a given batch and when the last update occurred. If the analyst needs further details on specific events, they can visit the event_summary_detailed table.

The code to create these changes can be found in the (\fanduel-assessment-CSP\database) directory and can be run by entering the following command from that directory in the terminal:

    $ python dbworkA.py

The above command does not commit the data to the database. In order to commit the information to the database, in the same directory, execute the following command:

    $ python dbworkA.py -commit

### Part B

In order to efficiently add the latest information to the above database, we need to ensure that we don't recomupte the entire database and instead just append the new stuff and update the new events. I propose that we do this by adding a column to the event summary tab called last_updated. The last_updated column will simply hold a timestamp of the most recent update time of that entry. We then look at the new open and click events using a time filter and process those items into the events_summary and events_summary_detailed tables that happened after the most recent update. Looking at Part B, you can see some distinct differences from Part A. In Part A, there was a bit of redesign that went into the database structure in the script. This mostly required us to iterate over tables quite a bit; however, there were still some optimizing we could do through the use of boolean filters. In Part B, you can see that we could completely reimage how we access specific information through multileveled indexing for much faster reads and writes for updating the database. You can run this script by navigating to the (\fanduel-assessment-CSP\database) directory and running the following command:

    $ python dbworkB.py

As in part A, you can commit these changes to the database by running the following command:

    $ python dbworkB.py -commit

## Part 3: Depth Charts

For the depth chart portion of the assignment, I ultimately decided to perform a series of quality checks against the input rather than overdo a class implementation (i.e. making different types of depth charts with checks against for example a position being valid for a sport; because there are no wide receivers in the MLB). I also decided not to implement the builder design pattern from the Java example because it is not needed in Python as Python has named and optional parameters. There are three files, similar to the Java example provided, for the depth class portion of the assignment. It can be run by navigating to the directory (\fanduel-assessment-CSP\depthcharts) and entering the following command from that directory in a terminal:

    $ python DepthChartsMain.py
