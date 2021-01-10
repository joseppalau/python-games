import turtle

wn = turtle.Screen()

wn.title('Pong by Josep Palau')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#socring variables
scoreA = 0
scoreB = 0

#Paddle A - the left one
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.shapesize(stretch_wid=5, stretch_len=1) #original size is 20 width x 20 length
paddleA.color('white')
paddleA.penup()
paddleA.goto(-350,0)

#Paddle B - the right one
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.shapesize(stretch_wid=5, stretch_len=1) #original size is 20 width x 20 length
paddleB.color('white')
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(0,0)

ball.dx = 0
ball.dy = 0
ball.lastdx = 0
ball.lastdy = 0

#Score Panel
sp = turtle.Turtle()
sp.speed(0)
sp.color('white')
sp.penup()
sp.hideturtle()
sp.goto(0,260)
sp.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

def startGame():
	ball.dx = 2
	ball.dy = 2

def reStartGame():
	ball.dx = 0
	ball.dy = 0
	scoreA = 0
	scoreB = 0
	paddleA.goto(-350,0)
	paddleB.goto(350,0)	
	ball.goto(0,0)
	sp.clear()
	sp.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

def stop_ball():
	if ball.dx != 0 and ball.dy != 0:
		ball.lastdx = ball.dx 
		ball.lastdy = ball.dy 
		ball.dx = 0
		ball.dy = 0

	elif ball.dx == 0 and ball.dy == 0:
		ball.dx = ball.lastdx 
		ball.dy = ball.lastdy 

#Movements Functions
ps = 40

def paddelA_up():
	y = paddleA.ycor()
	y += ps
	paddleA.sety(y)

def paddelA_down():
	y = paddleA.ycor()
	y -= ps
	paddleA.sety(y)	

def paddelB_up():
	y = paddleB.ycor()
	y += ps
	paddleB.sety(y)

def paddelB_down():
	y = paddleB.ycor()
	y -= ps
	paddleB.sety(y)		

#keyboard bind
wn.listen()
wn.onkey(paddelA_up, 'w')
wn.onkey(paddelA_down, 's')
wn.onkey(paddelB_up, 'Up')
wn.onkey(paddelB_down, 'Down')
wn.onkey(stop_ball, 'space')
wn.onkey(startGame, 'i')
wn.onkey(reStartGame, 'r')


#Main game loop
while True:
	wn.update()

	#setting borders bounds
	if abs(ball.xcor()) == 400 - 20: 
		
		if ball.xcor() > 0:
			scoreA += 1
			sp.clear()
			sp.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

		else:
			scoreB += 1
			sp.clear()
			sp.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))
		
		ball.lastdx = -ball.dx
		ball.lastdy = -ball.dy
		ball.dx = 0
		ball.dy = 0
		ball.goto(0,0)

	if abs(ball.ycor()) == 300 - 20 :
		ball.dy *= -1	

	#ball animation
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#paddels and bolls collisions
	if ball.xcor() == paddleA.xcor()+10 and ball.ycor() >= paddleA.ycor() - 50 and ball.ycor() <= paddleA.ycor() + 50:
		ball.dx *= -1

	if ball.xcor() == paddleB.xcor()-10 and ball.ycor() >= paddleB.ycor() - 50 and ball.ycor() <= paddleB.ycor() + 50:
		ball.dx *= -1	

	