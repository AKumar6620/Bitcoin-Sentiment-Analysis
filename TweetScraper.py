# Program Description: This program scrapes tweets from twitter and saves the data to a CSV file
import tweepy
import csv
import time


def authenticate(apikey, apisecret, accesstoken, accesssecret, bearertoken):
    # This function authenticates Twitter api credentials
    try:
        client = tweepy.Client(bearer_token=bearertoken, consumer_key=apikey, consumer_secret=apisecret, access_token=accesstoken, access_token_secret=accesssecret)
        print("Authentication successful :)")
    except:
        print("Authentication failed :(")
    return client


def get_tweets(client, Hashtags, account):
    # This function gathers up to 1000 recent tweets that are in reply to an account and contain specific keywords
    # Any retweets are filtered out
    q = ''
    i = 1
    for hashtag in Hashtags:
        if i == 1:
            q = '(' + hashtag
        else:
            q = q + ' OR ' + hashtag
        i = i + 1
    q = q + ') to:' + account + ' lang:en -is:retweet'

    tweets = tweepy.Paginator(client.search_recent_tweets, query=q, tweet_fields=['created_at'], max_results=100).flatten(limit=1000)
    return tweets


def tweets_to_csv(FilePath,tweets,to_account):
    # This function converts a list of tweets gathered using the search_recent_tweets function in Tweepy to a CSV file
    headers = ['To Author','Tweet_ID', 'Created_at', 'Tweet']
    tweet_list = []
    timestr = time.strftime("%Y%m%d-%H%M%S")

    for tweet in tweets:
        tweet_list.append([to_account, tweet.id, tweet.created_at, tweet.text])

    with open(FilePath + to_account + " - " + timestr + ".csv", "w", newline='', encoding='utf-8') as twt:
        t = csv.writer(twt)
        t.writerow(headers)
        t.writerows(tweet_list)


# Get API credentials from CSV File
with open('Credentials.csv') as csv_file:
    credentials = csv.reader(csv_file, delimiter=',')
    credentials_rows = list(credentials)

apiKey = credentials_rows[1][0]
apiSecret = credentials_rows[1][1]
accessToken = credentials_rows[1][2]
accessSecret = credentials_rows[1][3]
bearerToken = credentials_rows[1][4]

client = authenticate(apiKey, apiSecret, accessToken, accessSecret, bearerToken)
FilePath = "c:/Users/amank/PycharmProjects/Data Projects/Bitcoin Sentiment Analysis/Raw Data/"

# list of influencer crypto accounts
accounts = ['100trillionUSD', 'elonmusk', 'saylor', 'intocryptoverse', 'coinbureau', 'TheCryptoLark', 'woonomic', 'AltcoinDailyio', 'TechDec_52', 'Bitboy_crypto', 'BTC_Archive', 'TheMoonCarl', 'CryptoMichNL', 'APompliano',
            "CryptosR_US", "JRNYcrypto", "elliotrades", "SheldonEvans", "cryptomanran", "IOHK_Charles", "nayibbukele", "zhusu", "PeterLBrandt", "rektcapital", "Nebraskangooner", "KoroushAK", "TheCryptoDog", "BTC_JackSparrow",
            "crypto_birb", "crypto_blkbeard", "Pentosh1", "TrueCrypto28", "JonnyMoeTrades", "drei4u", "bensemchee", "BitcoinBroski", "julianhosp", "sunny_bitcoin", "CryptoTony__", "cointradernik", "bitcoin_dad", "Trader_M4tt",
            "CryptoNTez", "AlamedaTrabucco", "George1Trader", "TraderLenny", "kobratrading", "valcoins", "bensemchee", "ThinkingUSD"]

i = 1
for account in accounts:
    # 25 requests per 15 minutes
    if i == 26:
        i = 1
        time.sleep(900)

    tweets = get_tweets(client, ['bitcoin', 'btc'], account)
    tweets_to_csv(FilePath, tweets, account)
    i = i+1
