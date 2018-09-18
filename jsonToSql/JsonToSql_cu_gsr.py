#designed to convert all the json CU event data provided by IARPA (in the cu_gsr data)
#into a sql database for use later.  will try to format dates into 
#sql datetime format for easy time-based queries.

#hopefully all cu event warning will be inserted into the same db

#created by Austin Peterson

import json
import sqlite3
import time
import os

# need time.strftime to conv json time to sql datetime
#https://stackoverflow.com/questions/6119369/simple-datetime-sql-query




def main():

	path = '/Users/austinpeterson/Documents/code/MercuryChallenge/jsonToSql/cu_gsr/'

	#read each json file included in cu_gsr
	for filename in os.listdir(path):

		temppath = path+filename

		with open(temppath, "r") as read_file:
			data = json.load(read_file)

		#print(data)

		#json fields

		#Approximate_Location (str)
		#City (str)
		#Country (str)
		#Crowd_Size (str)
		#Crowd_Size_Description (str)
		#Earliest_Reported_Date (put in datetime format)
		#Encoding_Comment (str)
		#Event_Date (put in datetime format)
		#Event_ID (str)
		#Event_Type (str)
		#First_Reported_Link (str)
		#GSS_Link (str)
		#Latitude (float/)
		#Longitude (float/)
		#News_Source (str)
		#Other_Links (str, w/ newlines separating)
		#Population (str)
		#Reason (str)
		#Revision_Date (put in datetime format)
		#State (str)
		#Revision_DTG (int?)

		#parse json data into vars
		for i in data:
			print(i['City'])

			try:
				Approximate_Location = i['Approximate_Location']
				print(Approximate_Location)
				
			except Error as e:
				print(e)








main()







	
