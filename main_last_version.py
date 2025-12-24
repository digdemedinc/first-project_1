#main.py 
# last version, compatible with other files
print("Hello, we are pleased to welcome you in our regional credit union's pilot core-banking platform!")
from user import (
    load_users,
    save_users,
    register_user,
    login_user
)
from bank_operations import (
    deposit_money,
    withdraw_money,
    transfer_funds,
    check_balance
)
users_file = "users.json"
users = load_users(users_file)
current_user = None
current_username = None
isLoginScreen = True
while isLoginScreen:
    print("""
Choose to continue the system:
    Enter 1 to login
    Enter 2 to register
    Enter 3 to exit system
""")
    menu = input("Enter your choice: ").split(" ")
    if menu == "1": 
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = login_user(users, username, password)
        if user is not None:
            current_user = user
            current_username = username
            isLoginScreen = False
            print(f"Welcome back, {current_user['username']}!")
        elif menu == "2":
            username = input("Create a username: ")
            password = input("Create a password: ")
            sec_answer = input("Security answer: ")
            profile = {
                "username": username,
                "password": password,
                "security_answer": sec_answer,
                "balance" : 0.0
            }
            user = register_user(users, profile)
            save_users(users_file, users)
        elif menu == "3":
            print("Exiting the system. Hope to see you again!")
            save_users(users_file, users)
            isLoginScreen = False
        else : 
            print("Invalid choice! Enter 1, 2 or 3.")

while current_user is not None:
    print(f"""
Welcome {current_username}

    1. Deposit money
    2. Withdraw money
    3. Transfer money
    4. Check balance
    5. Logout
""")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        deposit_money(current_user, amount)
        save_users(users_file, users)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        withdraw_money(current_user, amount)
        save_users(users_file, users)
    elif choice == "3":
        recipient_username = input("Enter recipient's username: ")
        amount = float(input("Enter amount to transfer: "))
        transfer_funds(users, current_user, recipient_username, amount)
        save_users(users_file, users)
    elif choice == "4":
        check_balance(current_user)
    elif choice == "5":
        print(f"Goodbye, {current_username}!")
        current_user = None
        current_username = None
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")