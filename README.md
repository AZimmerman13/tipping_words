# tipping_words
A twitter bot to generate tweets based on the content made by the boys at @tipping_pitches

How to run this dang thing:

Create your own env file, populate it with these items that you get when you create a twitter developer account:


APP_KEY = 
APP_SECRET = 
BEARER_TOKEN = 
CLIENT_ID = 
CLIENT_SECRET = 
ACCESS_TOKEN =
ACCESS_TOKEN_SECRET =

run load_tweets.py to get 100 most recent tweets and add them to the corpus

run model.py to generate tweets and post to twitter