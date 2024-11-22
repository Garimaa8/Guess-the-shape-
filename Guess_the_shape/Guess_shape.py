import turtle
import random
from PIL import Image

# Set up the screen and turtles
tur = turtle.Turtle()
tur.color('red')
tur.speed(2)
t = turtle.Screen()
t.bgcolor('orange')

tu = turtle.Turtle()
tu.hideturtle()

# Define drawing functions
def rectangle(e):
    tur.fillcolor('black')
    tur.begin_fill()
    tur.forward(e)
    tur.left(360/4)
    tur.forward(e-20)
    tur.left(360/4)
    tur.forward(e)
    tur.left(360/4)
    tur.forward(e-20)
    tur.left(360/4)
    tur.end_fill()

def cube():
    tur.fillcolor('violet')
    tur.begin_fill()
    tur.left(45)
    tur.forward(135)
    tur.right(135)
    tur.forward(120)
    tur.right(45)
    tur.forward(120)
    tur.right(135)
    tur.forward(120)
    tur.end_fill()
    tur.fillcolor('red')
    tur.begin_fill()
    tur.left(45)
    tur.forward(120)
    tur.left(135)
    tur.forward(120)
    tur.left(45)
    tur.forward(120)
    tur.left(135)
    tur.forward(120)
    tur.end_fill()
    tur.fillcolor('green')
    tur.begin_fill()
    tur.left(45)
    tur.forward(120)
    tur.right(90)
    tur.forward(120)
    tur.right(90)
    tur.forward(120)
    tur.right(90)
    tur.forward(120)
    tur.left(135)
    tur.end_fill()

def cuboid():
    tur.fillcolor('blue')
    tur.begin_fill()
    tur.left(45)
    tur.forward(150)
    tur.right(135)
    tur.forward(100)
    tur.right(45)
    tur.forward(150)
    tur.right(135)
    tur.forward(100)
    tur.end_fill()
    tur.fillcolor('green')
    tur.begin_fill()
    tur.left(45)
    tur.forward(100)
    tur.left(135)
    tur.forward(100)
    tur.left(45)
    tur.forward(100)
    tur.left(135)
    tur.forward(100)
    tur.end_fill()
    tur.fillcolor('red')
    tur.begin_fill()
    tur.left(45)
    tur.forward(100)
    tur.right(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(150)
    tur.left(135)
    tur.end_fill()

def rhombus():
    tur.fillcolor('green')
    tur.begin_fill()
    tur.color('green')
    for i in range(3):
        tur.forward(100)
        tur.left(360/3)

    tur.right(360/6)
    tur.forward(100)
    tur.left(360/3)
    tur.forward(100)
    tur.end_fill()

def pyramid():
    tur.fillcolor('red')
    tur.begin_fill()
    tur.forward(100)
    tur.left(45)
    tur.forward(100)
    tur.left(110)
    tur.forward(120)
    tur.left(87)
    tur.forward(135)
    tur.left(117)
    tur.forward(100)
    tur.left(108)
    tur.forward(124)
    tur.right(135)
    tur.end_fill()

def shapes(n):
    r = ['pink', 'violet', 'blue', 'green', 'black']
    clr = random.choice(r)
    tur.fillcolor(clr)
    tur.begin_fill()
    for i in range(n):
        tur.forward(100)
        tur.left(360/n)
    tur.end_fill()

def shapes2(n):
    r = ['violet', 'yellow', 'blue', 'pink', 'black']
    clr = random.choice(r)
    tur.fillcolor(clr)
    for i in range(n):
        tur.color('blue')
        tur.forward(120)
        tur.left(360/n)
    tur.end_fill()

def circle(s):
    tu.fillcolor('violet')
    tu.begin_fill()
    tu.circle(s)
    tu.end_fill()

# Stage 1: Shape Selection Based on Input
n = 0
q = 1

while n != q:
    turtle.reset()
    a1 = input('Enter any alphabet = ')
    a2 = input('Enter any alphabet = ')
    b = ord(a1)
    c = ord(a2)
    
    if b % 10 == 0:
        n = 3
        pyramid()
    
    if b % 10 == 1:
        n = 5
        shapes(5)
    if b % 10 == 2:
        n = 4
        shapes(4)
    if b % 10 == 3:
        n = 8
        shapes(3)
    if b % 10 == 4:
        n = 9
        shapes(9)
    if b % 10 == 5:
        n = 6
        cube()
    if b % 10 == 6:
        n = 10
        cuboid()
    if b % 10 == 7:
        n = 0
        rectangle(150)
    if b % 10 == 8:
        n = 7
        rhombus()
    if b % 10 == 9:
        n = 11
        circle(100)
        
    tur.penup()
    tur.forward(250)
    tur.pendown()

    if c % 10 == 0:
        q = 4
        shapes2(4)
    if c % 10 == 1:
        q = 9
        shapes2(9)
    if c % 10 == 2:
        q = 6
        cube()
    if c % 10 == 3:
        q = 10
        tur.penup()
        tur.forward(200)
        tur.pendown()
        cuboid()
    if c % 10 == 4:
        q = 0
        rectangle(100)
    if c % 10 == 5:
        q = 11
        tu.penup()
        tu.forward(250)
        tu.pendown()
        circle(90)
        tu.clear()
        
    if c % 10 == 6:
        q = 5
        shapes2(5)
    if c % 10 == 7:
        q = 8
        shapes2(3)
    if c % 10 == 8:
        q = 3
        pyramid()
    if c % 10 == 9:
        q = 7
        rhombus()

    if n == q:
        print('Victory - Shapes are the same')
    else:
        tur.reset()
        print('Defeat - Shapes are not the same')

    if n == 11:
        tu.clear()

print('\n')
# Stage 2: Shape Guessing Game

print("STAGE 2")
num = random.randint(0, 9)
print('Which shape is associated with number', num)
Shape = ""
a = ""

# Map number to shape
if num == 0:
    a = "Honeycomb"
    Shape = "Hexagon"
elif num == 1:
    a = "Worship houses in Baha'i"
    Shape = "Nonagon"
elif num == 2:
    a = "Pencil, circus tent"
    Shape = "Pentagon"
elif num == 3:
    a = "Gazing at the sky at night"
    Shape = "Star"
elif num == 4:
    a = "Scale model of Earth"
    Shape = "Sphere"
elif num == 5:
    a = "Stop sign"
    Shape = "Octagon"
elif num == 6:
    a = "Not comfortable mattress"
    Shape = "Cuboid"
elif num == 7:
    a = "Regular candles"
    Shape = "Cylinder"
elif num == 8:
    a = "Oviparous animal"
    Shape = "Oval"
elif num == 9:
    a = "North Atlantic Ocean mystery"
    Shape = "Triangle"

im = Image.open("crown.png")

print(a)
b1 = input("Guess the name of the shape: ")
b1=b1.title()

if b1 == Shape:
    im.show()
    print("Victory", shapes(num))
else:
    print("Oh no, try again!")
    b1 = input("Guess the name of the shape: ")
    if b1 == Shape:
        print("Victory", shapes(num))
    else:
        print("Defeat - The correct shape is", Shape)
