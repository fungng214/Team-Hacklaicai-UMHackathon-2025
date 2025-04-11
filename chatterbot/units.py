from chatterbot import ChatBot


bot = ChatBot("Units", logic_adapters=["chatterbot.logic.UnitConversion"])

print("------------ Unit Conversion Chatbot ---------------")

while True:
    user_response = input("type the unit that you want to convert: ")
    if user_response.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        # Get a response from the chatbot
        print("Chatbot: " + str(bot.get_response(user_response)))