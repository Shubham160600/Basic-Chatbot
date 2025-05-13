def chatbot():
    print("Hi! I'm ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        elif "how are you" in user_input:
            print("ChatBot: I'm doing great! How about you?")
        elif "name" in user_input:
            print("ChatBot: I’m a Python chatbot.")
        else:
            print("ChatBot: Sorry, I didn’t understand that.")

chatbot()
