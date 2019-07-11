import turtle
import random
mo =turtle.Turtle()
mo.shape("turtle")
mo.pu()
mo.goto(-300,300)
mo.speed(0)
mo.pd()
mo.color('red')
def fir():
     x,y= mo.position()
     z=x+50
     for count in range(3):
          mo.pu()
          mo.goto(x,y)
          mo.pd()
          mo.circle(25)
          x+=150
          print(x)
     mo.pu()
     mo.goto(-300,300)
     c=50
     for square in range(3):
          mo.pu() 
          mo.fd(c)
          mo.pd()
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          c+=100
          if  c <=249 :
               c+=100
          if c ==250:
               c-=100
          print("c=" + str(c))


def sec():
     #x,y= mo.position()
     x=(-322)
     for count in range(3):
          mo.pu()
          mo.goto(x,225)
          mo.pd()
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          x+=150
          print(x)
     mo.pu()
     mo.goto(-270,225)
     c=50
     for square in range(3):
          mo.pu() 
          mo.fd(c)
          mo.pd()
          mo.circle(25)
          c+=100
          if  c <=249 :
               c+=100
          if c ==250:
               c-=100
          print("c=" + str(c))

def third():
     x=(-300)
     for count in range(3):
          mo.pu()
          mo.goto(x,225-75)
          mo.pd()
          mo.circle(25)
          x+=150
          print(x)
     mo.pu()
     mo.goto(-300,225-75)
     c=50
     for square in range(3):
          mo.pu() 
          mo.fd(c)
          mo.pd()
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          c+=100
          if  c <=249 :
               c+=100
          if c ==250:
               c-=100
          print("c=" + str(c))
def forth():
     x=(-322)
     for count in range(3):
          mo.pu()
          mo.goto(x,225-150)
          mo.pd()
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          mo.fd(50)
          mo.lt(90)
          x+=150
          print(x)
     mo.pu()
     mo.goto(-270,225-150)
     c=50
     for square in range(3):
          mo.pu() 
          mo.fd(c)
          mo.pd()
          mo.circle(25)
          c+=100
          if  c <=249 :
               c+=100
          if c ==250:
               c-=100
          print("c=" + str(c))
fir()
sec()
third()
forth()
turtle.done()
