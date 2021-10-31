def printPrimeNumbers(input):
    for number in range(1,input + 1):
        if number >= 1:
            for i in range(2,number):
                if (number % i) == 0:
                    break
            else:
                print(number)

def putPrimeNumbersIntoList(input):
    list = []
    for number in range(1,input + 1):
        if number >= 1:
            for i in range(2,number):
                if (number % i) == 0:
                    break
            else:
                list.append(number)
    return list

def sumSquaredList(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + (list[i] * list[i])
    return sum

def jamMan():
    loopCondition = True

    while(loopCondition):
        lower = 1
        #1 Asks user to input a number N
        upper = int(input("hello good sir, can you do me a favour and enter any random number here?: "))
        inputUpper = upper
        #2 All prime numbers 1 through N are printed
        for number in range(lower,upper + 1):
            if number >= 1:
                for i in range(2,number):
                    if (number % i) == 0:
                        break
                else:
                    print(number)
        #3 The sum of the square of all prime numbers 1 through N is computed and printed
        squared_sum = 0
        for number in range(lower,inputUpper + 1):
            if number >= 1:
                for i in range(2,number):
                    if (number % i) == 0:
                        break
                else:
                    squared_sum = squared_sum + (number * number)
        print(squared_sum)

        #4 The user is asked if they want to compute a new sum of squared numbers, if so, continue
        continueCondition = input("Want to compute a new sum of squared? ")
        if(continueCondition == "no"):
            loopCondition = False
    

def main():
    """
    myList = putPrimeNumbersIntoList(10)
    print("myList= ")
    print(myList)

    squared_sum = sumSquaredList(myList)
    print("sumSquaredLists = ")
    print(squared_sum)
    """

    jamMan()
    

if __name__ == "__main__":
    main()