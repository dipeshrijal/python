from openai import OpenAI

client = OpenAI(api_key="sk-proj-Lh4g9CFbsDegaN6LcQzbT3BlbkFJ7rPZrxKocTlQs8U9Z2Xx")


completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello!"}
],
stream=True)

for chunk in completion:
  print(chunk.choices[0].delta)
