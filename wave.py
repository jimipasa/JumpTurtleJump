from turtle import *
import random
msg,target =["Bingo!!!","Better luck next time", "sooo close, not really", "r u kidding me", "com'on man, be serious", "u can do better than that", "almost"],0
s,i,c =shape("turtle"),bgpic("cliff.gif"),pencolor("white")
up()
def spawn():
    global target
    clear()
    target=random.randrange(-450,450,10)
    setpos(target,-350)
    stamp()
    home()
def up():left(2)
def down():rt(2)
def start():spawn()
def enter():
    while(position()[1]>-350):
        fd(20)
        if ((target-15 < pos()[0] < target+15) and (pos()[1])< -340):
            write(msg[0],False,align="left",font=("Arial",18,"normal"))
            return
        if (90<heading()<270):lt(5)
        else:rt(5)
    write(msg[random.randint(1,6)],False,align="left",font=("Arial",18,"normal"))
spawn()
onkey(up, "Up")
onkey(start, "space")
onkey(down,"Down")
onkey(enter,"Return")
listen()
exitonclick()