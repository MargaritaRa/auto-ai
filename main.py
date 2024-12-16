from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
model = "gpt-3.5-turbo-16k"

#  Create our Assistant #
auto_ai_assis = client.chat.completions.create(
    model=model,
    messages=[
        {   "role": "system", 
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "I need help with my car and where to fix it?"
        }
    ]
)
print(auto_ai_assis.choices[0].message)