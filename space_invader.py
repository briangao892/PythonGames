import turtle
import os
import math
import random
import platform



# Set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders AMONG US")
wn.addshape("ezgif.com-resize-2.gif")
wn.addshape("Knife2.gif")
wn.bgpic("Ejected.gif")
wn.tracer(0)





# Draw Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score=0

# Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="Score {}".format(score)
score_pen.write(scorestring, False, align="Left", font=("Comic Sans", 30, "normal"))
score_pen.hideturtle()

#  Create the player turtle
player=turtle.Turtle()
player.color("cyan")
your_img=r"ezgif.com-resize-2.gif"
player.shape(your_img)
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed=0


# Choose the number of enemies
number_of_enemies=50
# Create an empty list of enemies
enemies=[]

# Add enemies to the list
for i in range(number_of_enemies):
	# Create the enemy
	enemies.append(turtle.Turtle())
	
enemy_start_x= -225
enemy_start_y= 250
enemy_number= 0

for enemy in enemies:
	enemy.color("red")
	your_img = r"ezgif.com-resize-2.gif"
	enemy.shape(your_img)
	enemy.penup()
	enemy.speed(0)
	x=enemy_start_x + (50*enemy_number)
	y=enemy_start_y 
	enemy.setposition(x,y)
	#Update the enemy number
	enemy_number +=1
	if enemy_number ==10:
		enemy_start_y -=50
		enemy_number=0

enemyspeed=0.2


# Create the player's bullet
bullet=turtle.Turtle()
bullet.color("blue")
your_img=r"Knife2.gif"
bullet.shape(your_img)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed=3

# Define bullet state
# ready- ready to fire
# fire- bullet is firing
bulletstate="ready"






# Move the player left, right, up, and down
def move_left():
	player.speed=-3


def move_right():
	player.speed=3
	
	
def move_player():
	x=player.xcor()
	x+=player.speed
	if x<-280:
		x=-280
	if x>280:
		x=280
	player.setx(x)
	

def fire_bullet():
	# Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate=="ready":
		os.system("afplay bullet.mp3&")
		bulletstate="fire"
		# Move the bullet to the just above the player
		x=player.xcor()
		y=player.ycor()+10
		bullet.setposition(x, y)
		bullet.showturtle()

# Move the player left and right
def move_up():
	player.speed=15

def move_down():
	player.speed=-15

def isCollision(t1, t2):
	if abs(t1.ycor() - t2.ycor())<40 and abs(t1.xcor() - t2.xcor())<40:
			return True
	else:
			return False




# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(move_up, "Down")
wn.onkeypress(move_down, "Up")


# Main game loop
os.system("afplay Good-Music.mp3 &")
quitflag=False
while True:
	
	if quitflag==True:
		break
	wn.update()	
	move_player()
	for enemy in enemies:
		# Move the enemy
		x=enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)

		# Move the enemy back and down
		if enemy.xcor()>280:
		# Moves all enemies down
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			# Change enemy direction
			enemyspeed*=-1

		if enemy.xcor()<-280:
		# Move all enemies down
			for e in enemies:
				y=enemy.ycor()
				y-=40
				e.sety(y)
			# Change enemy direction	
			enemyspeed*=-1
			
		# Check the bullet for a collision between the bullet and the enemy
		if isCollision(bullet,enemy):
			# Reset the bullet
			bullet.hideturtle()
			bulletstate="ready"
			bullet.setposition(0,-400)
			# Reset the enemy
			enemy.setposition(0,10000)
			
			# Update the score
			score+=1
			scorestring="Score {}".format(score)
			score_pen.clear()
			score_pen.write(scorestring, False, align="Left", font=("Comic Sans", 30, "normal"))
			
			
		
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print (" But it's too late cause you're dead")
			quitflag=True
			break			

	# Move the bullet
		if bulletstate=="fire":
			y=bullet.ycor()
			y+=bulletspeed
			bullet.sety(y)

	# Check to see if the bullet has gone to the top
		if bullet.ycor()>275:
			bullet.hideturtle()
			bulletstate="ready"





















