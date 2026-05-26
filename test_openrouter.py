from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Jawab singkat dalam bahasa Indonesia: koneksi OpenRouter berhasil atau tidak?"
        }
    ],
    max_tokens=80
)

print(response.choices[0].message.content)
