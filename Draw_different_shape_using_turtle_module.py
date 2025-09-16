from turtle import Turtle,Screen
import random

my_turtle=Turtle()

screen=Screen()

start_sides=3
end_sides=10
colors = ["red","blue","green","orange","purple","yellow","cyan","magenta","brown","pink"]

# while start_sides <= end_sides:
def draw_shape(num_sides):
        current_color=random.choice(colors)
        my_turtle.color(current_color)
        angle = 360 // num_sides
        for _ in range(num_sides):

            my_turtle.forward(100)
            my_turtle.right(angle)
for num_side in range(start_sides,end_sides):
    draw_shape(num_side)
screen.exitonclick()
