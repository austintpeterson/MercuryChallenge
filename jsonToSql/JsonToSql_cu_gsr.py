#designed to convert all the json CU warning data provided by IARPA (in the cu_gsr data)
#into a sql database for use later.  will try to format dates into 
#sql datetime format for easy time-based queries.

#created by Austin Peterson

import json
import sqlite3

with open("__", "r") as read_file:
    data = json.load(read_file)