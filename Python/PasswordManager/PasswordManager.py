pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Enter Account Name: ")
    password = input("Password: ")
    
    with open("password.txt", 'a') as f: # automatically closes files
        f.write(name + "|" + password + "\n") 
    
while True:
    mode = input("Do you want to Add Password [Add] or View Password [View]? Press 'Q' to quit. ").strip().title()
    
    if mode == "Q":
        print("Quitting session.")
        break 
    
    if mode == "Add":
        add()
    elif mode == "View":
        break

    else: 
        print("Invalide mode.", end=" ")
        continue