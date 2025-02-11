from flask import Flask
from flask import request
import json

app = Flask(__name__)

id = 0
with open("data.json") as f:
    data = json.load(f)
    id += len(data)

@app.get("/users")
def users_get():
    with open("data.json") as f:
        data = json.load(f)
        return json.dumps(data)

@app.get("/users/<id>")
def users_show(id):
    with open("data.json") as f:
        data = json.load(f)
        user = [i for i in data if i["id"] == int(id)]
    if len(user) < 1:
        return json.dumps({ "error": "no user with id: " + id})
    else:
        return json.dumps(user[0])

@app.post("/users")
def users_post():
    payload = request.json
    global id
    id += 1
    payload["id"] = id
    with open("data.json") as f:
        data = json.load(f)
        data.append(payload)
    save_users(data)
    return json.dumps(data)

@app.put("/users/<id>")
def users_put(id):
    params = request.json        
    with open("data.json") as f:
        data = json.load(f)
        user = [i for i in data if i["id"] == int(id)]
    if len(user) < 1:
        return json.dumps({ "error": "no user with id: " + id})
    else:
        user = user[0]
        for key in params:
            user[key] = params[key]
        save_users(data)
        return json.dumps(user)

@app.delete("/users/<id>")
def users_delete(id):
    with open("data.json") as f:
        data = json.load(f)
        user = [i for i in data if i["id"] == int(id)]
    if len(user) < 1:
        return json.dumps({ "error": "no user with id: " + id})
    else:
        users = [i for i in data if i["id"] != int(id)]
        save_users(users)
        return json.dumps(users)

def save_users(data):
    with open("data.json", "w") as f:
        f.write(json.dumps(data))