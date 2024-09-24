import random

# Define your intents dictionary
intents = {
    "intents": [
        {
            "patient": ["Hi", "Hello", "Is anyone there?", "Good day", "Hey"],
            "cre": ["Hello, welcome to our hospital chatbot!", "Hi there, how can I assist you with your healthcare needs?"]
        },
        {
            "patient": ["What are your visiting hours?", "When can I visit?", "What time does the hospital open?", "Hospital timings"],
            "cre": ["Our visiting hours are from 9 AM to 8 PM every day."]
        },
        {
            "patient": ["How do I book an appointment?", "How can I schedule a consultation?", "I need to book an appointment"],
            "cre": ["You can book an appointment by calling us at 123-456-7890 or through our online portal at hospitalwebsite.com."]
        },
        {
            "patient": ["What are your services?", "What medical services do you provide?", "Services offered by the hospital"],
            "cre": ["We offer a wide range of services including general check-ups, surgery, maternity care, and emergency services."]
        },
        {
            "patient": ["Can I speak to a doctor?", "I need to consult with a doctor", "How can I talk to a doctor?"],
            "cre": ["You can schedule a consultation with one of our doctors by booking an appointment. If it's an emergency, please visit our emergency room."]
        },
        {
            "patient": ["Do you accept insurance?", "Which insurance do you accept?", "Payment and insurance information"],
            "cre": ["Yes, we accept most major insurance plans. Please contact our billing department for more details."]
        },
        {
            "patient": ["Thank you", "Thanks", "That helps"],
            "cre": ["You're welcome! Let me know if you have any other questions."]
        },
        {
            "patient": ["Goodbye", "Bye", "See you later"],
            "cre": ["Goodbye! Take care and feel free to reach out anytime."]
        }
    ]
}

# Function to handle user input and provide appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['patient']:
            if pattern.lower() in user_input:
                return random.choice(intent['cre'])
    # Default response when input doesn't match any pattern
    return "I'm not sure how to respond to that. Please contact our support team at 123-456-7890 for further assistance."

def chat():
    print("Chatbot: Hello! How can I assist you today? (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
