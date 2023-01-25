import os
import sys
import openai

openai.api_key = os.getenv("OpenAPIKey")

response = openai.Completion.create(model="text-davinci-003", prompt=sys.argv[1], temperature=0, max_tokens=500)

print(response.choices[0].text)
