import turtle
import time
import os
import platform
import random


#Set up the screen p2
wn=turtle.Screen()
wn.title("Follower")
wn.bgcolor("blue")
wn.setup(width=600, height=600)




#Player
player=turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0,30)
player.direction="up"

#Boppers
bopper=turtle.Turtle()
bopper.speed(0)
bopper.shape("square")
bopper.color("black")
bopper.penup()
bopper.goto(220,0)

bopper2=turtle.Turtle()
bopper2.speed(0)
bopper2.shape("square")
bopper2.color("black")
bopper2.penup()
bopper2.goto(-220, 0)

bopper3=turtle.Turtle()
bopper3.speed(0)
bopper3.shape("square")
bopper3.color("black")
bopper3.penup()
bopper3.goto(0,220)

bopper4=turtle.Turtle()
bopper4.speed(0)
bopper4.shape("square")
bopper4.color("black")
bopper4.penup()
bopper.goto(0,-220)

#Shields
shield=turtle.Turtle()
shield.speed(0)
shield.shape("triangle")
shield.color("gray")
shield.penup()
shield.goto(0,100)

#Coins
coin=turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.goto(0,1000)



#Enemies
#Boss
boss=turtle.Turtle()
boss.speed(0)
boss.shape("circle")
boss.color("red")
boss.penup()
boss.goto(0,0)
boss.direction="up"

#Boss Fireball
fireball=turtle.Turtle()
fireball.hideturtle()
fireball.speed(1)
fireball.shape("circle")
fireball.color("red")
fireball.penup()


#Spinners
spinner=turtle.Turtle()
spinner.speed(0)
spinner.shape("turtle")
spinner.color("purple")
spinner.penup()
spinner.goto(220,220)

spinner2=turtle.Turtle()
spinner2.speed(0)
spinner2.shape("turtle")
spinner2.color("purple")
spinner2.penup()
spinner2.goto(-220,220)

spinner3=turtle.Turtle()
spinner3.speed(0)
spinner3.shape("turtle")
spinner3.color("purple")
spinner3.penup()
spinner3.goto(220,-220)

spinner4=turtle.Turtle()
spinner4.speed(0)
spinner4.shape("turtle")
spinner4.color("purple")
spinner4.penup()
spinner4.goto(-220,-220)

#Boarder
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("purple")
border_pen.penup()

#MIni fire
fire=turtle.Turtle()
fire.speed(0)
fire.shape("circle")
fire.color("blue")
fire.penup()
fire.goto(0, 0)

#Thunder wave
wave=turtle.Turtle()
wave.speed(0)
wave.shape("line")
wave.




#Keyboard Bindings defining
def go_up():
	if player.direction=="up":
		y=player.ycor()
		player.sety(y + 20)
def go_down():
	if player.direction=="down":
		y=player.ycor()
		player.sety(y - 20)
def go_left():
	if player.direction=="left":
		x=player.xcor()
		player.setx(x - 20)
def go_right():
	if player.direction=="right":
		x=player.xcor()
		player.setx(x + 20)
#Keyboard Bindings Calling
wn.listen()
wn.onkey(go_up, "up")
wn.onkey(go_down, "down")	
wn.onkey(go_left, "left")
wn.onkey(go_right, "right")



#Main Game Loop 


