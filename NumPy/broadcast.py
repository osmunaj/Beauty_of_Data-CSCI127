# --------------------------------------
# CSCI 127: Joy and Beauty of Data
# NumPy Computer Graphics "broadcast" example
# --------------------------------------

import turtle
import numpy as np

# --------------------------------------

def draw_house(stylus, coordinates, pen_color):
    stylus.color(pen_color)
    stylus.up()
    stylus.goto(coordinates[0][0], coordinates[0][1])
    stylus.down()
    for coordinate in coordinates:
        stylus.goto(coordinate[0], coordinate[1])

# --------------------------------------

def draw_neighborhood(drawing_turtle):
    drawing_turtle.hideturtle()
    coordinates = np.array([[-30, 50], [-30, -50], [70, -50], [70, 50],
                            [-30, 50], [20, 100], [70, 50]])
    
    draw_house(drawing_turtle, coordinates, "black")
    draw_house(drawing_turtle, coordinates + 10, "black")
    draw_house(drawing_turtle, coordinates + [-100, -200], "red")
    draw_house(drawing_turtle, coordinates * 2, "turquoise")
    draw_house(drawing_turtle, coordinates * [.5, .2] + [100, 200], "blue")


# --------------------------------------

def main():
    window = turtle.Screen()
    house_turtle = turtle.Turtle()
    draw_neighborhood(house_turtle)
    window.exitonclick()

# --------------------------------------

main()
