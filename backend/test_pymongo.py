from pymongo import MongoClient

"""
* Install MongoDB Community Edition on Windows
  * https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
  * https://www.mongodb.com/try/download/community
* Install mongosh
  * https://www.mongodb.com/try/download/shell
* Install MongoDB Database Tools
  * https://www.mongodb.com/try/download/database-tools
"""

# Connect to MongoDB database
mongodb_port = "27017"
mongodb_url = f"mongodb://localhost:{mongodb_port}"
client = MongoClient(mongodb_url)

db = client["gpt-webui"]
messages_collection = db["messages"]
llm_configs_collection = db["llm_configs"]

"""
# Insert messages into messages collection
messages = {
    "latest_messages": [
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
        {
            "model": "claude-2",
            "role": "llm",
            "content": "I am Claude-2",
        },
    ]
}

# Insert llm_configs into llm_configs collection
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

messages_collection.insert_one(messages)
llm_configs_collection.insert_one(llm_configs)
"""

# Get messages and llm_configs collections
llm_configs = llm_configs_collection.find_one()["llm_configs"]
print(llm_configs)
latest_messages = messages_collection.find_one()["latest_messages"]
print(latest_messages)
