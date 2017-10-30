from pymongo import MongoClient

def preproc():
	db = MongoClient('mongodb://143.215.138.132:27017')['big_data']

	matchNE = {'$match': {'lat': {'$gte': 36, '$lte': 50}, 'lon': {'$gte': -99, '$lte': -69}}}
	matchSE = {'$match': {'lat': {'$gte': 25, '$lte': 36}, 'lon': {'$gte': -99, '$lte': -69}}}
	matchNW = {'$match': {'lat': {'$gte': 36, '$lte': 50}, 'lon': {'$gte': -125, '$lte': -99}}}
	matchSW = {'$match': {'lat': {'$gte': 25, '$lte': 36}, 'lon': {'$gte': -125, '$lte': -99}}}


	tweets = []
	labels = []

	limit = {'$limit': 10000}

	pipeline = [matchNE, limit]

	for tweet in db.tweet.aggregate(pipeline):
	    tweets.append(tweet['text'])
	    labels.append('NE')


	pipeline = [matchSE, limit]

	for tweet in db.tweet.aggregate(pipeline):
		tweets.append(tweet['text'])
		labels.append('SE')

	return tweets, labels

