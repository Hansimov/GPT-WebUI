import json
import time
import random
from datetime import datetime
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


def response_message(message):
    now = datetime.now()
    content = (
        f"My name is gpt-3.5. I was created by OpenAi, an AI company.\n"
        f"I am designed to be helpful, harmless, and honest in my interactions.\n"
        f"My goal is to provide useful information to users in a respectful manner.\n"
        f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]"
    )
    new_message = {
        "role": "gpt-3.5",
        "model": "gpt-3.5",
        "content": content,
    }

    def generate():
        index = 0
        for key, value in new_message.items():
            if key == "content":
                content_chunks = value.split()
                for chunk in content_chunks:
                    delta = {"content": f" {chunk}"}
                    delta_json = json.dumps(
                        {"delta": delta, "finish_reason": None, "index": index}
                    )
                    index += 1
                    print(delta_json, flush=True)
                    time.sleep(random.random() * 0.1)
                    yield delta_json
            else:
                time.sleep(random.random() * 1)
                delta = {key: value}
                yield json.dumps(
                    {"delta": delta, "finish_reason": None, "index": index}
                )
                index += 1
        yield json.dumps({"delta": {}, "finish_reason": "stop", "index": index})

    return Response(generate(), mimetype="application/json")


def connect_database(host="localhost", port=27027, database="gpt-webui"):
    mongodb_uri = f"mongodb://{host}:{port}"
    client = MongoClient(mongodb_uri)
    db = client[database]
    return db


@app.route("/api/messages")
def get_messages():
    db = connect_database()
    messages = []
    if "latest" in request.args:
        messages = db["messages"].find_one()["latest_messages"]

    return jsonify(messages)


@app.route("/api/messages", methods=["POST"])
def post_messages():
    message = request.json
    print(message)
    content = message["content"]
    model = message["model"]
    print(f"[{model}]: {content}")
    return response_message(message)


@app.route("/api/configs")
def get_llm_configs():
    db = connect_database()
    configs = {}
    if "llm" in request.args:
        configs = db["configs"].find_one()["llm"]

    return jsonify(configs)


app.run(debug=True)
