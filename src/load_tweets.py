import tweepy
import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path



"""
{
  "data": [
    {
      "id": "888790426995621888",
      "name": "Tipping Pitches",
      "username": "tipping_pitches"
    }
  ]
}

"""

def load_tweets():
    dotenv_path = Path('../.env')
    load_dotenv(dotenv_path=dotenv_path)

    APP_KEY = os.getenv('APP_KEY')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    APP_SECRET = os.getenv('APP_SECRET')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')


    #authenticating to access the twitter API
    auth=tweepy.OAuthHandler(APP_KEY,APP_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)
    client = tweepy.Client(auth)

    # client.get_users_tweets(id=888790426995621888,tweet_fields=['created_at'])

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }

    params = {
        'max_results': '100'
    }

    response = requests.get('https://api.twitter.com/2/users/888790426995621888/tweets', params=params, headers=headers)
    

    with open('tweets.json', 'wb') as f:
        f.write(response.content)
    
    return

def update_corpus():
    with open('tweets.json') as json_file:
        data = json.load(json_file)

    #append the new text to the corpus file
    with open('rawtext.txt', 'a') as f:
        for i in range(len(data['data'])):
            f.write(str(data['data'][i]['text']).replace('\n'," ").strip())
            # f.write(str(data['data'][i]['text']))
            f.write('.\n')
    return
    


load_tweets()
print("\nNew tweets downloaded to json\n")
update_corpus()
print("\nCorpus updated...\n")