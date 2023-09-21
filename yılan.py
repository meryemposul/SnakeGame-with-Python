import turtle
import time
import random

hız = 0.15

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("light blue")
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("circle")
kafa.color("darkred")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"


yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("square")
yemek.color("black")
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

kuyruk =[]
puan = 0


topla = turtle.Turtle()
topla.speed(0)
topla.shape("square")
topla.color("black")
topla.penup()
topla.goto(0, 260)
topla.hideturtle()
topla.write("puan:{}" .format(puan), align="center", font=("Courier", 24,"normal"))
def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x-20)
def goUp():
    if kafa.direction != "down":
         kafa.direction = "up"
def goDown():
    if kafa.direction != "up":
        kafa.direction = "down"
def goLeft():
    if kafa.direction != "right":
        kafa.direction = "left"

def goRight():
    if kafa.direction != "left":
        kafa.direction = "right"

pencere.listen()
pencere.onkey(goUp,"Up")
pencere.onkey(goDown,"Down")
pencere.onkey(goRight,"Right")
pencere.onkey(goLeft,"Left")



while True:
    pencere.update()
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() >300 or kafa.ycor() <-300:
       time.sleep(1)
       kafa.goto(0,0)
       kafa.direction = "stop"

       for k in kuyruk:
           k.goto(1000, 1000)

       kuyruk =[]
       puan = 0
       topla.clear()
       topla.write("puan:{}" .format(puan), align="center", font=("Courier", 24,"normal"))

       hız=0.15



    if kafa.distance(yemek) < 20 :
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek .goto(x, y)

        puan = puan+10
        topla.clear()
        topla.write("puan:{}" .format(puan), align="center", font=("Courier", 24,"normal"))

        hız= hız - 0.001

        yeniKuyruk =turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("square")
        yeniKuyruk.color("white")
        yeniKuyruk.penup()
        kuyruk.append(yeniKuyruk)

    for i in range(len (kuyruk) -1, 0, -1):
        x = kuyruk[i - 1].xcor()
        y = kuyruk[i - 1].ycor()
        kuyruk[i].goto(x, y)

    if len (kuyruk) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruk[0].goto(x, y)

    move()
    time.sleep(hız)
