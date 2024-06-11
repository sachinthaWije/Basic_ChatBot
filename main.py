import nltk
from nltk.chat.util import Chat, reflections

# Download the NLTK data
nltk.download('punkt')


# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that.", "All right, good to know.",]
    ],
    [
        r"quit",
        ["Bye-bye! Take care.", "Goodbye! It was nice talking to you.",]
    ],
    [
        r"good morning",
        ["Good morning! How can I assist you today?",]
    ],
    [
        r"good night",
        ["Good night! Sleep well.",]
    ],
    [
        r"thank you",
        ["You're welcome!", "No problem at all!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ]
    
    
]

# Create a reflections dictionary
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)


def chat():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(response)

# Start chatting
if __name__ == "__main__":
    chat()
