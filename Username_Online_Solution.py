users = {}
status = ""

def displayMenu():
    status = raw_input("Are you a registered user? y/n? Press q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser():
    createLogin = raw_input("Create login name: ")

    if createLogin in users: # check if login name exists
        print "\nLogin name already exist!\n"
    else:
        createPassw = raw_input("Create password: ")
        users[createLogin] = createPassw # add login and password
        print("\nUser created!\n")     

def oldUser():
    login = raw_input("Enter login name: ")
    passw = raw_input("Enter password: ")

    # check if user exists and login matches password
    if login in users and users[login] == passw: 
        print "\nLogin successful!\n"
    else:
        print "\nUser doesn't exist or wrong password!\n"

while status != "q":            
    displayMenu()
