# Run the script by opening the terminal: $ python3 main.py

# Procedural Programming - where everything is usually in a single script/file (functions/procedures - top to bottom)
# One of the earliest programming paradigms is Procedural Programming
# Object Oriented Programming (OOP) - split tasks/code into smaller pieces
# Modal real-world objects

# Class - is a "blueprint", a template, that allows objects to be generated from it.

# Attributes - these are the variables of an object
# Methods - these are the functions of an object

# The car is the object that gets created from the class
# The CarBluePrint() is the class
# This uses PascalCase (each word starts with an uppercase letter)

# car = CarBlueprint()

# The Turtle Graphic library comes with every version of Python
# Here, we are using a class (blueprint) that comes from another module created by someone else

# import turtle

# To tap into the turtle class defined inside of the turtle module
# import turtle 

# We could use:
# from turtle import Turtle
# Using the Screen class allows us to use the window where the turtle will show
# from turtle import Turtle, Screen

# Get the Turtle() class (blueprint) from inside the turtle module and save into our own object named timmy
# This is using PascalCase here
# Use this is we use: import turtle
# timmy = turtle.Turtle()

# timmy = Turtle()

# Accessing attributes (variables):
# car.speed
# timmy.speed

# my_screen = Screen()
# print(my_screen.canvheight)    # Canvas height

import os
import tkinter as tk
from turtle import Turtle, Screen

# Suppress the deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Print Tk version
print(tk.TkVersion)

# Alternatively, for Tcl version
print(tk.Tcl().eval('info patchlevel'))

# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter and Turtle Example")

# Create a Canvas widget to draw with turtle
canvas = tk.Canvas(master=root, width=500, height=500)
canvas.pack()

# Create a turtle screen and associate it with the Tkinter canvas
screen = Screen()
print(screen)
screen._root = root
screen.cv = canvas
screen.screensize(500, 500)

# Create a turtle named timmy
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# Move the turtle around
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

# Keep the window open
root.mainloop()

