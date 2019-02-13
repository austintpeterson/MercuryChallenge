
#Austin P
#

#from xlrd import open_workbook
#import pyexcel

import pandas as pd
import csv
import os.path
import string

#switch to xlsx file reading
#https://pythonspot.com/read-xls-with-pandas/

#for loading word list (word, count)
def load_tweets(target_csv):
	path = os.path.dirname(os.path.abspath(__file__))

	try:
		#open word csv file
		with open(target_csv, "r") as csv_file:
			reader = csv.reader(csv_file, delimiter = ',')
			next(reader, None)#skip header (should always exist)

			#new load data
			col_names = ['word', 'count']#
			
			my_df = pd.DataFrame(columns = col_names)

			i = 0
			for row in reader:
				word = row[0]
				count = row[1]

				my_df.loc[len(my_df)] = [word, count]
				i += 1

			print("# of words loaded: "+str(i))


	except FileNotFoundError:
		print("could not find .csv file")

	#return a dataframe
	#[class (bot or not), text]x(# of users)
	return my_df



def load_tweets(target_xlsx):
	path = os.path.dirname(os.path.abspath(__file__))

	file_path = path+"/"+my_df

	my_df = pd.read_excel(file_path, sheet_name=None)
	





#load tweets as they're being clustered so that you can look through
#the tweets that were classified into each cluster
#

#do DBscan idiot
#https://www.dummies.com/programming/big-data/data-science/how-to-create-an-unsupervised-learning-model-with-dbscan/






















