
import csv

file = open("passwords.csv","w")

def info(): 
    file = list(csv.reader(open("passwords.csv"))) #Converts data from csv into a temporary list
    tmp = []
    for x in file:
        tmp.append(x)
    return tmp

def usercreate(tmp): 
    a = True
    while a == True:
        userin = input("Enter a new username: ")      #Ask user for username and checks if the username is in the csv
        lists = False
        row = 0
        for p in tmp:
            if userin in tmp[row][0]:
                print(userin,"has already been allocated.")
                lists = True
            row = row + 1
        if lists == False:
            a = False
        return userin

def createpassword(): 
    signs = ["!","£","$","^","&","*","(",")","?","@","#"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    a = True
    while a == True:
        checksecurity = 0
        ab = False
        cd = False
        ef = False
        gh = False
        enterpassw = input("Enter a password: ")     #Asks user for password 
        passlength = len(enterpassw)
        if passlength >= 8:
            checksecurity = checksecurity + 1
        for i in enterpassw:
            if i.islower():                     
                cd = True
            if i.isupper():                     
                ab = True
            if i in signs:
                ef = True
            if i in numbers:
                gh = True
        if ef == True:        
            checksecurity = checksecurity + 1       # checks if password is strong enough
        if cd == True:
            checksecurity = checksecurity + 1
        if ab == True:
            checksecurity = checksecurity + 1
        if gh == True:
            checksecurity = checksecurity + 1
        if checksecurity == 1 or checksecurity == 2:
            print("This is a weak password, try again.")  #If weak, does not accept the password
            print(createpassword())
                    
        if checksecurity == 3 or checksecurity == 4:
            print("This password could be improved.")
            
            passw_retry = input("Do you want to try for a stronger password? (y/n) ")
            passw_retry.lower()
            
            if passw_retry == "y":
                enterpassw = input("Enter a password: ")     #If strong, but not fully strong, option to enter a stronger password
                passlength = len(enterpassw)
                if passlength >= 8:
                    checksecurity = checksecurity + 1
                for i in enterpassw:
                    if i.islower():
                        cd = True
                    if i.isupper():
                        ab = True
                    if i in signs:
                        ef = True
                    if i in numbers:
                        gh = True
                if ef == True:
                    checksecurity = checksecurity + 1
                if cd == True:
                    checksecurity = checksecurity + 1
                if ab == True:
                    checksecurity = checksecurity + 1
                if gh == True:
                    checksecurity = checksecurity + 1
                if checksecurity == 1 or checksecurity == 2:
                    print("This is a weak password, try again.")
                    print(createpassword())
                if checksecurity == 3 or checksecurity == 4:
                    print("This password could be improved.")
                    passw_retry = input("Do you want to try for a stronger password? (y/n) ")
                    passw_retry.lower()
                    
            if passw_retry == "n":
                a = False
                
        userpass2 = input("Please enter your password a second time: ")    #Asks user to enter password a second time to confirm password
        if userpass2 != userpass2:
            print("Passwords do not match. File not saved")
            main()
        else:
            return enterpassw 

def searchuser(tmp):#Lets user search for username in database before changing password 
    
    tmp = info()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x = x + 1
        
    enteragian = True
    userin = ""
    while enteragian == True:
        usrsearch = input("Enter the username you are looking for ")
        lists = False
        tmp = info()
        x = 0
        for row in tmp:
            if usrsearch in tmp[x][0]:
                enteragian = False
                lists == True
            else:
                print(usrsearch,"is NOT in the list!")

        if lists == True:
            userin = usrsearch
            print(passwordchange())


def passwordchange(userin,tmp): #Allows user to change the password from their login information
    if userin != "":
        enterpassw = createpassword()
        ids = tmp.index(tmp)
        tmp[ids][1] = enterpassw
        file = open("passwords.csv","w")
        x = 0
        for row in tmp:
            new = tmp[x][0] + ", " + tmp[x][1] + "\n"
            file.write(new)
            x = x + 1
            file.close()
    

def displayusers(): #Projects all usernames from database
    tmp = info()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x = x + 1

                    
tmp = info()
a = True   
while a == True:
    print('\n')
    print("1) Create a new Username")   #Main menu where options are provided and executed
    print("2) Change a password")
    print("3) Display all Usernames")
    print("4) Quit")
    print('\n')
    try:
        user_input = int(input("Enter Selection: "))
        if user_input == 1:
            userin = usercreate(tmp)
            passw = createpassword()
            file =  open("passwords.csv","a")
            new = userin + ", " + passw + "\n"
            file.write(str(new))
            file.close()
        elif user_input == 2:
            userin = searchuser(tmp)
            passwordchange(userin,tmp)
        elif user_input == 3:
            displayusers()
        elif user_input == 4:
            print('Have a nice day!')
            a = False
        else:
            print("Incorrect selection")
    except(ValueError):
        print("")

