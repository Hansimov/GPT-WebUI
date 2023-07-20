from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


def connect_database(host="localhost", port=27027, database="gpt-webui"):
    mongodb_uri = f"mongodb://{host}:{port}"
    client = MongoClient(mongodb_uri)
    db = client[database]
    return db


@app.route("/messages")
def get_latest_messages():
    db = connect_database()
    messages = []
    if "latest" in request.args:
        messages = db["messages"].find_one()["latest_messages"]

    return jsonify(messages)


@app.route("/configs")
def get_llm_configs():
    db = connect_database()
    configs = {}
    if "llm" in request.args:
        configs = db["configs"].find_one()["llm"]

    return jsonify(configs)


app.run(debug=True)
