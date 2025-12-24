#main.py / admin.py

def admin_dashboard(users : dict) -> None: 
    print (f"""Admin Dashboard
           Total Users: {len(users)}""")
    total_balance = 0
    for user in users.values():
        total_balance += user["balance"]
    print(f"Total Bank Balance: {total_balance:.2f}")

def view_all_users(users : dict) -> None:
    for username , user in users.items():
        print(f"""User name : {username}
Balance : {user['balance']:.2f}""")
def audit_log(event : str , meta : dict) -> None :
    time = date.time.now().isformat()
    print(f"[{time}] EVENT: {event} | META: {meta}")
def update_interest_rate(config : dict , new_rate : float) -> dict :
    if new_rate < 0 :
        print("Interest rate cannot be negative.")
        return config
    config["interest_rate"] = new_rate
    print(f"Interest applied. New interest rate: {new_rate}%")
    return config
def deactivate_user(users : dict , username : str) -> bool :
    if username not in users :
        print(f"User {username} not found.")
        return False
    users[username]["active"] = False 
    print(f"User {username} has been deactivated.")
    return True

