#report.py
import os
from datetime import datetime

def view_transaction_history(user: dict, limit: int = 10) -> list:
    transactions = user.get("transactions", [])
    return transactions[-limit:]


def export_transaction_history(user: dict , directory: str) -> str:
    if not os.path.exits(directory):
        os.makedirs(directory)
    file_name = f"{user['username']}_transactions.txt"
    file_path = os.path.join(directory, file_name)
    with open (file_path , "w") as f:
        for t in user.get("transactions", []):
            f.write(f"{t['date']} | {t['type']} | {t['amount']} | {t['balance']}\n")
            return file_path
        

def generate_summary_report(users: dict , limit: int = 10) -> list:
    total_users = len(users)
    total_balance = 0
    for user in users.values():
        total_balance += user["balance"]
    return {
        "total_users": total_users,
        "total_balance": total_balance
                }



def total_bank_balance(users : dict) -> float:
    total_bank_balance_variable = 0.0
    for user in users.values():
        total_bank_balance_variable += user["balance"]
    return total_bank_balance_variable



def list_high_value_customers(users: dict , threshold : float) -> list:
    result = []
    for user in users.values():
        if user["balance"] >= threshold:
            result.append(user["username"])
    return result