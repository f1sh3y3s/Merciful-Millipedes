import turtle
import time
import random
import keyboard

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

def paddle_a_up(paddle_a):
    """Move the paddle_a up by 20."""
    y = paddle_a.ycor()
    if y + 50 < 290:
        y += 0.5
    paddle_a.sety(y)

def paddle_a_down(paddle_a):
    """Move the paddle_a down by 20."""
    y = paddle_a.ycor()
    if y - 50 > -290:
        y -= 0.5
    paddle_a.sety(y)

def get_random_cords():
    x = random.randint(-200, 200)
    y = random.randint(-250, 250)
    return x, y

def main():
    # Window of turtle.
    window = turtle.Screen()
    window.title('Pong Game - Medium')
    window.bgcolor('grey')
    window.setup(width=800, height=600)
    window.tracer(0)

    # Paddle A.
    paddle_a = make_obj(stretch=(5, 1), cordinates=(-350, 0))

    # Paddle B.
    paddle_b = make_obj(stretch=(5, 1), cordinates=(350, 0))

    # Ball
    ball = make_obj(cordinates=get_random_cords())

    # Define the deltas for the ball.
    # Now it will move by 2 pixels everytime.
    ball.dx = 0.15
    ball.dy = 0.15

    # Pen
    pen = make_obj(cordinates=(0, 260))
    pen.hideturtle()
    pen.write("You: 0  Computer: 0", align="center", font=('Courier', 20, 'normal'))

    # Score.
    score_a = 0
    score_b = 0

    # Keyboard binding.
    window.listen()
    # Listen to up, w, down, s keys to move the paddles.
    # window.onkeypress(paddle_a_up, 'Up')
    # window.onkeypress(paddle_a_down, 'Down')

    # Main game loop
    while True:
        if keyboard.is_pressed('Up arrow'):
            paddle_a_up(paddle_a)
        if keyboard.is_pressed('Down arrow'):
            paddle_a_down(paddle_a)

        a = 0
        if a == 10:
            a = 0
            time.sleep(0.00000001)
        window.update()

        # Move the randomly in any direction.
        if random.randint(0, 50000) == 1:
            ball.dx = -0.1
        if random.randint(0, 100000) == 1:
            ball.dy *= -1

        # Move the ball.
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking.
        if ball.ycor() > 290:
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.dy *= -1

        if ball.xcor() > 380:
            x, y = get_random_cords()
            ball.goto(x, y)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("You: " + str(score_a) + "  Computer: " + str(score_b), align="center", font=('Courier', 20, 'normal'))


        if ball.xcor() < -390:
            x, y = get_random_cords()
            ball.goto(x, y)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("You: " + str(score_a) + "  Computer: " + str(score_b), align="center", font=('Courier', 20, 'normal'))

        # Paddle and ball colision.
        if (ball.xcor() > 330 and ball.xcor() < 340) and (int(ball.ycor()) in list(range(int(paddle_b.ycor() - 50), int(paddle_b.ycor() + 50)))):
            ball.setx(330)
            ball.dx *= -1
        if (ball.xcor() < -330 and ball.xcor() > -340) and (int(ball.ycor()) in list(range(int(paddle_a.ycor() - 50), int(paddle_a.ycor() + 50)))):
            ball.setx(-330)
            ball.dx *= -1

        # Make the computer paddle move.
        ball_y = ball.ycor()
        if ball.xcor() > 80:
            if random.randrange(0, 4) == 1:
                if paddle_b.ycor() + 50 < ball_y:
                    paddle_b.sety(paddle_b.ycor() + 1)
                if paddle_b.ycor() - 50 > ball_y:
                    paddle_b.sety(paddle_b.ycor() - 1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        exit(0)
