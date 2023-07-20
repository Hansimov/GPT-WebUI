## Backend commands

```py
python app.py
```

## mongodb commands

Launch database:

```sh
# [./backend]
mongod --dbpath "./database/" --port 27027
```

Rename collection:

```sh
# in mongosh
use gpt-webui
db.llm_configs.renameCollection("configs")
```

Dump database:

```sh
# [./backend]
mongodump --host="localhost:27027" --db="gpt-webui" --out "dump"
```

Restore database:

```sh
# [./backend]
mongorestore --host="localhost:27027" --db "gpt-webui" --drop "dump/gpt-webui"
```