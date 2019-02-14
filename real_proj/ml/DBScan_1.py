#Austin Peterson
#file for first try at using DBScan on collected Arabic Tweets

import os.path
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(my_path, os.pardir))

#importing loader code by inserting path to file at runtime
#(if you want to include other files from /loader/, have to add)
sys.path.insert(0, parent_path+"/loader")
import loader


#testing load
loader.load_tweets_xlsx("outputSmall")

























#notes
#https://www.dummies.com/programming/big-data/data-science/how-to-create-an-unsupervised-learning-model-with-dbscan/

#load tweets as they're being clustered so that you can look through
#the tweets that were classified into each cluster
#(sounds like something we want)