from chatterbot import ChatBot

bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("------------ Math Chatbot ---------------")


while True:
    user_response = input("type the math equation that you want to solve: ")
    if user_response.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        # Get a response from the chatbot
        print("Chatbot: " + str(bot.get_response(user_response)))