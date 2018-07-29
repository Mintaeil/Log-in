import os
import sys
import cvs

def Registration_Menu():

    choice = input(' If you wish to login enter 1. If you have yet to make an account press enter something else'))

    if choice.lower() == '1' or 'one':
    
        login()
    
    else:
        User_Registration()

def User_Registration():
    
    Age = int(input('Age: '))

    Firstname = input('First name: ')

    Surname = input('Surname: ')

    Username = input('Username: ')

    Password = input('Password: ')

    Confirmpassword = input('Confirm Password: ')

    with open('accountdetails.txt', 'a', '\n') as userfile:
        
        writes = csv.write(userfile)
        
        writes.writerow([Age, Firstname, Surname, Username, Password])
        
        userfile.close()

def login():

    user = input('Username: ')
   
    password = input('Password: ')

    file = open('accountdetails.txt', 'r+')

    confirmation = False

    for line in file:

        details = line.split(', ')

        if user == details[3] and password == details[4]:
    
            confirmation = True
            
    if confirmation = True:
    
        print('Welcome ' + user)
    
    else:
        
        print('Incorrect or unregistered user information; please try again')
        
        login()

Registration_Menu()


