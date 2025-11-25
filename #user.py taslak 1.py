#user.py taslak 1
import json
import os
os.path.exists("users.json") 
def load_users_from_file(path : str) -> dict:
    import json
    try:
        with open(path) as f :
            users = json.load(f)
            return users
    except FileNotFoundError:
        return {}       
def save_users_to_file(users : dict, path : str) -> None:
    with open (path, "w") as f:
        json.dump(users, f)
users = load_users_from_file("users.json")
def register_user(users: dict, profile: dict) -> dict:
    username = profile["username"]
    password = profile["password"]
    if username in users :
        print("Username already exists. Try a different username.")
        return users
    else:
        users[username] = password
        save_users_to_file(users, "users.json")
        return users
def login_user(users: dict, username: str, password: str) -> dict | None:
    user = users.get(username)
    if not user:
        return None
    return user if user["password"] == password 
    else:
    None



