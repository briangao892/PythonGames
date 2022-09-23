import turtle
import time
import random
import platform
import random

delay=0.1

# Score
score = 0
high_score = 0


#Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.bgpic("Suicide.gif")
wn.bgpic("imp.gif")
wn.bgpic("Distraction.gif")
wn.bgpic("airship.gif")
wn.bgpic("lava.gif")




# Register the shapes
turtle.register_shape("Sussy_girl.gif")
turtle.register_shape("crewmini.gif")
turtle.register_shape("amogus.gif")

# Set the score to  0
score = 0

# Quick Note: False means 0

# Draw the score
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score 0", align ="center", font=("Courier", 24, "normal"))

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('Sussy_girl.gif')
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('crewmini.gif')
food.color("red")
food.penup()
food.goto(0,100)

#Enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("amogus.gif")
enemy.penup()
x = random.randint(-70, 70)
y = random.randint(-30, 30)
enemy.goto(x, y)







segments = []





#Functions
def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"	

def go_right():
	if head.direction != "left":
		head.direction = "right"

def move():
	if head.direction =="up":
		y=head.ycor()
		head.sety(y + 20)

	if head.direction =="down":
		y=head.ycor()
		head.sety(y - 20)

	if head.direction =="left":
		x=head.xcor()
		head.setx(x - 20)

	if head.direction =="right":
		x=head.xcor()
		head.setx(x + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")





#Main Game Loop
while True:
	wn.update()
	# Check for a collision between the border
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"

		#Hide the segments
		for segment in segments:
			segment.goto(1000, 1000)
		#Clear the segments list
		segments.clear()
		pen.clear()
		pen.write("Score: 0  High Score 0", align="center", font=("Courier", 24, "normal"))	
		score = 0
		wn.bgpic("lava.gif")
		
		


	#Check for a collision with the food
	if head.distance(food)<20:
		#Move the food to a random position
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		
		
		#Add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("crewmini.gif")
		new_segment.color("purple")
		new_segment.penup()
		segments.append(new_segment)


		score+=1	
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
		if score > 5:
			wn.bgpic("airship.gif")
		if score > 10:
			wn.bgpic("Distraction.gif")
		if score > 15:
			wn.bgpic("imp.gif")	
		if score > 25:
			wn,bgpic("Suicide.gif")		





	#Check for a collision with the enemy
	x = len(segments)
	print (x)

	s=segments.pop(0)

	if x>0 and head.distance(enemy)<20:
		segments.pop(0)
		
		segments.goto(1000,1000)
		
		if x<0 and head.distance(enemy)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
				




		
		
	




	#Move the end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	#Move segment 0 to the place where the head is
	if len(segments)>0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)


	move()
	# Check for head collisions with the TOXIC TAIL YEAH BOIII
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			
			head.direction = "stop"

			

			# Hide the segments of the TOXIC TAIL
			for segment in segments:
				segment.goto(1000, 1000)

			# Clear the toxic tail list
			segments.clear()
			pen.clear()
			pen.write("Score: 0  High Score 0", align="center", font=("Courier", 24, "normal"))	
			score = 0




	time.sleep(delay)

wn.mainloop()