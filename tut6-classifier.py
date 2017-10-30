from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import TweetTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Tweet_Tokenizer(object):
    def __init__(self):
        self.wnl = TweetTokenizer()
    def __call__(self, doc):
        return self.wnl.tokenize(doc)

def make_features(corpus):
    vectorizer = CountVectorizer(tokenizer=Tweet_Tokenizer(), analyzer='word', min_df=0)
    return vectorizer.fit_transform(corpus)

tweet_list = make_features(['A', 'B', 'C'])
location_list = ['SE', 'NE', 'NE']

tweet_training_set, tweet_test_set, location_training_set, location_test_set = train_test_split(tweet_list, location_list, test_size=0.2, random_state=999)
lr_clf = LogisticRegression(solver='saga', max_iter=3000)
lr_clf.fit(tweet_training_set, location_training_set)
predicted_location_test_set = lr_clf.predict(tweet_test_set)

print accuracy_score(location_test_set, predicted_location_test_set)
