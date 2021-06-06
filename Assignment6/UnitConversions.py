#This assignment will allow you to practice writing
#Python Generator functions and a small GUI using tkinter

#Title: Unit conversion GUI
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Nov 14, 2020

#Importing tkinter
from tkinter import *

class ConversionGUI():

    #The following functions change the label to the unit that is chosen
    def unit_is_inches(self):
        self.unit_label.config(text="inch")
    def unit_is_cm(self):
        self.unit_label.config(text="cm")
    def unit_is_feet(self):
        self.unit_label.config(text="ft")
    def unit_is_meter(self):
        self.unit_label.config(text="m")

    #Function converts to unit to inches
    def convert_to_inches(self):
        #Using the selected unit, this function converts that unit to inches

        self.text_box.config(state='normal')
        self.text_box.delete("1.0", END)
        self.text_box.config(state='disabled')
        
        unit = self.unit_label.cget("text")
        
        if self.text_entry.get():
            try:
                entry = float(self.text_entry.get())

                #Inches to inches
                if(unit == "inch"):
                    self.text_box.config(state='normal')

                    conversion = entry
                    self.text_box.insert(END, "{:} inches".format(conversion))
                    self.text_box.config(state='disabled')

                #Centimeters to inches
                elif(unit == "cm"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.393701
                    self.text_box.insert(END, "{:} inches".format(conversion))
                    self.text_box.config(state='disabled')

                #Feet to inches                 
                elif(unit == "ft"):
                    self.text_box.config(state='normal')

                    conversion = entry * 12
                    self.text_box.insert(END, "{:} inches".format(conversion))
                    self.text_box.config(state='disabled')

                #Meter to inches
                elif(unit == "m"):
                    self.text_box.config(state='normal')

                    conversion = entry * 39.3701
                    self.text_box.insert(END, "{:} inches".format(conversion))
                    self.text_box.config(state='disabled')
                    
            except ValueError:
                self.text_box.config(state='normal')
                self.text_box.insert(END, "Error: You must enter a number!")
                self.text_box.config(state='disabled')

    #Function converts to unit to feet
    def convert_to_feet(self):
        #Using the selected unit, this function converts that unit to feet

        self.text_box.config(state='normal')
        self.text_box.delete("1.0", END)
        self.text_box.config(state='disabled')
        
        unit = self.unit_label.cget("text")
        
        if self.text_entry.get():
            try:
                entry = float(self.text_entry.get())

                #Inches to feet
                if(unit == "inch"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.0833333
                    self.text_box.insert(END, "{:} feet".format(conversion))
                    self.text_box.config(state='disabled')

                #Centimeters to feet
                elif(unit == "cm"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.0328084
                    self.text_box.insert(END, "{:} feet".format(conversion))
                    self.text_box.config(state='disabled')

                #Feet to feet               
                elif(unit == "ft"):
                    self.text_box.config(state='normal')

                    conversion = entry
                    self.text_box.insert(END, "{:} feet".format(conversion))
                    self.text_box.config(state='disabled')

                #Meter to feet
                elif(unit == "m"):
                    self.text_box.config(state='normal')

                    conversion = entry * 3.28084
                    self.text_box.insert(END, "{:} feet".format(conversion))
                    self.text_box.config(state='disabled')
                    
            except ValueError:
                self.text_box.config(state='normal')
                self.text_box.insert(END, "Error: You must enter a number!")
                self.text_box.config(state='disabled')

    #Function converts to unit to centimeters
    def convert_to_cm(self):
        #Using the selected unit, this function converts that unit to centimeters

        self.text_box.config(state='normal')
        self.text_box.delete("1.0", END)
        self.text_box.config(state='disabled')
        
        unit = self.unit_label.cget("text")
        
        if self.text_entry.get():
            try:
                entry = float(self.text_entry.get())

                #Inches to centimeter
                if(unit == "inch"):
                    self.text_box.config(state='normal')

                    conversion = entry * 2.54
                    self.text_box.insert(END, "{:} centimeters".format(conversion))
                    self.text_box.config(state='disabled')

                #Centimeters to centimeter
                elif(unit == "cm"):
                    self.text_box.config(state='normal')

                    conversion = entry
                    self.text_box.insert(END, "{:} centimeters".format(conversion))
                    self.text_box.config(state='disabled')

                #Feet to centimeter                 
                elif(unit == "ft"):
                    self.text_box.config(state='normal')

                    conversion = entry * 30.48
                    self.text_box.insert(END, "{:} centimeters".format(conversion))
                    self.text_box.config(state='disabled')

                #Meter to centimeter
                elif(unit == "m"):
                    self.text_box.config(state='normal')

                    conversion = entry * 100
                    self.text_box.insert(END, "{:} centimeters".format(conversion))
                    self.text_box.config(state='disabled')
                    
            except ValueError:
                self.text_box.config(state='normal')
                self.text_box.insert(END, "Error: You must enter a number!")
                self.text_box.config(state='disabled')

    #Function converts from unit to meters
    def convert_to_meter(self):
        #Using the selected unit, this function converts that unit to meters

        self.text_box.config(state='normal')
        self.text_box.delete("1.0", END)
        self.text_box.config(state='disabled')
        
        unit = self.unit_label.cget("text")
        
        if self.text_entry.get():
            try:
                entry = float(self.text_entry.get())

                #Inches to meters
                if(unit == "inch"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.0254
                    self.text_box.insert(END, "{:} meters".format(conversion))
                    self.text_box.config(state='disabled')

                #Centimeters to meters
                elif(unit == "cm"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.01
                    self.text_box.insert(END, "{:} meters".format(conversion))
                    self.text_box.config(state='disabled')

                #Feet to meters                 
                elif(unit == "ft"):
                    self.text_box.config(state='normal')

                    conversion = entry * 0.3048
                    self.text_box.insert(END, "{:} meters".format(conversion))
                    self.text_box.config(state='disabled')

                #Meter to meters
                elif(unit == "m"):
                    self.text_box.config(state='normal')

                    conversion = entry
                    self.text_box.insert(END, "{:} meters".format(conversion))
                    self.text_box.config(state='disabled')
                    
            except ValueError:
                self.text_box.config(state='normal')
                self.text_box.insert(END, "Error: You must enter a number!")
                self.text_box.config(state='disabled')

    #__init__ method
    def __init__(self):

        #Set up window, give title, cannot resize
        root = Tk()
        root.geometry("350x400")
        root.title("Unit Conversions GUI")
        root.resizable(False, False)

        #Title row
        frame0 = Frame(root)
        self.title_label = Label(frame0, text="Unit Conversions", font=("Ariel",25)).pack()
        self.explain_label = Label(frame0, text="\nThis is the Unit Conversions GUI.\nType in the float number of the unit you want to convert,\nthen press one of the unit buttons \nto show what unit you are converting from,\nfinally, select what unit you would like to convert to").pack()
        frame0.pack()

        #Line row
        frame_line1 = Frame(root)
        self.line = Label(frame_line1, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n").pack()
        frame_line1.pack()

        #Unit row
        frame1 = Frame(root)
        
        self.text_entry = Entry(frame1)
        self.text_entry.pack(side=LEFT)

        self.unit_label = Label(frame1, text="?")
        self.unit_label.pack(side=LEFT)

        frame1.pack()

        #Button Row
        frame2 = Frame(root)
        self.choose_label = Label(frame2, text="My Unit: ").pack(side=LEFT)
        self.inch_button = Button(frame2, text="Inches", command=self.unit_is_inches).pack(side=LEFT)
        self.feet_button = Button(frame2, text="Feet", command=self.unit_is_feet).pack(side=LEFT)
        self.cm_button = Button(frame2, text="Centimeter", command=self.unit_is_cm).pack(side=LEFT)
        self.meter_button = Button(frame2, text="Meters", command=self.unit_is_meter).pack(side=LEFT)

        frame2.pack()

        #Line Frame
        frame_line2 = Frame(root)
        self.line = Label(frame_line2, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nI will convert to:\n").pack()
        frame_line2.pack()

        #Convert buttons
        frame4 = Frame(root)
        self.toinch_button = Button(frame4, text="Inches", command=self.convert_to_inches).pack(side=LEFT)
        self.tofeet_button = Button(frame4, text="Feet", command=self.convert_to_feet).pack(side=LEFT)
        self.tocm_button = Button(frame4, text="Centimeters", command=self.convert_to_cm).pack(side=LEFT)
        self.tometer_button = Button(frame4, text="Meters", command=self.convert_to_meter).pack(side=LEFT)
        frame4.pack()

        #Text box row
        frame5 = Frame(root)
        self.text_box = Text(state=DISABLED)
        self.text_box.pack()
        frame5.pack()

        #Start the event loop
        root.mainloop()

#Instantiate Conversion GUI, which will also start the event loop
my_gui = ConversionGUI()
