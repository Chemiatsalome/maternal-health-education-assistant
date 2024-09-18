# 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


import os
import groq

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

llama_70B = "llama-3.1-70b-versatile"
llama_405B = "Not Available"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models and transalate in swahili",
        }
    ],
    model= llama_70B,
)

print(chat_completion.choices[0].message.content)