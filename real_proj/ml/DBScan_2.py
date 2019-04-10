#Austin Peterson

from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
from leven import levenshtein
import numpy as np

#nlp stuff
from nltk.stem.isri import ISRIStemmer
isri = ISRIStemmer()

#for plotting/graphics
#import matplotlib.pyplot as plt

import os.path
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(my_path, os.pardir))

#importing loader code by inserting path to file at runtime
#(if you want to include other files from /loader/, have to add)
sys.path.insert(0, parent_path+"/loader")
import loader



def main():
	#target_xlsx = input("target xlsx (without file extension): ")
	target_xlsx = "outputSmall"

	#todo: convert to list of strings ('text' column)
	data_list = loader.load_tweets_xlsx(target_xlsx)

	#converting 'text' column to list
	text_list = data_list['text'].tolist()

	#process data here
	#proc_text_list = []

	#vectorizer(tfidf)
	#using vectorizer to transform text
	#vectorizer = TfidfVectorizer()
	#X = vectorizer.fit_transform(text_list)

	X = np.arange(len(text_list)).reshape(-1, 1)

	def lev_metric(x, y):
		i, j = int(x[0]), int(y[0])#extract indices
		return levenshtein(data_list[i], data_list[j])


	#new db scan
	db = DBSCAN(metric=lev_metric, eps = 0.3, min_samples = 5)

	db.fit(X)




	#plotting

	#get list of labels for group (-1 is noise)
	labels = db.labels_

	#find amt of noise labels (quikndirty)
	n_noise = list(labels).count(-1)

	#number of clusters (ignoring noise)
	n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

	#with outputSmall test data, clusters coming out to 23
	print("# of labels(clusters): "+str(n_clusters))
	#coming out to 5713 (oh no)
	print("# of data labelled as noise: "+str(n_noise))

	#resolve labels of clusters to X (labels and X should have same index)
	#print("array:")
	#print(X)

	# print(len(text_list))
	# print(len(X))
	# print("end")




main()
























