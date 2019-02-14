
#Austin P
#this is for loading xlsx from the tweet_collections dir in /scraping/

import pandas as pd
import numpy as np
import csv
import os.path
import string
import math

#for loading keyword list csv (word, count)
#this is currently UNUSED, ignore it
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



#function for loading tweet_collections xlsx into a pandas dataframe
#can be modified later depending on format of data coming in
def load_tweets_xlsx(target_xlsx):
	
	#get current path and parent path
	my_path = os.path.dirname(os.path.abspath(__file__))
	parent_path = os.path.abspath(os.path.join(my_path, os.pardir))

	file_path = parent_path+"/scraping/tweet_collections/"+target_xlsx+".xlsx"

	print("xlsx path to load: "+file_path+"\n")
	
	#probably costly to load whole xlsx, but allows us to filter columns/rows later
	my_df = pd.read_excel(file_path, sheet_name = "Sheet1")#(file_path, index_col = 0)

	#print(my_df.columns)

	#clean df here
	cleaned_df = clean_loaded_df(my_df)

	#print(cleaned_df['text'])
	return cleaned_df
	
	

#takes raw dataframe loaded by load_tweets_xlsx and cleans up/filters the columns needed
#the filtering/cleaning can be changed later
#takes a df as parameter, returns a 'clean' dataframe
def clean_loaded_df(dirty_df):
	#delete columns we don't need for ml
	#these stmts can be added/commented based on what we want for our clean_df
	
	#1 for columns, 0 for rows
	#'Number' column is kept for filtering keyword tag rows
	new_df = dirty_df.drop('user',1)
	new_df = new_df.drop('fullname',1)
	new_df = new_df.drop('tweet-id',1)
	new_df = new_df.drop('timestamp',1)
	new_df = new_df.drop('url',1)
	new_df = new_df.drop('likes',1)
	new_df = new_df.drop('replies',1)
	new_df = new_df.drop('retweets',1)
	#ALWAYS keeping the 'text' column
	new_df = new_df.drop('html',1)

	#['Number', 'text']
	#print(new_df.columns)
	
	#filter rows here
	#getting rid of "keyword tag" rows that aren't tweet/data rows
	#these rows have nothing in 'text' column ('')
	
	#note: there is probably a better way to do this, but I struggled with 
	#issues regarding how NaN and int values are read in from xlsx for a while
	#if xlsx format in changes, this will have to be addressed

	#replace any empty text rows with numpy nan (this is supported by pandas)
	new_df['text'].replace('', np.nan, inplace=True)
	#drop any rows that have numpy nan in text column
	new_df.dropna(subset = ['text'], inplace=True)

	print(new_df.shape)

	print(new_df["Number"])

	return new_df













