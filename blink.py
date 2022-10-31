from tkinter import *
import tkinter.font
from gpiozero import LED as red_light
from gpiozero import LED as green_light
from gpiozero import LED as yellow_light

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Red = red_light(14)
YelloW = yellow_light(15)
Green = green_light(18)

win = Tk() #creating a window.
win.title("LED Toggler") #creating  the title of the window.
winFont = tkinter.font.Font(family = 'Cambria', size = 12, weight = "bold") # defining custom font

def RedLedToggle():            

    if Red.is_lit:                       #checks if the red led is on or off 
        Red.off()
        RedLedButton["text"] = "Turn on Red LED"

    else:

        YelloW.off()
        Green.off()
        Red.on()
        RedLedButton["text"] = "Turn on Red LED "


def YellowLedToggle():

    if YelloW.is_lit:              #checks if the yellow led is on or off 

        YelloW.off()
        YellowLedButton["text"] = "Turn on Yellow LED"

    else:

        Red.off()
        Green.off()
        YelloW.on()
        YellowLedButton["text"] = "Turn off Yellow LED "


def GreenLedToggle():

    if Green.is_lit:            #checks if the green led is on or off 

        Green.off()
        GreenLedButton["text"] = "Turn on Green LED"

    else:

        Red.off()
        YelloW.off()
        Green.on()
        GreenLedButton["text"] = "Turn Green LED"

def close():           #it is used to close the GUI function by turning off all the leds and the GPIO cleanup function. This way the application is completely closed

    GPIO.cleanup()
    Red.off()
    YelloW.off()
    Green.off()
    win.destroy()

#creation of radio buttons
RedLedButton = Radiobutton(win, text = 'Turn on Red LED', font  = winFont, command = RedLedToggle, bg = 'red', height = 1, width = 24)  
RedLedButton.grid(row=0, column=1)

YellowLedButton = Radiobutton(win, text = 'Turn on Yellow LED', font  = winFont, command = YellowLedToggle, bg = 'yellow', height = 1, width = 24)  
YellowLedButton.grid(row=1, column=1)

GreenLedButton = Radiobutton(win, text = 'Turn on Green LED', font  = winFont, command = GreenLedToggle, bg = 'green', height = 1, width = 24)  
GreenLedButton.grid(row=2, column=1)

exitButton = Radiobutton(win, text = 'Exit', font  = winFont, command = close, bg = 'bisque2', height = 1, width = 24)  
exitButton.grid(row=3, column=1)

#to swtich off the led lights if the GUI is closed while led is on (if any)
win.protocol("WM_DELETE_WINDOW", close)

#infinite loop which keep the GUI on until the exit button is selected
win.mainloop()