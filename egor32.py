from turtle import *
from random import randint

#первый дом
def cube(x,y, border_color, colour, h, v):
    penup()
    goto(x,y)
    pendown()
    color(border_color, colour)
    begin_fill()
    for i in range(2):
        forward(h)
        left(90)
        forward(v)
        left(90)
    end_fill()

#солнце
def day():
    penup()
    goto(330,350)
    pendown()
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(80)
        left(100)
    end_fill()




speed(100)

cube(-400,-100, 'blue', 'blue', 1000,1000)
cube(-400,-1100, 'green', 'green', 1000,1000)

cube(-300,-200, 'black', 'pink', 90, 200)

x = -295
y = -30

#первый дом
for i in range(5):
    for i in range(3):
        cube(x, y, 'black', 'blue', 20, 20)
        x += 30
    x -= 90
    y -= 30

cube(-265,-200, 'black', 'black', 20, 40)
cube(-275,0, 'black', 'green', 40, 15)
cube(-270,15, 'black', 'green', 30, 15)

pensize(5)
cube(-255,30, 'black', 'black', 1, 60)
pensize(1)


x = -210
y = -200
#второй дом
for i in range(9):
    cube(x,y, 'black', 'white', 60, 20)
    y += 20


#третий дом
x = -150
y = -200
for i in range(5):
    cube(x,y, 'black', 'orange', 20, 80)
    x += 20

cube(-150,-120, 'black', 'purple', 100, 20)

cube(-150,-100, 'black', 'pink', 100, 200)

x = -140
y = 70
for i in range(6):
    for i in range(3):
        cube(x, y, 'black', 'blue', 20, 20)
        x += 30
    x -= 90
    y -= 30

color('yellow')
penup()
goto(-150,100)
pendown()
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()



#четвёртый дом
cube(-50,-200, 'white', 'white', 40, 250)

x = -33
y = 0
for i in range(5):
    cube(x,y, 'black', 'yellow', 6, 30)
    y -= 40


#пятый дом
colours = ['DarkOrchid2', 'green', 'yellow', 'pink', 'red', 'DeepPink2']

y = -200
for i in range(18):
    cube(-10,y, 'black', colours[randint(0, len(colours)-1)], 80, 20)

    y += 20

cube(70,-200, 'black', 'yellow', 40, 200)

x = 80
y = -40
for i in range(5):
    for i in range(2):
        cube(x, y, 'black', 'pink', 6, 30)
        x += 16
    x -= 32
    y -= 35
    
#седьмой дом
color('black')
penup()
goto(160,30)
pendown()
begin_fill()
circle(50)
end_fill()
cube(110,-200, 'black', 'grey', 100,280)

y = 50
for i in range(8):
    cube(120,y, 'black', 'blue', 80,20)
    y -= 30

x = 210
y = -100
for i in range(3):
    for i in range(2):
        cube(x,y, 'black', colours[randint(0, len(colours)-1)], 50,50)
        x += 50
    x = 210
    y -= 50

cube(310,-200, 'black', 'pink', 100,200)


y = -60
for i in range(3):
    cube(330,y, 'black', 'blue', 60,40)

    y -= 60

color('green')
penup()
goto(310,0)
pendown()
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()

color('black')
penup()
goto(360,90)
pendown()
pensize(3)
right(80)
for i in range(80):
    forward(2)
    left(1)

penup()
goto(360,90)
pendown()
pensize(3)
left(260)
for i in range(80):
    forward(2)
    right(1)


color('black')
penup()
goto(30,160)
pendown()
left(270)
pensize(5)
forward(40)
right(90)
begin_fill()
circle(5)
end_fill()

pensize(1)

day()

hideturtle()
exitonclick()
