import spacy
import re
import markovify
import nltk
from nltk.corpus import gutenberg
import warnings
warnings.filterwarnings('ignore')nltk.download('gutenberg')

#inspect Gutenberg corpus
print(gutenberg.fileids())

#import novels as text objects
hamlet = gutenberg.raw('shapespeare-hamlet.txt')
macbeth = gutenberg.raw('shakespeare-macbeth.txt')
caesar = gutenberg.raw('shakespeare-caesar.txt')#print first 100 characters of each
print('\nRaw:\n', hamlet[:100])
print('\nRaw:\n', macbeth[:100])
print('\nRaw:\n', caesar[:100])

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

#remove chapter indicator
hamlet = re.sub(r'Chapter \d+', '', hamlet)
macbeth = re.sub(r'Chapter \d+', '', macbeth)
caesar = re.sub(r'Chapter \d+', '', caesar)

#apply cleaning function to corpus
hamlet = text_cleaner(hamlet)
caesar = text_cleaner(caesar)
macbeth = text_cleaner(macbeth)

#parse cleaned novels
nlp = spacy.load('en')
hamlet_doc = nlp(hamlet)
macbeth_doc = nlp(macbeth)
caesar_doc = nlp(caesar)

hamlet_sents = ' '.join([sent.text for sent in hamlet_doc.sents if len(sent.text) > 1])
macbeth_sents = ' '.join([sent.text for sent in macbeth_doc.sents if len(sent.text) > 1])
caesar_sents = ' '.join([sent.text for sent in caesar_doc.sents if len(sent.text) > 1])shakespeare_sents = hamlet_sents + macbeth_sents + caesar_sents

#inspect our text
print(shakespeare_sents)

#create text generator using markovify
generator_1 = markovify.Text(shakespeare_sents, state_size=3)

#We will randomly generate three sentences
for i in range(3):
  print(generator_1.make_sentence())#We will randomly generate three more sentences of no more than 100 characters
for i in range(3):
  print(generator_1.make_short_sentence(max_chars=100))