def chatbot():
    print("Welcome to Chatbot")
    print("Type 'quit' to exit")

    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Bot: Hi")

        elif user == "how are you":
            print("Bot: I am fine,thank you for asking")

        elif user == "quit":
            print("Bot: Goodbye")
            break
        else:
            print("sorry, I dont understand")
chatbot()