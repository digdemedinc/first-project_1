#file_manager
from datetime import datetime
from fileinput import filename
import os
import json

def load_data(file_path : str , transactions_path : str) -> tuple[dict , list]:
    users = {}
    transactions = []
    if os.path.exists(file_path):
        with open (file_path , "r") as f :
            users = json.load(f)
    if os.path.exists(transactions_path):
        with open (transactions_path , "r") as f :
            transactions = json.load(f)
    return users , transactions


def save_data(users_path : str , transactions_path : str , users : dict , transactions : list) -> None:
    with open(users_path , "w") as f :
        json.dump(users , f , indent = 4)
    with open (transactions_path , "w") as f :
        json.dump(transactions , f , indent = 4)

def backup_data (source_path : list[str] , backup_dir : str) -> list[str]:
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_files = []
    datetime = datetime
    for path in source_path :
        if os.path.exists(path):
            filename = os.path.basename(path)
            backup_name = f"{timestamp}_{filename}"
            backup_path = os.path.join(backup_dir , backup_name)
            with open (path , "r") as source_file :
                with open (backup_path , "w") as backup_file :
                    backup_file.write(source_file.read())
            backup_files.append(backup_path)
    return backup_files

def validate_storage_schema(users : dict) -> bool :
    for user in users.values():
        if "username" not in user or "balance" not in user:
            return False
        if "transactions" not in user:
            return False    
    return True

def initialize_storage(base_dir) -> dict :
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return {
        "users_path" : os.path.join(base_dir , "users.json"),
        "transactions_path" : os.path.join(base_dir , "transactions.json"),
        "backup_dir" : os.path.join(base_dir , "backups")
    }