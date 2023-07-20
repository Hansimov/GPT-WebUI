from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/messages")
def get_messages():
    messages = [
        {"model": "user", "role": "user", "content": "What is your model?"},
        {
            "model": "gpt-4",
            "role": "llm",
            "content": "I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks.",
        },
        {
            "model": "gpt-3.5",
            "role": "llm",
            "content": "I am ChatGPT, an AI language model created by OpenAI. I'm based on the GPT-3.5 architecture, designed to understand and generate human-like text based on the data I've been trained on. My purpose is to assist and provide helpful information on a wide range of topics. If you have any questions or need assistance, feel free to ask!",
        },
        {"model": "claude-2", "role": "llm", "content": "I am Claude-2"},
    ]
    return jsonify(messages)


@app.route("/llm_configs")
def get_llm_configs():
    llm_configs = {
        "user": {
            "name": "User",
            "class": "user-chats",
            "avatar": "src/assets/user.png",
        },
        "gpt-3.5": {
            "name": "GPT-3.5",
            "class": "gpt-35-chats",
            "avatar": "src/assets/gpt-3.5.png",
        },
        "gpt-4": {
            "name": "GPT-4",
            "class": "gpt-4-chats",
            "avatar": "src/assets/gpt-4.png",
        },
        "claude-2": {
            "name": "Claude-2",
            "class": "claude-2-chats",
            "avatar": "src/assets/claude-2.png",
        },
    }
    return jsonify(llm_configs)


app.run()
