def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that."


def main():
    print("Simple Chatbot")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()
