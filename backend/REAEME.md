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

Dump database:

```sh
# [./backend]
mongodump --host="localhost" --port=27027 --db="gpt-webui"
```