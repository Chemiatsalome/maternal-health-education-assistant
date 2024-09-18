# maternal-health-education-assistant
The application utilizes the meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo model from Together.AI for generating responses. 

# Maternal Health Education Assistant

This project is a Flask-based application that uses the Together AI model to provide answers to user questions about maternal health, specifically focused on first-trimester education. The application utilizes the `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo` model from Together AI to generate responses.

## Getting Started

### Prerequisites

1. **Python**: Ensure you have Python installed (preferably Python 3.7+).
2. **Flask**: The web framework used to create the web interface.
3. **Together API Key**: Required to access the Together AI model.

### Setup

#### 1. **Get Your Together API Key**

   - **Login to Together AI**: Go to the [Together AI Playground](https://api.together.ai/playground/chat/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo).
   - **Generate API Key**: Follow the instructions on the website to generate your API key. This key is necessary for authenticating API requests.

#### 2. **Clone the Repository**

   ```bash
   git clone https://github.com/username/maternal-health-education-assistant.git
   cd maternal-health-education-assistant

# Packages needed

pip install flask together

# Set Up Your Environment Variable

To keep your API key secure, use an environment variable rather than hardcoding it into your application. Create a .env file in your project directory and add your API key:


