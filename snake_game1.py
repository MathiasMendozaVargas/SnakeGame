# Simple Snake Game in Python 3 For Beginners
# By @MathiasMendoza
# Part 1: Getting Started

import random
import time
import turtle


# Set Time Delay
delay = 0.1

# Define Score and High Score Variables
score = 0
high_score = 0

# Set Up The Screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("Snake Game by @Mathias_Mendoza")
wn.bgcolor("#a76d1b")
wn.tracer(0)

# Set Up The Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Set Up The Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


# Set Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Move Function
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# KEYBOARD BINDINGS
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# SNAKE BODY LIST
segments = []
# WHILE LOOP
while True:
    wn.update()
    # Check for border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "up"
        food.goto(0, 100)
        # Hide The Segments
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear Segments List
        segments.clear()
        # Reset the delay
        delay = 0.1
        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "up"
            food.goto(0, 100)
            # Hide The Segments
            for segment in segments:
                segment.goto(1000, 1000)
            # Clear Segments List
            segments.clear()
            # Reset the delay
            delay = 0.1
            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
    # Move the food to random position
    if head.distance(food)<20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 250)
        food.goto(x, y)
        # Create new Snake segment body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        # Shorten the delay
        delay -= 0.002
        # Increase Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)

wn.mainloop()

