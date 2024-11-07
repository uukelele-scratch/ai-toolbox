import nltk
nltk.download('punkt_tab')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('ScratchGPT')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

trainer.train("chatterbot.corpus.english","chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations")


def respondto(msg):
	if msg != "" and msg != " ":
		return chatbot.get_response(msg)