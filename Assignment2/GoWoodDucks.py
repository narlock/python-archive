#This assignment will allow you to practice writing programs
#That use lists in Python

#Title: GoWoodDucks
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Sept 16, 2020

import PPMViewer

WIDTH = PPMViewer.IMG_WIDTH
HEIGHT = PPMViewer.IMG_HEIGHT

#Function that draws the original image of Woody
def draw_original():
    """ Draws the original version of Woody"""
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Function that draws the image of Woody with extreme contrast
def extreme_contrast():
    """ Draws Woody with extreme contrast """
    amount_of_pixels = len(PPMViewer.img) # Sets this to the amount of pixels (tuples)
    for i in range (0, amount_of_pixels):
        x = list (PPMViewer.img[i])       #Gets a tuple, then uses a for loop for RGB values, and changes them
        for j in range(0,3):
            if(x[j] < 127):
               x[j] = 0
            else:
                x[j] = 255
        PPMViewer.img[i] = tuple(x)       #Returns the modified tuple
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Function that draws the image of Woody with greyscale
def greyscale():
    """ Draws Woody with greyscale """
    amount_of_pixels = len(PPMViewer.img) # Sets this to the (tuples)
    for i in range (0, amount_of_pixels):
        x = list (PPMViewer.img[i])       #Gets a tuple, finds the average of the tuple, then sets the values to the average
        average = int((x[0] + x[1] + x[2]) / 3)
        for j in range(0, 3):
            x[j] = average
        PPMViewer.img[i] = tuple(x)       #Returns the modified tuple
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Function that draws the image of Woody inverted
def inverted_rgb():
    """ Draws Woody with inverted colors """
    amount_of_pixels = len(PPMViewer.img) # Sets this to the (tuples)
    for i in range (0, amount_of_pixels): 
        x = list (PPMViewer.img[i])       # Gets the tuple, then inverts the color of each
        for j in range(0, 3):
            x[j] = 255 - x[j]
        PPMViewer.img[i] = tuple(x)       #Returns the modified tuple
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Function that draws the image of Woody flipped vertically
def flipped_vertical():
    """ Draws Woody flipped vertically """
    midpoint_amount_of_pixels = len(PPMViewer.img)/2 # Set this through MIDPOINT!
    for i in range (0, int(midpoint_amount_of_pixels)):
        x = list (PPMViewer.img[i])      #Gets the tuple
        y = list (PPMViewer.img[-(i+1)]) #The opposite side of the tuple
        PPMViewer.img[i] = tuple(y)      #Replaces the tuples with each other
        PPMViewer.img[-(i+1)] = tuple(x)
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Function that draws the top part of Woody on the bottom, and the bottom part of Woody on the top
def top_bottom_swap():
    """ Draws Woody by swapping the top and bottom of the image """
    midpoint_amount_of_pixels = len(PPMViewer.img)/2                #Sets this through MIDPOINT!
    for i in range (0, int(midpoint_amount_of_pixels)):
        x = list (PPMViewer.img[i])                                 #Gets tuple
        y = list (PPMViewer.img[int(midpoint_amount_of_pixels) + i])#Gets the last half of tuple
        PPMViewer.img[i] = tuple(y)                                 #Replaces the top half with bottom half and vice versa
        PPMViewer.img[int(midpoint_amount_of_pixels) + i] = tuple(x)
    PPMViewer.draw_pict(WIDTH, HEIGHT, PPMViewer.img)

#Initial Print and inputs
print("Select an image effect to display a picture of Woody the Woodduck:")
selection = int(input("Enter '1' for draw_original,\n'2' for extreme_contrast,\n'3' for greyscale,\n'4' for inverted_rgb,\n'5' for flipped_vertical, \n'6' for top_bottom_swap\n"))

#Input validation: user must enter an integer between 1 and 6
while(selection <= 0 or selection > 6):
    print("Invalid input, please try again.")
    selection = int(input("Enter '1' for draw_original,\n'2' for extreme_contrast,\n'3' for greyscale,\n'4' for inverted_rgb,\n'5' for flipped_vertical, \n'6' for top_bottom_swap\n"))

#Selection numbers determine which effect will maniuplate the Woody image
if(selection == 1):
    draw_original()
elif(selection == 2):
    extreme_contrast()
elif(selection == 3):
    greyscale()
elif(selection == 4):
    inverted_rgb()
elif(selection == 5):
    flipped_vertical()
elif(selection == 6):
    top_bottom_swap()
