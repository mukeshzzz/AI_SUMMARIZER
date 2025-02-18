import os
import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

def get_answer_from_text(text, question):
    """Answers questions based on extracted PDF content."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": f"Text: {text}\nQuestion: {question}"}
        ]
    )
    return response["choices"][0]["message"]["content"]
