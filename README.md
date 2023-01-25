# Nonsense-proverb-chatbot
A simple chatbot based on a corpus of proverbs and several other corpora to provide the user with comic relief

Corpus creation from Ch.G. Rossetti's poems and preliminary analysis of word frequency: https://www.kaggle.com/code/olgaiudina/rossetti-corpus/notebook

The main idea behind this project was to build on a basic random quote machine by using text mining and other NLP strategies. First, three blocks of text were developed to provide corpora for the chatbot. Items from the corpora were pos-tagged and randomly assigned to substitute for parts of specifically collected proverbs. Finally, the proverbs were randomly offered to the user during their interaction with the chatbot. As a simple system this project has much room for improvement. 
Possibilities include:
* sentiment analysis of the user at the start and feedback stages of the interaction, 
* vectorization of the user's request and grouping the proverbs themselves intent-wise,
* improvement of the grammar rules for article matching and correct plural endings of nouns.
