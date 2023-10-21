from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, '#0000ee')
    back(100)
    right(120)
    forward(100)
    dot(120, 'yellow')
    back(100)
    right(120)
    forward(100)
    dot(120, 'black')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0 ,)
bgcolor('maroon')
hideturtle()
tracer(False)
width(20),color('#32cd32')
onkey(flick, 's')
listen()
animate()
done()
