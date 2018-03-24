#
#
#

import turtle
import random
import math


#Set up screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Whatever")

#Set world coordinates
#turtle.setworldcoordinates(-1, -1, 10, 10)

#Create border turtle
#Create a pen
border_pen = turtle.Turtle()
border_pen.speed(0) # speed 0 is fastest
border_pen.color("white")
border_pen.penup() # don't draw turtle moving from origin to corner
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

#draw the border
for side in range(4):
    border_pen.fd(600)  #move forward 600
    border_pen.left(90)  #in degrees
border_pen.hideturtle() # done with this turtle

#create the robot turtle
robot = turtle.Turtle()
robot.color("green")
robot.shape("classic")
robot.penup() # Penup until start position set
robot.speed(0)
robot.setposition(-275, -275)
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
obsx = random.randint(-250, 250)
obsy = random.randint(-250, 250)
obs.setposition(obsx, obsy)
obs.setheading(135)

#create an second obstacle turtle
obs2 = turtle.Turtle()
obs2.color("red")
#turtle shapes triangle, classic, arrow, turtle, circle,
# square
obs2.shape("square")
obs2.shapesize(1,4,0)
obs2.penup()
obs2.speed(0)
#obstacle position - Random
obs2x = random.randint(-250, 250)
obs2y = random.randint(-250, 250)
obs2.setposition(obs2x, obs2y)
obs2.setheading(135)



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
destx = random.randint(-250, 250)
desty = random.randint(150, 250)
dest.setposition(destx, desty)



run = True

#Main loop
while run:
    #Convert to normal coordinates
    robx = robot.xcor()+275
    roby = robot.ycor()+275
    obsx = obs.xcor()+275
    obsy = obs.ycor()+275
    obs2x = obs2.xcor()+275
    obs2y = obs2.ycor()+275
    desx = dest.xcor()+275
    desy = dest.ycor()+275

   #Calculate the angle that the object needs to turn
   #We will also display all the objects coordinates to the display
    print("The robot is located at: " + str(robot.xcor()) + "," + str(robot.ycor()))
    print("The robot is facing: " + str(robotHeading) + " degrees.")
    print("The robot is located at: " + str(robx) + "," + str(roby))

    #Display obstacles location
    print("The first obstacle is located at: " + str(obsx) + "," + str(obsy))
    print("The second obstacle is located at: " + str(obs2x) + "," + str(obs2y))

    #Display ending destination location
    print("The destination is located at: " + str(desx) + "," + str(desy))

    #Calculate the angle
    # This assumes robot is facing right down positve X-axis
    powAx = math.pow(desx - robx, 2)
    powAy = math.pow(desy - roby, 2)
    hyp = math.sqrt(powAx + powAy)
    adj = desx - robx
    turnAngle = format(math.degrees(math.acos(adj/hyp)), '.4f')
    degrees = float(turnAngle)
    print("Angle to turn: " + str(degrees))

    #Turn and face the destination
    delay = input("Press any button to turn robot towards destination.")
    robot.setheading(degrees)

    while 1:
        #Move or turn
        print("Does the robot detect an object?")
        turn = input("Please enter y or n: ")
        if turn == "y":
            robot.setheading(0)
        delay = input("Press any button to move robot forward 1 unit.")
        print("Moving robot")
        #Calculate new robot x and y
        newrobx = math.cos(math.radians(degrees)) / 100
        newroby = math.sin(math.radians(degrees)) / 100
        #move Robot location
        robx += newrobx
        roby += newroby
        robot.setx(robx)
        robot.sety(roby)
        #Dispaly the new robot x and y
        print("The robot has moved.")







    run = False
delay = input("Press any button.")