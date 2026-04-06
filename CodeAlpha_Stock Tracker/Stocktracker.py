print("Welcome! I am a simple chatbot ")

while True:
    user_message = input("You: ").lower()

    if user_message == "hello":
        print("Bot: Hi there!")
    elif user_message == "how are you":
        print("Bot: I'm doing great!")
    elif user_message == "bye":
        print("Bot: Goodbye ")
        break
    else:
        print("Bot: I don't understand.")