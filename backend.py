import math

import GetOldTweets3 as got




#starttime = (month,year)
#endtime = (month,year)

monthdic = {
	1:31,
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31,
}



def monthtweets(handle,month,year):
	#returns list of tweets
	tweetCriteria = got.manager.TweetCriteria().setUsername(handle).setSince(year+"-"+month+"-"+"01").setUntil(year+"-"+month+"-"+str(monthdic[int(month)]))
	tweets = []
	for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
		lowercase = tweet.text.lower()
		tweets.append(lowercase.split())
	return tweets


def tfidf(word,document,corpus): # returns tuple: (tf_idf_score,no. of documents with that word)
	#word is a single word
	#document is a list of words from a tweet
	#corpus is a collection of tweets
	tf = (document.count(word))/len(document)
	#    IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
	docs_w_word = 0
	for doc in corpus:
		if word in doc:
			docs_w_word = docs_w_word + 1
	idf = math.log(len(corpus)/docs_w_word)

	return tf*idf,docs_w_word

def actual(handle,month,year):

	print("gettings words",handle,month)
	tweets = monthtweets(handle, month, year)


	wordranks = []
	for tweet in tweets:
		for word in tweet:

			wordranks.append((tfidf(word,tweet,tweets),word))

	wordranks = list(dict.fromkeys(wordranks))
	wordranks.sort()
	wordranks.reverse()

	rankingagain = []

	for i in range(0,30):
		word = wordranks[i][1]
		occurence = wordranks[i][0][1]
		if occurence >= 2 :

			rankingagain.append((occurence,word))

	rankingagain.sort()
	rankingagain.reverse()
	rankingagain = list(dict.fromkeys(rankingagain))

	for word in rankingagain:
		return rankingagain #return a list of tuples, sorted by occurrence of word



