#This assignment will allow you to practice writing programs which
#can read from files to create dictionaries to use in the program.

#Title: State Quiz Program
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Oct 17, 2020

import random

#Function that creates and returns states dictionary with index value
def create_state_dict():
    #Open the text file in read mode
    try:
        file = open("StateList.txt","r")
    except FileNotFoundError:
        print("The file \"Statelist\".txt was not found. Unable to open file.")
    except:
        print("An unexpected error occured. Unable to open file.")

    #Create states dictionary
    state_number = -1
    states = {}
    for line in file:
        x = line.split("|") 
        a = state_number + 1
        b = x[0]
        states[a] = b
        state_number = state_number + 1

    file.close()
    return states

#Function creates and returns statehood_year dictionary
def create_statehood_year_dict():
    #Open the text file in read mode
    try:
        file = open("StateList.txt","r")
    except FileNotFoundError:
        print("The file \"Statelist\".txt was not found. Unable to open file.")
    except:
        print("An unexpected error occured. Unable to open file.")

    #Create statehood year dictionary
    statehood_year = {}
    for line in file:
        x = line.split("|")     #This will split each line,
        a = x[0]                #first element in the file is the "key"
        b = x[2]                #thrid element represents the statehood year
        statehood_year[a] = b

    file.close()
    return statehood_year

#Function creates and returns captial dictionary
def create_captial_dict():
    #Open the text file in read mode
    try:
        file = open("StateList.txt","r")
    except FileNotFoundError:
        print("The file \"Statelist\".txt was not found. Unable to open file.")
    except:
        print("An unexpected error occured. Unable to open file.")

    #Create captial dictionary
    captial = {}
    for lines in file:
        x = lines.split("|")     #This will split each line
        a = x[0]                #First element in the file is the key
        b = x[3]                #Fourth element represents captial
        captial[a] = b

    file.close()
    return captial

#Main function: creates the quiz dictionaries, and enters selection
def main():

    #Runs the functions to create both dictionaries
    states = create_state_dict()
    statehood_year = create_statehood_year_dict()
    captial = create_captial_dict()

    #Program asks the user if they would like to be tested
    #On the captials or year of statehood
    print("Welcome to the State Quiz Program!")
    print("Would you like to be tested on the captials or years of statehood?")

    #Input validation for the quiz
    while True:
        selection = int(input("Enter '1' for captials\nEnter '2' for years of statehood\nI would like to take quiz: "))
        try:
            selection = int(selection)
        except:
            print("Invalid quiz number, try again.")
            continue
        if (selection < 1 or selection > 2):
            print("Invalid quiz number, try again.")
            continue
        break

    #Selection numbers determine which quiz will be executed
    if(selection == 1):
        start_quiz(states, captial, "captial")
    elif(selection == 2):
        start_quiz(states, statehood_year, "year of statehood")

def start_quiz(states, test, quiz_name):
    correct_answers = 0
    incorrect_answers = 0
    question_number = 0
    print("Quiz", quiz_name, "will now begin\n------------------------")

    #Completes a 10 question quiz via for loop, calculating correct and incorrect answers.
    for index in range(0, 10):
        #Choose random state, assigns correct answer
        randomState = random.randint(1,50) - 1
        state_chosen = states[randomState]
        correct_answer = test[state_chosen]

        #Asks the question:
        print("What is the", quiz_name, "of", state_chosen,"?")
        ans = input("My answer is: ")
        
        #Checks if the inputted answer is equal to the correct answer
        if(ans.lower().strip() == test[state_chosen].lower().strip()):
            print("Correct! Next question.")
            correct_answers = correct_answers + 1
        else:
            print("Incorrect. Next question.")
            incorrect_answers = incorrect_answers + 1
        question_number = question_number + 1

    #Final expected output
    print("You answered",correct_answers,"questions correctly")
    print("You answered",incorrect_answers,"questions incorrectly")
    percentage = (correct_answers / question_number) * 100
    print("You scored",percentage,"% on the quiz.")
        

#Driver
if __name__ == '__main__':
    main()
