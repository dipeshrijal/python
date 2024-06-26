from openai import OpenAI

client = OpenAI(api_key="")


completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system",
                                                    "content": "You are a helpful assistant."},
                                                {"role": "user", "content": "Hello!"}
                                            ],
                                            stream=True)

for chunk in completion:
    print(chunk.choices[0].delta)
