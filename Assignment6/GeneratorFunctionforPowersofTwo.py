#This assignment will allow you to practice writing
#Python Generator functions and a small GUI using tkinter

#Title: Generator Function of Powers of Two
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Nov 14, 2020

#Powers of two is a gen function that can take multiple parameters, 1 or 2, gives error for anything else
def powers_of_twos(*args):
    number_of_parameters = len(args)
    if(number_of_parameters == 1):
        starting_pow = 1
        num_of_pow = args[0]
    elif(number_of_parameters == 2):
        starting_pow = args[0]
        num_of_pow = args[1]
    else:
        raise TypeError("Expected either one or two parameters")

    for i in range(num_of_pow):
        yield 2 ** starting_pow
        starting_pow += 1
        
#main function for testing
def main():
    print("Printing the powers of two that yield from powers_of_two(5):")
    single_example = powers_of_twos(5)
    for powers in powers_of_twos(5):
        print(powers)

    print("\nPrinting the powers of two that yield from powers_of_two(3,5):")
    for powers in powers_of_twos(3,5):
        print(powers)

    #print("\n Showing error by typing powers_of_twos(1,2,3)")
    #for powers in powers_of_twos(1,2,3):
    #    print(powers)

    print("\n Showing error by typing powers_of_twos(0)")
    for powers in powers_of_twos():
        print(powers)
    
if __name__ == '__main__':
    main()

