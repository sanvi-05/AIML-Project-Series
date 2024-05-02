# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

class SimpleChatbot:
    def __init__(self):
        self.previous_interaction = []

    def greet(self):
        return "Hello! I'm a simple chatbot. How can I assist you today?"

    def basic_responses(self, question):
        responses = {
            "How are you?": ["I'm doing well, thank you!", "Feeling good, thanks for asking!"],
            "What is your name?": ["I'm just a simple chatbot, you can call me ChatBot!", "I don't have a name, but you can refer to me as ChatBot."],
            "What can you do?": ["I can answer your questions and have a simple conversation with you.", "I'm here to assist you with basic queries."],
            "Who created you?": ["I was created by a team of developers.", "I'm a creation of some brilliant minds!"],
            "Goodbye": ["Goodbye! Have a great day!", "Goodbye! Take care!"]
        }
        return random.choice(responses.get(question, ["I'm sorry, I didn't understand that."]))

    def ask_question(self, question):
        if question:
            self.previous_interaction.append(question)

        if len(self.previous_interaction) > 3:
            return "You've asked enough questions for now. How can I assist you further?"
        elif len(self.previous_interaction) > 0:
            return "What else would you like to know?"

    def respond(self, message):
        if message.endswith("?"):
            response = self.basic_responses(message)
        else:
            response = "I'm sorry, I didn't understand that."

        return response

# Example usage
chatbot = SimpleChatbot()

print(chatbot.greet())

for _ in range(3):
    user_input = input()
    print(chatbot.ask_question(user_input))
    user_input = input()
    print(chatbot.respond(user_input))

print("Goodbye!")
