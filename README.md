# first-project_1
#cse101 lab project_1 DİĞDEM EDİNÇ 
print("Hello, we are please to welcome you in our regional credit union's pilot core-banking platform!")
#main.py– menu loop and program bootstrap.
users = {} 
while True:
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
    elif menu== "2":
        username = input("Create a username: ")
        password = input("Create a password: ")
        if username in users :
            print("You have already registered before, go back to menu and login or this username has been choosen by other users.")
            continue
        else:
            users.add(username)
            users[username] = password
            print("Registration successful!")
    elif menu == "3" :
        print("Exiting system.")
        break
    else:
        print("Invalid choice!Enter 1 ,2 or 3.")
        continue
#hocam ilk adımı yapmaya calıstım ama elif menu == "2" : kısmından sonra yeni bir username tanımlayıp menuye geri donup login yapınca set'e kaydolmuyor. you havve not registered yazıyo. Saatlerdir bakıyorum ama cozemedim nasıl yapabilirim? bir de powershell de calıstırınca kapanıyor ama visual studio'da gayet çalışıyor.










#user.py – user/account model definitions and authentication helpers.
#bank_operations.py – deposit, withdrawal, transfer, and balance utilities.
#file_manager.py – load/save/backup helpers.
#report.py – analytics and export functionality.



