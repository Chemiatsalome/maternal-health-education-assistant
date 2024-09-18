import os
from flask import Flask, request, render_template
from together import Together
from googletrans import Translator

# Initialize the Together client with your API key
together_client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))
translator = Translator()

app = Flask(__name__)

def query_agent(user_question):
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": """You are an AI assistant specializing in maternal health education. Answer the following question with detailed, accurate, and contextually relevant information based on maternal health. Do not mention the classification process. Respond in the language of the question if it is Swahili or English."""
            },
            {
                "role": "user",
                "content": f"{user_question}"
            }
        ],
        max_tokens=1500,
        temperature=0.7,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"]
    )
    
    answer = response.choices[0].message.content
    return answer

def translate_to_swahili(text):
    translated = translator.translate(text, dest='sw')
    return translated.text

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        user_question = request.form.get('question')
        language = request.form.get('language', 'en')  # Default to English if no language specified
        
        # Print debug statement to check user question and language
        print(f"Debug: User question: {user_question}")
        print(f"Debug: Language selected: {language}")
        
        if user_question:
            answer = query_agent(user_question)
            if language == 'sw':
                answer = translate_to_swahili(answer)
    
    return render_template('index.html', answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
