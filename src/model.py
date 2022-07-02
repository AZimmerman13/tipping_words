import spacy
import re
import os
import tweepy
import markovify
import nltk
from nltk.corpus import gutenberg
# from twython import Twython
from dotenv import load_dotenv
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
nltk.download('gutenberg')
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

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

APP_KEY = os.getenv('APP_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
APP_SECRET = os.getenv('APP_SECRET')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth=tweepy.OAuthHandler(APP_KEY,APP_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)


#import novels as text objects

tp = open('rawtext.txt', 'r')
tp = tp.read()

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = re.sub(r'https(.*)(?=.)', '', text) # this line removes QTs and GIFs
  text = re.sub(r'RT(.*)', '', text) #this line removes RTs
  text = re.sub(r'\@[^\s]*\s', '', text) # this line removes @handles
  text = ' '.join(text.split())
  return text



#apply cleaning function to corpus
tp = text_cleaner(tp)

#parse cleaned tweets
nlp = spacy.load('en_core_web_sm')
tp_doc = nlp(tp)

tp_sents = ' '.join([sent.text for sent in tp_doc.sents if len(sent.text) > 1])

#inspect our text
# print(tp_sents)

#create text generator using markovify
# generator_1 = markovify.Text(shakespeare_sents, state_size=3)
generator_1 = markovify.Text(tp_sents, state_size=2)


#We will randomly generate three sentences
# print("\n\nrandomly generate three sentences:\n")
# for i in range(3):
#   print(generator_1.make_sentence(tries=1000))
#We will randomly generate three more sentences of no more than 100 characters
# print("\n\nrandomly generate three more sentences of no more than 280 characters:\n")
# for i in range(3):
#   print(generator_1.make_short_sentence(max_chars=280))

#next we will use spacy's part of speech to generate more legible text
class POSifiedText(markovify.Text):   
    def word_split(self, sentence):
      return ['::'.join((word.orth_, word.pos_)) for word in nlp(sentence)]   
    def word_join(self, words):
      sentence = ' '.join(word.split('::')[0] for word in words)
      return sentence#Call the class on our text

generator_2 = POSifiedText(tp_sents, state_size=2)

#now we will use the above generator to generate sentences
# print("\n\nprint some POSified sentances:\n")
# for i in range(5):
  # print(generator_2.make_sentence(tries=1000))
#print 100 characters or less sentences
# print("\n\nprint some POSified sentances with maxchar=280:\n")
# for i in range(5):
#   print(generator_2.make_short_sentence(max_chars=280, tries=1000))


# loop to generate new tweets if you dont like the one you got 
loop = True
while loop==True:
  tweet = generator_2.make_short_sentence(max_chars=280, tries=1000)
  do_tweet = input(f"The tweet will be:\n\n{tweet}\n\n Would you like to tweet this (y/n)...")
  if do_tweet == 'y':
    api.update_status(status=tweet)
    break
  else:
    continue
