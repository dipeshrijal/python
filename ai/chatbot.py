import os
from openai import OpenAI

client = OpenAI(
    api_key="")

# Set your OpenAI API key

# Define a function to generate response using OpenAI


def generate_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
                "content":
                """Given the input above, please find the intent and describe in one word of what user is trying to request and extrat the shipment number and the email for the request in the format below.  if no email is provided prompt again to ask for an email address. don't modify the output format"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.7,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].message.content.strip()


# Example conversation loop
print("Welcome to the Chatbot!")
print("You can exit the conversation by typing 'exit'.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = generate_response(user_input + "\nUser: ")
    print("Chatbot:", response)
