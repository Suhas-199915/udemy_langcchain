import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {"role": "user", "content": "Hello, how can I help you today?"}
    ]
)

print(chat_response.choices[0].message.content)