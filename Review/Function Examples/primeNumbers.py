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
        sum = sum + (i * i)
    return sum

def main():
    myList = putPrimeNumbersIntoList(10)
    print("myList= ")
    print(myList)

    squared_sum = sumSquaredList(myList)
    print("sumSquaredLists = ")
    print(squared_sum)
    

if __name__ == "__main__":
    main()