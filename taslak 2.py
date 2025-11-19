# first-project_1
#cse101 lab project_1 DİĞDEM EDİNÇ 
print("Hello, we are please to welcome you in our regional credit union's pilot core-banking platform!")
#main.py– menu loop and program bootstrap.
isLoginScreen = True
users = {} 
while isLoginScreen:
    print("""
Choose for continue the system:
    Enter 1 to login. 
    Enter 2 to register.
    Enter 3 to exit system.
""")
    menu = input("ENTER: ")
    if menu =="1" :
        username= input("Username: ")
        password= input("Password: ")
        if username not in users :
            print("You have not registered before. Try to register.")
            continue
        elif username in users and users[username] != password :
            print("Password is incorrect.")
            continue
        else:
            print("Login successful!")
            isLoginScreen = False
    elif menu== "2":
        username = input("Create a username: ")
        password = input("Create a password: ")
        if username in users :
            print("You have already registered before, go back to menu and login or this username has been choosen by other users.")
            continue
        else:
            users[username] = password
            print("Registration successful!")
    elif menu == "3" :
        print("Exiting system.")
        break
    else:
        print("Invalid choice!Enter 1 ,2 or 3.")
        continue








