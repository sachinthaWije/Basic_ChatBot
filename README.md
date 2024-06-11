# Basic Chatbot in Python

This repository contains a basic text-based chatbot implemented in Python using the Natural Language Toolkit (NLTK). The chatbot can engage in simple conversations with users based on predefined patterns and responses.

## Features

- Responds to greetings and common questions.
- Uses regular expressions to match user inputs.
- Simple and easy to extend with more patterns and responses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
2. Change to the project directory:
    ```bash
    cd your-repo-name
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```bash
    pip install nltk
    ```

## Usage

1. Ensure you have the necessary NLTK data downloaded:
    ```python
    import nltk
    nltk.download('punkt')
    ```
2. Run the chatbot:
    ```bash
    python main.py
    ```
