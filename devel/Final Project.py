# John Swain
# Final Project
# Python Turtle Walk through

import random
import turtle
import time

screen = turtle.Screen()
turtle = turtle.Turtle()
random1 = random.randint(1,25)
random2 = random.randint(20,90)
random3 = random.randint(30,60)

turtle.shape("turtle")

print("Preferably so that you can see the shell and the Turtle window run them split screen or on 2 monitors.\n")

def main():
    print("Hi my name is John, and I will be teaching you about the turtle!\n")
    print("First a brief introduction.\n Turtle is a graphics program that comes packaged with python.\n It allows the user to manipulate text, color, and the size of shapes or text on a seperate window.")

    time.sleep(10)

    mainMenu = print("What would you like to do.\n A. introduction to turtle commands.\n B. Basic turtle drawings. \n C. Example code.\n D. Random generation ")
        
    menuChoice = input("Well what would you like to do" + " use Capital Letters. ")

    print("Remember after finishing each section to type main[] into the shell to restart")

    if menuChoice == "A":
        print("The turtle program uses a variety of commands for modifying the screen and turtle itself.\n An example of such commands are turtle.Screen[], this initates the screen and allows you to begin drawing\n Another key command is turtle.Turtle[], this enables turtle itself and lets you name it, btw the lowercase turtle in front of some commands is because they are imported from turtle\n now some turtle commands are things like turtle.forward[] turtle.left[], right and backward\n other commands are things like showturtle[] hideturtle[], reset[] clear[] fill[] color[] pencolor[] setx[] sety[], turtle automatically begins in the middle so setting x or y is important. screen.bgcolor[] sets the back ground color.\n there are many other commands but this is a basic introduction to teach you about turtle.")

    elif menuChoice == "B":
        print("There are many things you can draw with turtle and it all depends on youre creativity and the amount of time you have.\n What I am going to show you are basic drawings like squares circles stars etc\n In the next section I will show you all the code behind it.")
        shape = input("What would you like to see first ")
        
        if shape == "Square":
            for i in range(4):
                turtle.forward(200)
                turtle.left(90)
            time.sleep(5)
            screen.reset()

        if shape == "Circle":
            for i in range(360):
                turtle.forward(2)
                turtle.left(1)
            time.sleep(5)
            screen.reset()
        
        if shape == "Star":
            turtle.penup()
            turtle.setposition(200,0)
            turtle.pendown()
            for i in range(5):
                turtle.right(144)
                turtle.forward(400)
            time.sleep(5)
            screen.reset()
        
    elif menuChoice == "C":
        print("In this section I will be showing you examples of code for different shapes and explane what each command does.\n First you want to import turtle then define turtle and screen. In section A I told you the commands for both of those.\n After that you setposition if needed and use left, right, forward, and backward\n to make a square you would use turtle.forward[a number] and turtle.left/right[90] You would want to run this in a for loop\n for a circle you want to run a for loop 360 times with a turtle.forward[] less then 5 for size issuse and turtle.left/right[1], thats about as close to a circle you can get without more advanced commands\n Now that you know how turtle works why don't you try making your own basic program.")
        time.sleep(20)
        print("In Section D you will see it in use but by using rand you can make amazingly cool drawings like a spirograph\n an example would be\n for i in range[70]:\n turtle.forward[90]\n turtle.left[75] \n turtle.forward[76] \n turtle.right[45]")
        

    elif menuChoice == "D":
        print("This section will show spirographs and what happens if you use random numbers")
        SectionD = input("Do you want a spirograph or a random ")
        
        if SectionD == "Spirograph":
            turtle.penup()
            turtle.setposition(0,50)
            turtle.pendown()
            for i in range(100):
                turtle.left(116)
                turtle.forward(86)
                turtle.right(12)
                turtle.backward(16)
                turtle.left(98)
                turtle.right(41)
                turtle.forward(58)
            time.sleep(10)
            screen.reset()

        if SectionD == "random":
            turtle.penup()
            turtle.setposition(-50,50)
            turtle.pendown()
            for i in range(50):
                turtle.right(random2)
                turtle.forward(random2)
                turtle.left(random2)
                turtle.right(random1)
                turtle.forward(random2)
                turtle.right(random2)
                turtle.forward(35)
                turtle.left(random3)
            time.sleep(10)
            screen.reset()

    else:
        print("look at you testing my program :>")
main()
