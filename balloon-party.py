# Name: Masooma Fatima
# NSID: mbq567
# Student number: 11438127
# Course: CMPT 140
# Instructor Name: Sandra Kumi

import turtle
import random

initial_size = 30
inflate_amount = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'

balloons = []

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Cookie Monster's Ballon Party")
screen.bgcolor('white')
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def make_balloon(x, y):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return {'x': x, 'y': y, 'color': (r, g, b), 'size': initial_size}

def draw_balloon(balloon, label):
    size = balloon['size']
    x = balloon['x']
    y = balloon['y']
    color = balloon['color']
    
    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    
    pen.penup()
    pen.goto(x, y - size // 2)
    pen.color('white')
    pen.write(label, align='center', font=('Garamond', max(8, size // 2), 'bold'))
    
def draw_all():
    pen.clear()
    for i, balloon in enumerate(balloons):
        draw_balloon(balloon, alphabet[i])
    screen.update()
    
def mouse_click(x,y):
    if len(balloons) < 26:
        balloons.append(make_balloon(x, y))
        draw_all()
        
def pop_balloon():
    if len(balloons) > 0:
        balloons.pop()
        draw_all()
    
def make_inflate_handler(letter):
    def handler():
        index = alphabet.index(letter)
        if index < len(balloons):
            balloons[index]['size'] += inflate_amount
            draw_all()
    return handler

screen.colormode(255)
screen.onclick(mouse_click)
screen.onkey(pop_balloon, 'space')

for letter in alphabet:
    screen.onkey(make_inflate_handler(letter), letter)
    
screen.listen()
draw_all()
screen.mainloop()

