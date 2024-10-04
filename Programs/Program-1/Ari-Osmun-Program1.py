# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Flag Designer
# Author: Daniel DeFrance
# (c) Copyright Daniel DeFrance and Montana State University
# You may modify this code and use it for class
# You may NOT publish this code to any website
# ---------------------------------------
# Assignment: Modify this program as described in D2L
# ---------------------------------------
#
# Modified by: <your full name>, <date>
#
# ---------------------------------------

import turtle

width = 800
height = 500
turtle.setup(width, height)
wn = turtle.Screen()
wn.bgcolor("lightgray")

draw_color = "gray"
color_1, color_2, color_3 = draw_color, draw_color, draw_color
section = turtle.Turtle()
section.color(draw_color, "lightgray")
section.shapesize(2)
section.speed(0)
section.penup()

message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(-100, -150)
message.color("gray")
message.speed(0)
message.write("Click anywhere to begin designing a flag.", font = ("Arial", 12))

def draw_section():
    section.begin_fill()
    section.pendown()
    for i in range(2):
        section.forward(100)
        section.right(90)
        section.forward(200)
        section.right(90)
    section.end_fill()
    section.penup()
    section.goto(-250, 0)

def draw_first():
    section.goto(-150,100)
    draw_section()

def draw_second():
    section.goto(-50,100)
    draw_section()

def draw_third():
    section.goto(50,100)
    draw_section()

def cycle_color(current_color):
    if current_color == "yellow" or current_color == "gray" :
        new_color = "white"
    elif current_color == "white":
        new_color = "blue"
    elif current_color == "blue":
        new_color = "red"
    elif current_color == "red":
        new_color = "green"
    elif current_color == "green":
        new_color = "yellow"
        
    else:
        # (note: we shouldn't ever get here...)
        print("There seems to be a mistake with the color cycling.")
        new_color = "gray"
        
    return new_color

def color_flag(x, y):

    # Whenever we try to change a variable defined outside the function,
    # we need to use the global keyword to let Python know it's on purpose.
    global draw_color, color_1, color_2, color_3

    # This print statment will tell us where on the screen the user clicked.
    print("x: ", x, "y: ", y)

    if (-150 < x < -50) and (100 > y > -100):
        draw_first()
        color_1 = draw_color
    elif (-50 < x < 50) and (100 > y > -100):
        draw_second()
        color_2 = draw_color
    elif (50 < x < 150) and (100 > y > -100):
        draw_third()
        color_3 = draw_color
    else:
        draw_color = cycle_color(draw_color) 
        section.color(draw_color)
        
    check_flag(color_1, color_2, color_3)

# function to clear the previous message by drawing a box over it
def erase_message():
    message_color = "lightgray"
    message.fillcolor(message_color)
    message.begin_fill()
    message.goto(-300, -120)
    for i in range(2):
        message.forward(600)
        message.right(90)
        message.forward(40)
        message.right(90)
    #TODO: draw a 600 wide by 40 pixel high box here
    message.end_fill()
    message.goto(-100, -150)

def check_flag(one, two, three):
    
    print("left: " + one + ", center: " + two + ", right: " + three)
    erase_message()
    if(one == "blue" and two == "white" and three=="red"): #Goes through each color and checks
        message.write("National Flag of France", font = ("Arial", 20))
    elif(one == "green" and two == "white" and three=="red"):
        message.write("National Flag of Italy", font = ("Arial", 20))
    elif(one == "red" and two == "white" and three=="red"):
        message.write("National Flag of Peru", font = ("Arial", 20))
    elif(one == "green" and two == "white" and three=="green"):
        message.write("National Flag of Nigeria", font = ("Arial", 20))
    elif(one == "blue" and two == "yellow" and three=="red"):
        message.write("National Flag of Romania", font = ("Arial", 20))
    elif(one == "green" and two == "yellow" and three=="red"):
        message.write("National Flag of Mali", font = ("Arial", 20))
    elif(one == "gray" or two == "gray" or three == "gray"):
        message.write("Color all three sections.", font = ("Arial", 20))
    else:
        message.write("The design is available!", font = ("Arial", 20))

        # FRANCE: Blue, White, Red
        # ITALY: Green, White, Red
        # PERU: Red, White, Red
        # NIGERIA: Green, White, Green
        # ROMANIA: Blue, Yellow, Red
        # MALI: Green, Yellow, Red
    # ...otherwise, display a message that the design is available.
    
    # if any of the three sections are gray, prompt the user to color them
   
draw_first()
draw_second()
draw_third()

wn.onclick(color_flag)


    
    
