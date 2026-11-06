
print("======================================")
print("          PYTHON CHATBOT")
print("======================================")

# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I'm Python Chatbot."

    elif user_input == "what can you do":
        return "I can answer simple predefined questions."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand your message."


# Main chatbot program
print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: You can start chatting with me.")
print("Chatbot: Type 'bye' to exit.")

while True:

    user_message = input("\nYou: ")

    response = chatbot_response(user_message)

    print("Chatbot:", response)

    if user_message.lower().strip() == "bye":
        break

print("Chatbot session ended.")
