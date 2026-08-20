def chatbot(message):
    message = message.lower().strip()
    if message == "hello":
        return "Hi! Nice to meet you."
    elif message == "how are you":
        return "I'm doing fine. Thank you."
    elif message == "bye":
        return "Goodbye! See you again."
    else:
        return "Sorry, I don't understand."

while True:
    message = input("Input: ")
    output = chatbot(message)
    print("Output:", output)
    if message == "bye":
        break