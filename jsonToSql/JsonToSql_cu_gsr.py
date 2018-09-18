#designed to convert all the json CU event data provided by IARPA (in the cu_gsr data)
#into a sql database for use later.  will try to format dates into 
#sql datetime format for easy time-based queries.

#hopefully all cu event warning will be inserted into the same db

#created by Austin Peterson

import json
import sqlite3
import time

# need time.strftime to conv json time to sql datetime
#https://stackoverflow.com/questions/6119369/simple-datetime-sql-query

with open("/Users/austinpeterson/Documents/code/MercuryChallenge/jsonToSql/cu_gsr/CU_April_2016.json", "r") as read_file:
    data = json.load(read_file)

    print(data)