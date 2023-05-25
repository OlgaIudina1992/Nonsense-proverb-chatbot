import random
from proverb_mock import proverbs, proverb_twist
import time
import string

neg_corpus = ['no', 'not', 'nope', 'nah', 'dont', 'sorry', 'out', 'quit', 'pass', 'later', 'afraid', 'unfortunately', 'doubt', 'nothing', 'nuh', 'bad', 'worse', 'worst', 'gross', 'yuck', 'meh', 'ugh']

def chatbot_greet():
  print('Hello, stranger! My name is NonsenseBot and I simply LOVE to give advice.')
  time.sleep(1)
  name = input("What is your name?\n")
  print(f"Nice to meet you, {name}! It's a lovely name.\n")
  time.sleep(1)
  res = input(f'Would you like to ask me something, {name}?\n')
  res_words = res.lower().translate(str.maketrans(' ', ' ', string.punctuation)).split()
  intersect = set(res_words).intersection(neg_corpus)
  if len(intersect) > 0:
    print('Okay, have a niche day!')
    return
  else:
    advice_exec()

def advice_exec():
  advice = input(f'Tell me, what can I help you with? Name one thing.\n')
  advice_clean = advice.lower().translate(str.maketrans(' ', ' ', string.punctuation))
  intersect = set(advice_clean).intersection(neg_corpus)
  if len(intersect) > 0:
    print('Alright, see you later!')
    return
  else:
    print(f"Okay, some advice about {advice_clean} coming up!\n")
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Wait for it...")
    time.sleep(1)
    print('...')
    print("There! Ancient wisdom says:\n")
    time.sleep(1)
    print(random.choice(proverb_twist)) #can be replaced with proverbs variable imported above
    time.sleep(2)
    feedback = input('Was that helpful?\n')
    feedback_clean = feedback.lower().translate(str.maketrans(' ', ' ', string.punctuation)).split()
    intersect = set(feedback_clean).intersection(neg_corpus)
    if len(intersect) > 0:
      print('So sorry! I am still learning :)\n')
    else:      
      print('Aw, thank you! That warms my heart :)\n')
    more_advice()

def more_advice():
  time.sleep(1)
  repeat = input("Would you like to ask me something else?\n")
  repeat_words = repeat.lower().translate(str.maketrans(' ', ' ', string.punctuation)).split()
  intersect = set(repeat_words).intersection(neg_corpus)
  if len(intersect) > 0:
    print('Okay, have a niche day!')
    return
  else:
    advice_exec()
 

chatbot_greet()
