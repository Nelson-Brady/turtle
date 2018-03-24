import turtle
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

#test = win.textinput("Robot Maze", "Do you want to y/n")
# print(test)

easygui.msgbox("stuff", "other")



delay = input("Press any button.")