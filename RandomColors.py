import random
import turtle
bob=turtle.Turtle()
a=0
colors=("black","orange","yellow","blue","pink","green")
class Circle():
    def __init__(self,x,y,diametros,mhkos):
        self.x=x
        self.y=y
        self.diametros=diametros
        self.mhkos=mhkos

    def tetragwno(self):
        bob.speed(10)
        bob.penup()
        bob.goto(self.x,self.y)
        bob.pendown()
        color=random.choice(colors)
        bob.color(color)
        bob.fillcolor(color)
        bob.begin_fill()
        bob.forward(self.mhkos)
        bob.right(90)
        bob.forward(self.mhkos)
        bob.right(90)
        bob.forward(self.mhkos)
        bob.right(90)
        bob.forward(self.mhkos)
        bob.right(90)
        bob.end_fill()


    def kyklos(self):
        bob.speed(10)
        bob.penup()
        bob.goto(self.x,self.y)
        bob.pendown()
        bob.dot(self.diametros)
        bob.color(random.choice(colors))
    


for i in range (0,50):
    a=random.randint(1,2)
    sxhma = Circle(x=random.randint(-400,400),y=random.randint(-400,400),diametros=random.randint(0,100),mhkos=random.randint(0,100))
    if a==1:
        sxhma.tetragwno()
    else:
        sxhma.kyklos()
    i=i+1
turtle.exitonclick()
