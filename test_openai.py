from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
{
"role": "user",
"content": "Tell me about Python"
}
]
)

print(response.choices[0].message.content)
