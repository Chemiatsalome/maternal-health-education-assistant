import os
from flask import Flask, request, render_template
from together import Together

# Initialize the Together client with your API key
together_client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

# Create a Flask app
app = Flask(__name__)

def query_agent(user_question):
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": """You are an AI assistant specializing in maternal health education. Your task is to answer user questions about maternal health with detailed, accurate, and contextually relevant information.
                Address questions related to:
                - Key health monitoring practices during pregnancy.
                - Essential educational topics for expectant mothers.
                - Preventive care measures and recommended screenings.
                - Common risk factors and screenings.
                Ensure responses are clear and helpful, and cover the specifics of the user’s question."""
            },
            {
                "role": "user",
                "content": f"Here's the user's question on maternal health: {user_question}"
            }
        ],
        max_tokens=1500,  # Ensure there's enough space for detailed answers
        temperature=0.7,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"]
    )
    
    answer = response.choices[0].message.content
    return answer

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        user_question = request.form.get('question')
        if user_question:
            answer = query_agent(user_question)
    return render_template('index.html', answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
