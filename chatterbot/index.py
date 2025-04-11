from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False, 
              logic_adapters=[
                    {
                        "import_path":"chatterbot.logic.BestMatch",
                        "default_response": "I am sorry, but I do not understand.",
                        "maximum_similarity_threshold": 0.90
                    }
                    ])


# copy array and make new one with new responses to train more than one response to same question
# list_to_train = [
#     "Hello",
#     "Hi there!",
#     "How are you?",
#     "I'm doing well, thank you!",
#     "What is your name?",
#     "My name is ChatBot." 
    
# ]
# list_to_train = [
#     "Hello",
#     "Hi there!",
#     "how r u",
#     "I'm doing well, thank you!",
#     "What is your name?",
#     "My name is ChatBot." 
    
# ]
# ]
# list_to_train = [
#     "Hello",
#     "Hi there!",
#     "how r u",
#     "I'm doing fine!",
#     "What is your name?",
#     "My name is ChatBot." 
    
# ]


# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    return render_template("index.html")
    

# while True:
#     user_response = input("User: ")
#     if user_response.lower() == "bye":
#         print("Chatbot: Goodbye!")
#         break
#     else:
#         # Get a response from the chatbot
#         print("Chatbot: " + str(bot.get_response(user_response)))

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    #rawData = requests.get("")
    #result = rawData.json()
    #call in index data.main.temp
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
    