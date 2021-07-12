import turtle

def make_obj(color='white', stretch=(1, 1), cordinates=(0, 0), shape='square'):
    """The function to make the object on the turtle screen."""
    object_name = turtle.Turtle()
    object_name.speed(0)
    object_name.shape(shape)
    object_name.color(color)
    object_name.shapesize(stretch_wid=stretch[0], stretch_len=stretch[1])
    object_name.penup()
    object_name.goto(cordinates[0], cordinates[1])
    return object_name

def paddle_a_up():
    """Move the paddle_a up by 20."""
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    """Move the paddle_a down by 20."""
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    """Move the paddle_b up by 20."""
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    """Move the paddle_b down by 20."""
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Window of turtle.
window = turtle.Screen()
window.title('Pong Game')
window.bgcolor('grey')
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A.
paddle_a = make_obj(stretch=(5, 1), cordinates=(-350, 0))

# Paddle B.
paddle_b = make_obj(stretch=(5, 1), cordinates=(350, 0))

# Ball
ball = make_obj()

# Define the deltas for the ball.
# Now it will move by 2 pixels everytime.
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = make_obj(cordinates=(0, 260))
pen.hideturtle()
pen.write("Player A: 0  Player B: 0", align="center", font=('Courier', 20, 'normal'))

# Score.
score_a = 0
score_b = 0

# Keyboard binding.
window.listen()
# Listen to up, w, down, s keys to move the paddles.
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking.
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  Player B: " + str(score_b), align="center", font=('Courier', 20, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  Player B: " + str(score_b), align="center", font=('Courier', 20, 'normal'))

    # Paddle and ball colision.
    if (ball.xcor() > 330 and ball.xcor() < 340) and (int(ball.ycor()) in list(range(paddle_b.ycor() - 50, paddle_b.ycor() + 50))):
        ball.setx(330)
        ball.dx *= -1
    if (ball.xcor() < -330 and ball.xcor() > -340) and (int(ball.ycor()) in list(range(paddle_a.ycor() - 50, paddle_a.ycor() + 50))):
        ball.setx(-330)
        ball.dx *= -1
