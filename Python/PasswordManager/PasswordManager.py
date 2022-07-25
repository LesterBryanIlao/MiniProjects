from cryptography.fernet import Fernet

# key generation
'''
def write_key():
    key = Fernet.generate_key()
    
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
# load key
def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

while True:
    master_password = input("What is the master password? ")
    if master_password.strip() == "Lester":
        break
    else:
        print("Wroing master password. Try again.")
        continue

key = load_key() + master_password.encode()
fer = Fernet(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            username, password = line.strip().split("|")
            print(f"Username: {username}, Password: {fer.decrypt(password.encode()).decode()}")

def add():
    name = input("Enter Account Name: ")
    password = input("Password: ")
    
    with open("password.txt", 'a') as f: # automatically closes files
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n") 
    
# input attempts 
while True:
    mode = input("Do you want to Add Password [Add] or View Password [View]? Press 'Q' to quit. ").strip().title()
    
    if mode == "Q":
        print("Quitting session.")
        break 
    
    if mode == "Add":
        add()
    elif mode == "View":
        view()

    else: 
        print("Invalide mode.", end=" ")
        continue