def easy_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello there! How can I assist you today"

    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, but I'm here to help you!"

    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"

    else:
        return "I'm Sorry, I didn't understand that."

while True:
    user_input = input("User:")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = easy_chatbot(user_input)
    print("Chatbot", response)                   