import random
import json
import time

# Load keywords and responses from a JSON file
def load_keywords():
    return {
        "coffee": [
            "The campus coffee bar opens at 8:00 AM and closes at 4:00 PM.",
            "We have a great coffee bar! It opens from 8 AM to 4 PM."
        ],
        "library": [
            "The library is open from 9 AM to 9 PM during the weekdays.",
            "You can visit the library from 9 AM to 9 PM."
        ],
        "admissions": [
            "You can apply for admission online through our university website.",
            "For admission details, please visit the University Admissions page."
        ],
        "course": [
            "We offer a variety of courses. Could you specify the department you're interested in?",
            "What course are you looking for? We have many options across departments."
        ]
    }

# Function to generate a random agent name
def get_random_agent_name():
    agent_names = ['Alex', 'Jordan', 'Taylor', 'Casey', 'Sam']
    return random.choice(agent_names)

# Function to log questions and responses to a file
def log_conversation(question, response):
    with open('chat_log.txt', 'a') as log_file:
        log_file.write(f"Question: {question}\nResponse: {response}\n\n")

# Function to get a response based on user's input
def get_response(user_input, keywords):
    # Convert user input to lowercase for easier keyword matching
    user_input = user_input.lower()
    for keyword, responses in keywords.items():
        if keyword in user_input:
            return random.choice(responses)
    # If no keywords match, return a random response
    random_responses = [
        "That's an interesting question, let me think about it!",
        "Hmm, I'm not sure about that. Can you ask something else?",
        "I'm not sure how to answer that, but I can help with other questions!"
    ]
    return random.choice(random_responses)

def chatbot():
    # Greet the user
    user_name = input("Hello! What's your name? ")
    print(f"Hi {user_name}, welcome to the University of Poppleton chat! How can I help you today?")

    # Display a random agent name
    agent_name = get_random_agent_name()
    print(f"Your agent for today is {agent_name}. Let's chat!")

    # Load keyword-based responses
    keywords = load_keywords()

    # Start the conversation loop
    while True:
        # Get user's question
        user_question = input(f"{user_name}: ")

        # Exit the conversation if the user types a termination word
        if user_question.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye {user_name}, have a great day!")
            break

        # Get the appropriate response
        response = get_response(user_question, keywords)

        # Log the conversation
        log_conversation(user_question, response)

        # Simulate a delay in response
        time.sleep(1)

        # Print the agent's response
        print(f"{agent_name}: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
