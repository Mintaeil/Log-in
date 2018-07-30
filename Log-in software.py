import os
import sys
import csv

def Registration_Menu(): 
    choice = input(' If you wish to login enter 1. If you have yet to make an account please enter something else: ')
    if choice != '1':
        User_Registration()
    else:
        login()

def User_Registration():   
    Age = int(input('Age: '))
    Firstname = input('First name: ')
    Surname = input('Surname: ')
    Username = input('Username: ')
    Password = input('Password: ')
    Confirm_password = input('Confirm Password: ')
    if Password != Confirm_password:
        return
    with open('accountdetails.txt', 'r+', newline = '\n') as userfile:  
        for line in userfile:
            if Username in line:
                print('That username is taken!') 
                return
        writes = csv.writer(userfile)   
        writes.writerow([Age, Firstname, Surname, Username, Password])   
        userfile.close()
    print('You will now be directed to login to your new account')
    login()

def login():
    user = input('Username: ')
    password = input('Password: ')
    file = open('accountdetails.txt', 'r')
    confirmation = False
    for i in file:
        details = i.strip().split(',')
        if user == details[3] and password == details[4]:
            confirmation = True  
    if confirmation == True:
        print('Welcome ' + 'user')
    else:
        print('Incorrect or unregistered user information; please try again')
        login()

Registration_Menu()