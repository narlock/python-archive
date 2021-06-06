#This assignment will allow you to practice writing programs
#That use lists in Python

#Title: Password Validator
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Oct 1, 2020

#Function check_password validates the given password parameter
#returns True if the password is valid, False if not
def check_password(password, username):
    #Lists to store common passwords and symbol marks, invalid and valid
    banned_symbols = ['#','^','&','(',')','-','+','_','+','[',']','\'','\"','\\','`','~','{','}','<','>','/','?','|']
    common_passwords = ['password','1234','111111','Qwerty123','Abcd99','football','dragon','letmein','iloveyou','admin','login','welcome','flower','zaq1','Password1']
    correct_punct = ['!','+','.','@','$','%','*']
    success = True

    #Check if the password is identical to the username or username spelt backwards
    if(password.lower() == username.lower() or password.lower() == username [::-1].lower()):
        print("Password cannot contain a variation of the username")
        success = False

    #Check if password is a common password
    for i in common_passwords:
        if(i == password):
            print("Don't use common passwords")
            success = False

    #Check if the password contains an unrecognized character
    if any(char in banned_symbols for char in password):
        print("Password contains an invalid character")
        success = False

    #Check if the password is too short
    if(len(password) < 8):
        print("Password is too short, must be at least 8")
        success = False

    #Check if the password is too large
    if(len(password) > 20):
        print("Password is too large, must be at most 20")
        success = False

    #Check if the password contains an upper-case char
    if not any(char.isupper() for char in password):
        print("Password must contain at least one UPPERCASE letter")
        success = False

    #Check if the password contains a lower-case char
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter")
        success = False

    #Check if the password contains a digit 0-9
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit 0-9")
        success = False

    #Check if the password contains at least one of the punct marks respectively
    if not any(char in correct_punct for char in password):
        print("Password must contain at least one punctuation mark (!+.@$%*)")
        success = False

    #Returns success/failure
    return success
            
#Main function
def main():
    #Prompts user for username and password
    username = input("Enter a username:")
    password = input("Enter a password:")

    #Checks if the password is valid, if not, user must re-enter a password
    while(check_password(password, username) != True):
        password = input("Please re-enter password:")

    #After password is validated, good password
    print("Good password!")

#Driver
if __name__ == '__main__':
    main()
