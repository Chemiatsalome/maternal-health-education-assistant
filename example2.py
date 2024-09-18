import os
from together import Together
from openai import OpenAI

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {
                "role": "system",
                "content": "you are a helpful assistant. always answer in short. use bullet points."
        },
        {
                "role": "user",
                "content": "teach me the basics of Machine Learning. answer in short."
        }
],
    max_tokens=699,
    temperature=0.11,
    top_p=1,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>"],
    # stream=True
)
print(response.choices[0].message.content)


