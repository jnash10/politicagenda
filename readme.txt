requirements:
	libraries: pip install GetOldTweets3
	reccomended python version :3.8

description:
	provides meaningful words from a user's tweets for a given month.

Algorithm Used:	
	uses tf-idf to remove most stop words,
	ranks words left according to no. of tweets that used it.
	(occasional stop words may creep in.)
	
	
Usage:
	after installing requirements
	to run:
		"python interactive.py"
