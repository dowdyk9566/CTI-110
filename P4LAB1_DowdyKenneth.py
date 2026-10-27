import turtle

#Setup the window background and turtle screen
window = turtle.Screen()
window.bgcolor("lightblue") #change background color to light blue

#Setup the turtle object
t = turtle.Turtle()
t.color("purple") #change turtle color to dark green
t.pensize(3)
t.speed(3)

# Draw the square base of the house using a for loop
# A square has 4 equal sides and 90-degree turns
for _ in range(4):
    t.forward(100)
    t.left(90)      

#move the turtle to the top left corner of the square to start drawing the roof
t.left(90)
t.forward(100)
t.right(90)

#Draw the triangle roof using a WHILE loop
#A equalateral triangle has 3 equal sides and 120-degree external turns
sides_drawn= 0
while sides_drawn < 3:
    t.forward(100)
    t.left(120)
    sides_drawn += 1

#Keep window open until user clicks on it
window.exitonclick()