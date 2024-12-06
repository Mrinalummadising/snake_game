import turtle
import time
import random

# Initialize the screen
sc = turtle.Screen()
sc.bgcolor("blue")
sc.setup(height=1000, width=1000)
delay = 0.1

# Initialize variables
segments = []
score = 0
high_score = 0

# Create the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 100)
snake.direction = "stop"

# Functions to move the snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Functions to link with the keys
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

# Listen for key inputs
sc.listen()
sc.onkey(go_up, "w")
sc.onkey(go_down, "s")
sc.onkey(go_left, "a")
sc.onkey(go_right, "d")


# Create the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Create the score display
pen = turtle.Turtle()
pen.penup()
pen.goto(0, 100)
pen.hideturtle()
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 30, "normal"))

while True:
    sc.update()  # Update the screen
    move()  # Move the snake
    time.sleep(delay)  # Introduce a slight delay for smooth gameplay
    if snake.distance(food) < 20:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.penup()
        food.goto(x, y)
        food.pendown()

        # Increase the length of the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        score += 1

        # Update score and high score
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 30, "normal"))

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to follow the head
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
