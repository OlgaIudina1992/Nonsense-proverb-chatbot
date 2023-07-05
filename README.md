# Nonsense-proverb-chatbot
A simple chatbot based on a corpus of proverbs and several other corpora to provide the user with comic relief

Corpus creation from Ch.G. Rossetti's poems and preliminary analysis of word frequency: https://www.kaggle.com/code/olgaiudina/rossetti-corpus/notebook

This personal project started off as a challenge to create a rule-based chatbot that could, to some extent, replicate the behavior of a generative AI chatbot with only conditional loops and functions, project an impression of learning from user feedback and create nonsense phrase to offer users advice on a variety of topics.

At the start of conversation, NonsenseBot asks the user for their name, and whether or not they would like to continue communication. If the user confirms and presents a topic they are interested in, the bot will generate advice and request feedback as follows:
![image](https://github.com/OlgaIudina1992/Nonsense-proverb-chatbot/assets/110724838/5903b850-2f73-4c6c-a48e-00213a5d7af7)
Based on whether the communication was insightful for the user, the bot will offer different reactions to the feedback. Then the user is free to request additional advice or finsh the communication:

![image](https://github.com/OlgaIudina1992/Nonsense-proverb-chatbot/assets/110724838/cdf774ea-f26e-445a-85c5-d3eea88c5e61)

Or:

![image](https://github.com/OlgaIudina1992/Nonsense-proverb-chatbot/assets/110724838/e11352ed-59d3-4a48-bdcb-1584f0eaa7b7)

Here is the additional request:

![image](https://github.com/OlgaIudina1992/Nonsense-proverb-chatbot/assets/110724838/0c5c1952-69be-4ed5-90f0-9b701eaf6df2)

To generate this simple interaction, the chatbot relies on random selection from a corpus of standard English-language proverbs, some part of which was replaced with POS-tagged words from several other corpora (MIT corpus, an animal name collection and Ch.G. Rossetti's poetry were used to make it fun). The replacement is also based on random choice function, which enables the chatbot to create fresh responses each time it is asked for advice. Please check the code for more details.

To sum up:

The main idea behind this project was to build on a basic random quote machine by using text mining and other NLP strategies. First, three blocks of text were developed to provide corpora for the chatbot. Items from the corpora were pos-tagged and randomly assigned to substitute for parts of specifically collected proverbs. Finally, the proverbs were randomly offered to the user during their interaction with the chatbot. As a simple system this project has much room for improvement. 

Possibilities include:
* sentiment analysis of the user at the start and feedback stages of the interaction, 
* vectorization of the user's request and grouping the proverbs themselves intent-wise,
* improvement of the grammar rules for article matching and correct plural endings of nouns.
