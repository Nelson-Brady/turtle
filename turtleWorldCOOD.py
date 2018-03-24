import turtle
import random
import math
import easygui


#Set up screen
win = turtle.Screen()
win.bgcolor("black")
win.title("10x10")

#Set world coordinates
turtle.setworldcoordinates(-1, -1, 11, 11)

#create the robot turtle
robot = turtle.Turtle()
robot.color("green")
robot.shape("classic")
robot.penup() # Penup until start position set
robot.speed(0)
robot.setposition(0, 0)
robot.setheading(0)# we want default to start
robotHeading = 0    # We had it start at zero, but we will change it.

#create an obstacle turtle
obs = turtle.Turtle()
obs.color("red")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
obs.shape("square")
obs.shapesize(1,4,0)
obs.penup()
obs.speed(0)
#obstacle position - Random
obsx = random.randint(1, 9)
obsy = random.randint(3, 9)
obs.setposition(obsx, obsy)
obs.setheading(135)

#create a second obstacle turtle
obs2 = turtle.Turtle()
obs2.color("red")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
obs2.shape("square")
obs2.shapesize(1,4,0)
obs2.penup()
obs2.speed(0)
#obstacle position - Random
obs2x = random.randint(4, 9)
obs2y = random.randint(2, 9)
obs2.setposition(obs2x, obs2y)
obs2.setheading(135)

#create a third obstacle turtle
obs3 = turtle.Turtle()
obs3.color("red")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
obs3.shape("square")
obs3.shapesize(1,4,0)
obs3.penup()
obs3.speed(0)
#obstacle position - Random
obs3x = random.randint(4, 9)
obs3y = random.randint(2, 9)
obs3.setposition(obs3x, obs3y)
obs3.setheading(135)

#create a fourth obstacle turtle
obs4 = turtle.Turtle()
obs4.color("red")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
obs4.shape("square")
obs4.shapesize(1,4,0)
obs4.penup()
obs4.speed(0)
#obstacle position - Random
obs4x = random.randint(4, 9)
obs4y = random.randint(2, 9)
obs4.setposition(obs4x, obs4y)
obs4.setheading(135)

# Create the destination object
dest = turtle.Turtle()
dest.color("blue")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
dest.shape("circle")
#dest.shapesize(1,6,0)
dest.penup()
dest.speed(0)
#obstacle position - Random
destx = random.randint(1, 9)
desty = random.randint(5, 9)
dest.setposition(destx, desty)

#These can be deleted later, used for testing purposes
# Display x and y back to user.
#print("Robot is at: " + str(robot.xcor()) + "," + str(robot.ycor()))

# Display x and y of the obstacle back to user.
#print("Obstacle 1 is at: " + str(obs.xcor()) + "," + str(obs.ycor()))
#print("Obstacle 2 is at: " + str(obs2.xcor()) + "," + str(obs2.ycor()))
# Display x and y of the destination back to user.
#print("Destination is: " + str(dest.xcor()) + "," + str(dest.ycor()))

#Calculate angle to turn to face destination
#print("The robot is facing: " + str(robotHeading) + " degrees.")
easygui.msgbox(str(robotHeading) + " degrees.","Current Direction"  )

# This assumes robot is facing right down positve X-axis
powAx = math.pow(dest.xcor() - robot.xcor(), 2)
powAy = math.pow(dest.ycor() - robot.ycor(), 2)
hyp = math.sqrt(powAx + powAy)
adj = dest.xcor() - robot.xcor()
turnAngle = format(math.degrees(math.acos(adj / hyp)), '.4f')
degrees = float(turnAngle)
#print("Angle to turn: " + str(degrees))
easygui.msgbox(str(degrees) + " degrees.","Angle to turn"  )

#turn the robot
#delay = input("Press any button to face robot towards destination.")
easygui.msgbox("Press OK to turn the robot")
robot.setheading(degrees)


######
while 1:

    #Does the robot detect a colision?
    #print("Has the robot detected a colision y/n")
    #collision = input("Please enter y or n: ")
    collision = easygui.ynbox('Has the robot detected a colision?', 'Colision?', ('Yes', 'No'))

    if collision == True:
        degrees = 0
        robot.setheading(0)
        #print("Robot is facing: " + str(degrees))
        easygui.msgbox(str(robotHeading) + " degrees.", "Current Direction")

        #Move robot 1 unit in new direction
        # Calculate new robot x and y
        newfbot_x = math.cos(math.radians(degrees))
        newfbot_y = math.sin(math.radians(degrees))
        # move robot location
        robot.setposition(newfbot_x + robot.xcor(), newfbot_y + robot.ycor())
        #After moving 1, turn the robot back so it can see if it cleared obs
        powAx = math.pow(dest.xcor() - robot.xcor(), 2)
        powAy = math.pow(dest.ycor() - robot.ycor(), 2)
        hyp = math.sqrt(powAx + powAy)
        adj = dest.xcor() - robot.xcor()
        turnAngle = format(math.degrees(math.acos(adj / hyp)), '.4f')
        degrees = float(turnAngle)
        robot.setheading(degrees)

    else:
        # Move robot 1 unit in new direction
        # Calculate new robot x and y
        newfbot_x = math.cos(math.radians(degrees))
        newfbot_y = math.sin(math.radians(degrees))
        # move robot location
        robot.setposition(newfbot_x + robot.xcor(), newfbot_y + robot.ycor())






















delay = input("Press any button.")