from bs4 import BeautifulSoup
import requests

import string
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

lemmatizer = WordNetLemmatizer()

### Miscellania corpus ###
build_response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')

misc_text = build_response.content
soup = BeautifulSoup(misc_text, "html.parser")

misc = soup.get_text()
misc_sep = misc.split()

misc_lemmes = [lemmatizer.lemmatize(word) for word in misc_sep]
misc_unique = list(set(misc_lemmes))
misc_unique = [i for i in misc_unique if len(i) > 2]
misc_clean = [i for i in misc_unique if i]

misc_pos = nltk.pos_tag(misc_clean)

misc_nouns = [word[0] for word in misc_pos if word[1] == 'NN']
#print(misc_nouns[0:10])

misc_verbs = [word[0] for word in misc_pos if word[1] == 'VB']
#print(misc_verbs[0:10])

misc_adjs = [word[0] for word in misc_pos if word[1] == 'JJ']
#print(misc_adjs[0:10])

misc_advs = [word[0] for word in misc_pos if word[1] == 'RB']
#print(misc_advs[0:10])

misc_vbn = [word[0] for word in misc_pos if word[1] == 'VBN']
#print(misc_vbn[0:10])

misc_vbg = [word[0] for word in misc_pos if word[1] == 'VBG']
#print(misc_vbg[0:10])
