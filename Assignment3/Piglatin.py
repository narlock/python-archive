#This assignment will allow you to practice writing programs
#That use lists in Python

#Title: Pig Latin Translator
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Oct 1, 2020


#listToString is a function that converts a list to a string
#In this case, we will be converting a list of 'words' to a sentence, captializing the first letter.
def listToString(words):
    sentence = ""
    words[0] = words[0].capitalize()
    for i in words:
        sentence += i + ' '
            
    return sentence

#Main function
def main():
    #Constant lists representing their title respectively
    CONSONANT = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    VOWEL = ['a','e','i','o','u']
    PUNCT = ['.','!','?',',',';']
    AY = 'ay'
    WAY = 'way'

    #Prompts the user to type a sentence
    print("Type a sentence and this program will re-write it in Pig Latin")
    sentence = str(input("Type sentence:"))
    pl_words = []

    #Splits the sentence into words (list)
    words = sentence.split()

    #Determines if the word has a consonant or vowel for it's first letter
    #Then translates the word to the "Pig Latin" equivalent
    for i in range(len(words)):
        
        first_letter = words[i][0]
        first_letter = str(first_letter)
        first_letter = first_letter.lower()
            
        if first_letter in CONSONANT:
            pl_words.append(words[i][1:len(words[i])] + first_letter + AY)
        elif first_letter in VOWEL:
            pl_words.append(words[i] + WAY)

    #Determines if the word has a punctuation marking in it, if so
    #If true, the punctuation mark will move to the end of the word
    for i in range(len(pl_words)):
        punctuation = ''
        word_length = len(pl_words[i])
        
        for j in range(word_length):
            if pl_words[i][j] in PUNCT:
                punctuation = pl_words[i][j]


        pl_words[i] = pl_words[i].replace(punctuation,'')
        pl_words[i] += punctuation
                
    #After the words have been translated, the listToString function is called,
    #Which creates the new sentence in Pig Latin
    pl_sentence = listToString(pl_words)
    print(pl_sentence)
            

#Driver
if __name__ == '__main__':
    main()
