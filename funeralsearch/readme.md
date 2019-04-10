Use these excel files and scripts to search for the funeral keywords in the twitter scraper

The funeral keywords are the keywords professor Ewaisha gave us, and are what the script searches for

The db.xlsx file is a database of event id's and event dates of all the events in the gsr that have one of the keywords in the content of the gss article links.

The script just needs to be run in the same folder as the two xlsx files, you can edit the file and edit the mindate and maxdate variables to change the dates of when you want to search for each event. You can also change the limit to search for the number of tweets.

It only searches for a 10 day period from the event date of march 2017

It takes a long time as you're searching for 17 keywords for every event, so you're basically making 500 twitterscraper calls which returns 200 tweets each for 100,000 tweets found which is a relatively small sample size per keyword.
