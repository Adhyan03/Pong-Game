import turtle

wn = turtle.Screen()
wn.title("Pong by @Adhyan_Jain")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle() #(intializing the turtle acts like a pen)
paddle_a.speed(0)#animation speed
paddle_a.shape("square")
paddle_a.color("Blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()#no more
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle() #(meaning?)
paddle_b.speed(0)#animation speed
paddle_b.shape("square")
paddle_b.color("Red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle() #(meaning?)
ball.speed(0)#animation speed
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto( 0,0)
ball.dx = 0.5 #d = delta x=cordinate
ball.dy = -0.5 #actual movement of ball
#Function
def func_a_up():
    y = paddle_a.ycor()#returns the value back to y cordinate
    y += 20
    paddle_a.sety(y)#means set y to the new y

def func_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def func_b_up():
    y = paddle_b.ycor()#returns the value back to y cordinate
    y += 20
    paddle_b.sety(y)#means set y to the new y

def func_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard pressing
wn.listen()# means to listen for the command
wn.onkeypress(func_a_up,"w")
wn.onkeypress(func_a_down,"s")
wn.onkeypress(func_b_up,"Up")
wn.onkeypress(func_b_down,"Down")



while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)#xcor means x cordinate
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290: #right to left
        ball.sety(290)#ball to set 290
        ball.dy *= -1 #to reverse the ball


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #left to right
        ball.goto(0 , 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1

    #Paddle and ball clash
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1



