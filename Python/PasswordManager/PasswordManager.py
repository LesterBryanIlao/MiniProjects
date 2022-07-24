pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Enter Account Name: ")
    password = input("Passwowrd: ")
while True:
    mode = input("Do you want to Add Password [Add] or View Password [View]? Press 'Q' to quit. ").strip().title()
    
    if mode == "Q":
        print("Quitting session.")
        break 
    
    if mode == "Add":
        break
    elif mode == "View":
        break

    else: 
        print("Invalide mode.", end=" ")
        continue