> **Note:**
> All the commands should run in path `./backend` if not specified.

# Install python packages

```sh
python -m pip install -r requirements.txt
```

# Backend commands

```sh
python app.py # localhost:5000
```

# Install MongoDB, mongosh, mongodb tools

Remember to add the MongoDB and tools bin folder to the PATH environment variables.

* Download: MongoDB Community Edition on Windows
  * https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
  * https://www.mongodb.com/try/download/community
* Download: MongoDB Command Line Database Tools
  * https://www.mongodb.com/try/download/database-tools
* Download: mongosh
  * https://www.mongodb.com/try/download/shell


# mongodb commands

Launch database:

```sh
# mkdir database
mongod --dbpath "./database/" --port 27027
```

Dump database:

```sh
mongodump --host="localhost:27027" --db="gpt-webui" --out "dump"
```

Restore database:

```sh
mongorestore --host="localhost:27027" --db "gpt-webui" --drop "dump/gpt-webui"
```

Rename collection:

```sh
# in mongosh of MongoDB Compass
use gpt-webui
db.llm_configs.renameCollection("configs")
```