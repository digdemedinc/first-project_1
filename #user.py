#user.py 
import json
from datetime import datetime
def load_users_from_file(path: str) -> dict:
    try :
        with open (path, "r") as file :
            return json.load(file)
    except FileNotFoundError :
        return {}

def save_users_to_file(path: str, users: dict) -> None:
    with open (path, "w") as file :
        json.dump(users, file, indent=4)

def register_user(users: dict, profile: dict) -> dict:
    username = profile["username"]
    if username in users :
        print("Username already exists!")
        return users
    profile["balance"] = profile.get("balance" , 0.0)
    profile["created_at"] = datetime.now().isoformat()
    profile["transactions"] = []
    users[username] = profile
    print("Registeration successful!")
    return users

def login_user(users: dict, username: str, password: str) -> dict | None:
    if username not in users:
        print("Username does not exist!")
        return None
    if users[username]["password"] != password:
        print("Password is wrong, try again !")
        return None
    users[username]["last_login"] = datetime.now().isoformat()
    print("Login successful!")
    return users[username]

def logout_user(active_sessions: dict, username: str) -> None:
    if username in active_sessions:
        del active_sessions[username]
        print("Logout successful!")

def reset_password(users: dict, username: str, secret_answer: str,new_password: str) -> bool:
    if username not in users :
        return False
    if users[username]["security_answer"] != secret_answer :
        return False