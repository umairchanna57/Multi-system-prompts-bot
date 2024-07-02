# Multi-System Prompts Bot

This project is an AI chatbot utilizing the LLM Mistral Algorithm to provide various functionalities through system prompts. The bot can tell jokes, provide cooking recipes, and give up-to-date news about the War in Palestine.

## Features

- **Joke Assistant**: Tells jokes in JSON format.
- **Chef Assistant**: Provides step-by-step guidelines for making a dish.
- **News Assistant**: Gives up-to-date news about the War in Palestine with citations.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/umairchanna57/Multi-system-prompts-bot.git
    cd Multi-system-prompts-bot
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your secret key**:
    ```env
    SEC_KEY=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
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

6. **Open your browser and go to** `http://127.0.0.1:5000`

## Usage

1. **Joke Assistant**:
    - Enter a topic to hear a joke.
    - Example: "Tell me a joke about computers."

   
<div align="center">
  <img width="512" src="static/img/joke.png">
</div>


2. **Chef Assistant**:
    - Enter the name of a dish to get a recipe.
    - Example: "How do I make spaghetti carbonara?"

  
<div align="center">
  <img width="512" src="static/img/chef.png">
</div>


3. **News Assistant**:
    - Enter a date to get news about the War in Palestine.
    - Example: "What happened on 2024-06-25?"

<div align="center">
  <img width="512" src="static/img/news.png">
</div>

