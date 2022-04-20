# Program Description: Assign a sentiment of positive, negative, neutral to tweet data stored in CSVs

import pandas as pd
import glob
import os
import warnings
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# obtain list of CSVs stored in directory
path = "c:/Users/amank/PycharmProjects/Data Projects/Bitcoin Sentiment Analysis/Raw Data/"
csv_files = glob.glob(os.path.join(path, "*.csv"))

# supress any warning messages declared by pandas library
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('display.max_columns', None)


# Clean tweet data
def clean_tweets(tweet_df):
    cln_tweets = []

    for t in tweet_df['Tweet'].iteritems():
        tweet = t[1]
        tweet = re.sub('#bitcoin', 'bitcoin', tweet)  # remove # from bitcoin keyword
        tweet = re.sub('#Bitcoin', 'Bitcoin', tweet)  # remove # from bitcoin keyword
        tweet = re.sub('#[A-Za-z0-9]+', '', tweet)  # replace words that begin with #
        tweet = re.sub('@[A-Za-z0-9]+', '', tweet)  # replace words that begin with @
        tweet = re.sub('$[A-Za-z0-9]+', '', tweet)  # replace words that begin with $
        tweet = re.sub('\\n', ' ', tweet)  # replace new line with space
        tweet = re.sub('https?:\/\/\S+', '', tweet)  # remove hyperlinks
        tweet = re.sub(r"^\s+|\s+$", '', tweet)  # remove trailing and leading spaces
        tweet = re.sub(r"\s+", " ", tweet)  # sub multiple whitespaces with single whitespace
        cln_tweets.append(tweet)

    tweet_df['Clean_Tweets'] = cln_tweets
    return tweet_df


# Assign polarity to each tweet. Create separate columns for positive, negative, neutral.
def sentiment_analyzer(tweet_df):
    obj = SentimentIntensityAnalyzer()
    compound = []
    neg = []
    pos = []
    neu = []
    for i in tweet_df['Clean_Tweets'].iteritems():
        compound.append(obj.polarity_scores(i[1])['compound'])
        neg.append(obj.polarity_scores(i[1])['neg'])
        pos.append(obj.polarity_scores(i[1])['pos'])
        neu.append(obj.polarity_scores(i[1])['neu'])

    tweet_df['pos'] = pd.Series(pos)
    tweet_df['neg'] = pd.Series(neg)
    tweet_df['neu'] = pd.Series(neu)
    tweet_df['compound'] = pd.Series(compound)
    return tweet_df


tw = []
# read csv files into dataframe and clean tweets'
for f in csv_files:
    tweet_data = pd.read_csv(f)
    tweet_data = clean_tweets(tweet_data)
    tw.append(tweet_data)   # append CSV file to list

# convert list to pandas dataframe
tweet_data = pd.concat(tw, axis=0, ignore_index=True)

# analyze sentiment of each tweet and store as separate columns in dataframe
tweet_data = sentiment_analyzer(tweet_data)

# output resulting data in CSV file
tweet_data.to_csv('results.csv', float_format='%.3f')
