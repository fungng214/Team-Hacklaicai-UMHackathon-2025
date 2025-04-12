from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests
from multilingual_adapter import MultilingualAdapter
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from data_analysis import DataProcessor
import json as json



app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False, 
              logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',
                    'chatterbot.logic.UnitConversion',
                    {
                        "import_path":"chatterbot.logic.BestMatch",
                        "default_response": "I am sorry, but I do not understand.",
                        "maximum_similarity_threshold": 0.90
                    }
                    ])


# copy array and make new one with new responses to train more than one response to same question
#list_to_train = [
#     "Hello",
#     "Hi there!",
#     "How are you?",
#     "I'm doing well, thank you!",
#     "What is your name?",
#     "My name is ChatBot."  
# ]



# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.indonesian',
    'chatterbot.corpus.thai'
)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    if "top keywords" in userText.lower():
        return str(DataProcessor().get_top_keywords())
    elif "match" in userText.lower():
        return str(DataProcessor().get_match_items())
    elif "cuisine stats" in userText.lower():
        return str(DataProcessor().cuisine_stats())
    #rawData = requests.get("")
    #result = rawData.json()
    #call in index data.main.temp
    elif "visualise" in userText.lower():
        plot = DataProcessor().plot_data()
        return plot
    else:
        return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
    
    # while True:
#     user_response = input("User: ")
#     if user_response.lower() == "bye":
#         print("Chatbot: Goodbye!")
#         break
#     else:
#         # Get a response from the chatbot
#         print("Chatbot: " + str(bot.get_response(user_response)))
    