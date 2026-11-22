from textblob import TextBlob

print("Welcome to Spy")

user_name = input("Please enter your name: ").strip()
if not user_name:
    user_name = "Anonymous"

conversation_history = []

print(f"Hello, {user_name}! Let's start our conversation. Type 'exit' to end the chat,history' to view conversation history, or 'reset' to clear the history.")

while True:
    user_input = input(">> ").strip()

    if not user_input:
        print("Please enter a message.")
        continue

    if user_input.lower() == 'exit':
        print(f"Goodbye, Agent {user_name}!")
        break

    elif user_input.lower() == 'reset':
        conversation_history.clear()
        print("Conversation history cleared.")
        continue

    elif user_input.lower() == 'history':
        if not conversation_history:
            print("No conversation history available.")
        else:
            print("\nConversation History:")
            for idx, (text, polarity, sentiment) in enumerate(conversation_history, start=1):
                print(f"{idx}. {text} | Polarity: {polarity:.2f} | Sentiment: {sentiment}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive 😊"

    elif polarity < -0.25:
        sentiment = "Negative 😞"

    else:
        sentiment = "Neutral 😐"

    conversation_history.append((user_input, polarity, sentiment))

    print(f"{sentiment} sentiment detected with polarity {polarity:.2f}.")


    


