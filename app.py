from flask import Flask, request, render_template
import os
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, pydantic, 
from langchain_huggingface import HuggingFaceEndpoint


# Load environment variables from a .env file
load_dotenv()

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
sec_key = "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"


# Set environment variable for Hugging Face token
import os
os.environ['umair'] = sec_key


# Set up the Hugging Face endpoint
try:
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=256, temperature=0.7, api_key=sec_key)
except Exception as e:
    raise RuntimeError(f"Error setting up HuggingFaceEndpoint: {e}")

# Define the prompt templates for different tasks
prompts = {
    "Joke": ChatPromptTemplate.from_messages([
        ("system", "You are a funny assistant that tells jokes. Please respond with a joke in the form of 'setup' and 'punchline' in JSON format."),
        ("user", "Tell me a joke about {topic}")
    ]),
    "Chef": ChatPromptTemplate.from_messages([
        ("system", "You are a professional chef. Please provide step-by-step guidelines for making a dish."),
        ("user", "How do I make {dish}")
    ]),
    "News": ChatPromptTemplate.from_messages([
        ("system", "You are an informative assistant providing up-to-date news about the War in Palestine with citations."),
        ("user", "What happened on {date}")
    ])
}

# Define output parsers
output_parser = StrOutputParser()

# Initialize Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        task_choice = request.form['task_choice']
        
        if task_choice not in prompts:
            response = "Invalid task choice."
        else:
            prompt = prompts[task_choice]
            chain = prompt | llm | output_parser

            try:
                if task_choice == "Joke":
                    response = chain.invoke({'topic': input_text})
                elif task_choice == "Chef":
                    response = chain.invoke({'dish': input_text})
                elif task_choice == "News":
                    response = chain.invoke({'date': input_text})
            except HTTPError as e:
                response = f"HTTP error occurred: {e}. Request ID: {e.request_id}"
                print(f"HTTP error details: {e.response.text}")
            except Exception as e:
                response = f"An error occurred: {e}"
                print(f"General error: {e}")
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
