#Austin Peterson
#file for first try at using DBScan on collected Arabic Tweets

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
	proc_text_list = []

	for text in text_list:
		proc_text_list.append(process_text(text))

	#defining floats for data segmentation, went with 80/20 split
	#train_seg = .8
	#test_seg = 1-float(train_seg)

	#vectorizer(tfidf)
	#using vectorizer to transform text
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(proc_text_list)

	#can define custom distance metrics for DBScan
	#check it out
	#https://scikit-learn.org/stable/faq.html#how-do-i-deal-with-string-data-or-trees-graphs
	#levenshtein is good for strings, currently using tfidf
	#NOT CURRENTLY USED
	def lev_metric(x, y):
		i, j = int(x[0]), int(y[0])#extract indices
		return levenshtein(data_list[i], data_list[j])


	#create dbscan
	#X = np.arange(len(data_list)).reshape(-1, 1)
	#db = dbscan(X, metric=lev_metric, eps=5, min_samples=2)

	#this is where we need to play around with parameters
	db = DBSCAN(eps = 0.3, min_samples = 5)#don't wanna go lower than 5

	#fit data to dbscan
	#todo: build pipeline for vectorizer->dbscan workflow
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



#simple, fast way to stem/process text
#todo - remove urls from all text
def process_text(text):
	words = text.split()

	new_words = []

	for word in words:
		#stem word
		new_word = isri.stem(word)
		#print("."+new_word+".")

		#dont append if stemming turns it into whitespace/""
		if new_word != "":
			new_words.append(new_word)

	#return this
	new_text = ' '.join(new_words)

	return new_text




main()





















#notes
#https://www.dummies.com/programming/big-data/data-science/how-to-create-an-unsupervised-learning-model-with-dbscan/

#load tweets as they're being clustered so that you can look through
#the tweets that were classified into each cluster
#(sounds like something we want)