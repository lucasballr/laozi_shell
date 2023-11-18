from openai import OpenAI
import config
client = OpenAI()

question = input("Ask your question: ")

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a code helper. You respond to each message with only the relevant code. If there is no relevant code in the response, explain the response with the smallest amount of text possible."},
    {"role": "user", "content": question}
  ]
)

print(completion.choices[0].message.content)

