
# Bitcoin Sentiment Analysis

This is a simple project that focuses on consolidating weekly tweets from top 50 crypto influencer accounts and determining the general sentiment of those tweets using Python's Vader library (positive, negative, neutral).

To do so, I used Twitter's Tweepy API V2. You'll need to create an account with Twitter and sign-up for their developer portal. Once done, you'll obtain the following which can be loaded into the credentials.csv file: 

- API Key
- API Key Secret
- Access Token
- Access Secret
- Bearer token

Next, run TweetScraper.py (ensure to change the download file path so that the program knows where to download the raw data).

Once that is complete, run SentimentAnalysis.py which will consolidate all raw tweet data and output a 'results.csv' file with the general sentiment of each tweet. 

Keep in mind, that Tweet data can be quite messy and can impact the accuracy of sentiment. I did my best to clean the tweets before processing, but I'm sure their is more room for improvement.

Other considerations: One of the problems with Natural Language Processing is that it can have trouble assessing sarcasm in a tweet or sentence.

For future iterations: With enough data it would be interesting to plot Sentiment against Price action :)

