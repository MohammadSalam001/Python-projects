#Coded by Mohammad Salam

# Still updating it ...

import turtle

wn = turtle.Screen()
wn.title("Ping Pong by Mohammad Salam")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)


#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                          Player B: 0", align="center", font=("Coruier", 24, "bold"))


# Paddle X

paddle_x = turtle.Turtle()
paddle_x.speed(0)
paddle_x.shape("square")
paddle_x.color("blue")
paddle_x.shapesize(stretch_wid=5, stretch_len=1)
paddle_x.penup()
paddle_x.goto(-350, 0)

# Paddle M

paddle_m = turtle.Turtle()
paddle_m.speed(0)
paddle_m.shape("square")
paddle_m.color("blue")
paddle_m.shapesize(stretch_wid=5, stretch_len=1)
paddle_m.penup()
paddle_m.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.05
ball.dy = -0.05


# Function:-

#Paddle X Up and Down
def paddle_x_up():
    y = paddle_x.ycor()
    y += 20
    paddle_x.sety(y)

def paddle_x_down():
    y = paddle_x.ycor()
    y -= 20
    paddle_x.sety(y)

#Paddle M up and down
def paddle_m_up():
    y = paddle_m.ycor()
    y += 30
    paddle_m.sety(y)

def paddle_m_down():
    y = paddle_m.ycor()
    y -= 30
    paddle_m.sety(y)




#Keyboard binding
wn.listen()
wn.onkeypress(paddle_x_up, "w")
wn.onkeypress(paddle_x_down, "s")

wn.onkeypress(paddle_m_up, "Up")
wn.onkeypress(paddle_m_down, "Down")


#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Boarder checking 
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
   
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball touching
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_m.ycor() + 40 and ball.ycor() > paddle_m.ycor() -40):
        ball.setx(340)
        ball.dx += -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_x.ycor() + 40 and ball.ycor() > paddle_x.ycor() -40):
        ball.setx(-340)
        ball.dx += -1



