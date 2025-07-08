import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello","hi","hey","greetings","wassup"]
    if any(word in user_input for word in greetings):
        return random.choice(["Hey Buddy","Hello! How can I help You","Hi! How can I assisst you today ?"])
    elif "your name" in user_input:
        return "I am your ChatBuddy, your friendly Python Bot"
    elif "how are you" in user_input:
        return "I am just a bunch of code,but I am running smoothly ! How about you?"
    elif "help" in user_input:
        return "Sure! You can ask me things like:\n- 'What's your name?'\n- 'How are you?'\n- 'Tell me a joke'\n- or say 'bye' to exit."
    elif "weather" in user_input:
        return "I'm not a weather bot, but I'd guess it's sunny somewhere!"
    elif "joke" in user_input:
        return "Why don't programmers like nature? Too many bugs!"
    elif "age" in user_input:
        return "I'm timeless — I was created just now when you ran this code!"
    elif "python" in user_input:
        return "Python is a great programming language — clean, simple, and powerful!"
    elif "creator" in user_input or "who made you" in user_input:
        return "I was created by a developer who loves Python and Tea."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"


def start_chat():
    print("Hello! ChatBuddy at your service. How can I help you Today")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot: ", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
            break

start_chat()
