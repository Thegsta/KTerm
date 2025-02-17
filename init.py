from settings import user_settings_kterm

import getpass
import time
import os

setbold = '\033[1m'
endbold = '\033[0m'

loged_user = ""

def login():
    global loged_user
    username = input("Username: ")
    for user in user_settings_kterm:
        if user['username'] == username:
            password = getpass.getpass("Password: ")
            if user['password'] == password:
                loged_user = user['username']
                start_up()
                return
            elif user['password'] == password.strip("/s"):
                loged_user = user['username']
                os.system('cls||clear')
                main()
                return
            else:
                print("Wrong Password")
                return login()
    print("Wrong Username")
    return login()

def main():
    print(f"Running {setbold}KTerm{endbold}; Version 0.0.1")
    print(f"Hello {setbold}{loged_user}{endbold}")
    command()

def command():
    user = input("> ")
    if user == "exit":
        user = input("Are you sure? (Y/N) ").upper()
        if user == "Y":
            os.system('cls||clear')
            os._exit(0)
        elif user == "N":
            command()
        else:
            print("Command not found")
            command()
    elif user == "credits":
        print(f"Made and published by {setbold}Thegsta{endbold}")
        print(f"and {setbold}TheAxoltolLord{endbold} helped with some code")
        command()
    elif user == "clear":
        os.system('cls||clear')
        command()
    elif user == "logout":    
            login()
    else:
        print("Command not found")
        command()

def start_up():
    time.sleep(1)
    for i in range(4):
        print("Loading.")
        time.sleep(.5)
        os.system('cls||clear')
        print("Loading..")
        time.sleep(.5)
        os.system('cls||clear')
        print("Loading...")
        time.sleep(.5)
        os.system('cls||clear')
    main()

login()