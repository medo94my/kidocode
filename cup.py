import turtle 
tom=turtle.Turtle()
tom.speed(100)

tom.pu()
tom.goto(0,-200)
tom.pd()
tom.shape('turtle')
tom.color('black', 'lightgray')
tom.begin_fill()

tom.width(10)
tom.circle(100,90)
tom.lt(90)
tom.seth(90)
tom.fd(200)
tom.bk(200)
tom.rt(45)
tom.circle(100,45)
tom.fd(50)
tom.circle(80,50)
tom.seth(90)
tom.fd(20)
tom.seth(90)
tom.pu()
tom.pd()
tom.circle(100)
tom.circle(100,180)
tom.fd(200)
tom.circle(100,90)
tom.lt(90)
tom.pu()
tom.fd(205)
tom.seth(0)
tom.pd()
tom.end_fill()
tom.color('brown')
tom.begin_fill()
tom.circle(80)
tom.end_fill()
tom.color('black')
tom.circle(100)
tom.rt(90)
tom.pu()
tom.fd(80)
tom.pd()
tom.left(110)
tom.color('yellow')
tom.tracer(100)
for count in range(320):
	tom.width(1)
	for count in range(4):
		tom.fd(30)
		tom.bk(30)
	tom.lt(360.0/360)
tom.ht()
