#https://github.com/taspinar/twitterscraper/

from twitterscraper import query_tweets
import datetime as dt

#can be used as a command line tool as well, very useful
#ex: twitterscraper realDonaldTrump -u -o tweets_trump.json

#can get from bd (begindate) to ed (enddate)
#twitterscraper Trump -l 100 -bd 2017-01-01 -ed 2017-06-01 -o trumptweets.json/.txt

#Per Tweet it scrapes the following information: + Username and Full Name + Tweet-id + Tweet-url + Tweet text + Tweet html + Tweet timestamp + No. of likes + No. of replies + No. of retweets
#Each tweet has these attribs: user, fullname, id, url, timestamp, text, replies, rewteets, likes, html

#query_tweets(query, limit=None, begindate=dt.date(2006,3,21), enddate=dt.date.today(), poolsize=20, lang='')

list_of_tweets = query_tweets("Muslim Brotherhood", 10)

#can write to file
file = open("output.txt","w")
for tweet in query_tweets("Egypt", 10):
	file.write(tweet.text)#write text of tweet to file
	file.write("\n\n")
file.close()