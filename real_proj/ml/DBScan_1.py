#Austin Peterson
#file for first try at using DBScan on collected Arabic Tweets

from sklearn.cluster import DBSCAN
import pandas as pd
from leven import levenshtein
import numpy as np

import os.path
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(my_path, os.pardir))

#importing loader code by inserting path to file at runtime
#(if you want to include other files from /loader/, have to add)
sys.path.insert(0, parent_path+"/loader")
import loader





def main():
	target_xlsx = input("target xlsx (without file extension): ")

	#todo: convert to list of strings ('text' column)
	data_list = loader.load_tweets_xlsx(target_xlsx)

	#converting 'text' column to list
	text_list = data_list['text'].tolist()

	#defining floats for data segmentation, went with 80/20 split
	#train_seg = .8
	#test_seg = 1-float(train_seg)

	#can define custom distance metrics for DBScan
	#check it out
	#https://scikit-learn.org/stable/faq.html#how-do-i-deal-with-string-data-or-trees-graphs
	#levenshtein is good for strings
	def lev_metric(x, y):
		i, j = int(x[0]), int(y[0])#extract indices
		return levenshtein(data_list[i], data_list[j])


	#create dbscan
	X = np.arange(len(data_list)).reshape(-1, 1)
	db = dbscan(X, metric=lev_metric, eps=5, min_samples=2)

	#fit data to dbscan
	db.fit(data_list)

	print(db)























#notes
#https://www.dummies.com/programming/big-data/data-science/how-to-create-an-unsupervised-learning-model-with-dbscan/

#load tweets as they're being clustered so that you can look through
#the tweets that were classified into each cluster
#(sounds like something we want)