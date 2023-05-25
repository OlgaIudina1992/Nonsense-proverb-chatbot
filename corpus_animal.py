import string
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
### Animal corpus ###
with open("animal_names.txt") as file:
  animals = file.read()

animal_tokens = animals.lower().split(',')

animal_lemmes = [lemmatizer.lemmatize(word) for word in animal_tokens]

animal_unique = list(set(animal_lemmes))
animal_unique = [i.translate(str.maketrans('', '', string.punctuation)) for i in animal_unique]
animal_clean = [i for i in animal_unique if i]

animal_pos = nltk.pos_tag(animal_clean)

anim_nouns = [word[0] for word in animal_pos if word[1] == 'NN']
#print(anim_nouns[0:10])

anim_verbs = [word[0] for word in animal_pos if word[1] == 'VB']
#print(anim_verbs[0:10])

anim_adjs = [word[0] for word in animal_pos if word[1] == 'JJ']
#print(anim_adjs[0:10])

anim_advs = [word[0] for word in animal_pos if word[1] == 'RB']
#print(anim_advs[0:10])

anim_vbg = [word[0] for word in animal_pos if word[1] == 'VBG']
#print(anim_vbg[0:10])
