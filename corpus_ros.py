from bs4 import BeautifulSoup
import requests
import string
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

### Rossetti corpus ###
build_response = requests.get('https://www.gutenberg.org/cache/epub/19188/pg19188-images.html')

cgr_text = build_response.content
soup = BeautifulSoup(cgr_text, "html.parser")

poetry = soup.get_text()
poetry = re.sub(r'\n', ' ', poetry)
poetry = re.sub(r'\r', ' ', poetry)
poetry = re.sub(r'\'s', ' ', poetry)
poetry = re.sub('\d', ' ', poetry)
poetry = poetry.translate(str.maketrans(' ', ' ', string.punctuation))

lemmatizer = WordNetLemmatizer()
poetry_tokens = word_tokenize(poetry)
poetry_tokens = [x.lower() for x in poetry_tokens]
poetry_tokens = poetry_tokens[256:-2913]

#final corpus
extracted_corpus = poetry_tokens
extracted_lemmes = [lemmatizer.lemmatize(word) for word in extracted_corpus]
extracted_corpus_pos = nltk.pos_tag(extracted_lemmes)

poetry_unique = set(extracted_corpus_pos)
#pos groups:

ros_nouns = [word[0] for word in poetry_unique if word[1] == 'NN']
#print(ros_nouns[0:10])

ros_verbs = [word[0] for word in poetry_unique if word[1] == 'VB']
#print(ros_verbs[0:10])

ros_adjs = [word[0] for word in poetry_unique if word[1] == 'JJ']
#print(ros_adjs[0:10])

ros_advs = [word[0] for word in poetry_unique if word[1] == 'RB']
#print(ros_advs[0:10])

ros_vbn = [word[0] for word in poetry_unique if word[1] == 'VBN']
#print(ros_vbn[0:10])

ros_vbg = [word[0] for word in poetry_unique if word[1] == 'VBG']
#print(ros_vbg[0:10])
