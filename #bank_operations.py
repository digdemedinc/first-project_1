#bank_operations.py
from datetime import datetime
def deposit_money(user: dict, amount: float, channel: str = "branch") -> dict:
    if amount <= 0 :
        print("Amount must be positive to deposit!")
        return user
    user["balance"] += amount
    transaction = {
        "type" : "deposit" ,
        "amount" : amount ,
        "balance_after" : user["balance"] ,
        "date" : datetime.now().isoformat() ,
        "channel" : channel
    }
    user["transaction"].append(transaction)
    print(f"Successfully deposited {amount}. New balance is {user['balance']}.")
    return user

def withdraw_money(user: dict, amount: float, channel: str = "branch") -> dict:
    if amount <= 0 :
        print("Amount must be positive to withdraw!")
        return user
    if amount > user["balance"] :
        print("Not enough balance to withdraw!")
        return user
    user["balance"] -= amount
    transaction = {
        "type" : "withdraw" ,
        "amount" : amount ,
        "balance_after" : user["balance"] ,
        "date" : datetime.now().isoformat() ,
        "channel" : channel
    }
    user["transaction"].append(transaction)
    print(f"Successfully withdrew {amount}. New balance is {user['balance']}.")
    return user


def transfer_funds(users: dict, sender_username: str, receiver_username:str, amount: float) -> tuple[dict, dict]:
    if sender_username not in users or receiver_username not in users:
        print("Sender's or receiver's username does not exist!")
        return None , None
    sender = users[sender_username]
    receiver = users[receiver_username]
    if amount <= 0 :
        print("Amount must be positive to transfer!")
        return sender , receiver
    if amount > sender["balance"] :
        print("Not enough balance to transfer!")
        return sender , receiver
    sender["balance"] -= amount
    receiver["balance"] += amount
    print(f"Successfully transferred {amount} from {sender_username} to {receiver_username}.")
    return sender , receiver

def check_balance(user: dict) -> float:
    return float(user.get("balance", 0.0))


def apply_interest(user: dict, rate: float = 0.015) -> dict:
    import decimal
    rate = decimal(str(rate))