import math
from p5 import *
from CoolColor import CC
col=CC(255,0,0)
orig_scale=100
scale=orig_scale
polar=False
paused=False
update=None
window=Vector(600,600)
def zeta(s,n):
    total=[1]
    for i in range(2,n+1):
        total.append(total[-1]+i**-s)
    return total
def mouse_wheel(event):
    global scale
    scale+=int(event.scroll.y)
    scale=abs(scale)
def mouse_dragged(event):
    if event.button=="RIGHT":
        size(mouse_x,mouse_y)
def mouse_pressed(event):
    global paused
    if event.button=="MIDDLE":
        paused=not paused
def key_pressed(event):
    global paused,update,scale,polar
    if event.key=="SPACE":
        paused=True
        update=complex(input("Complex number: "))
    elif event.key=="R":
        size(window.x,window.y)
        scale=orig_scale
    elif event.key=="S":
        scale=orig_scale
    elif event.key=="W":
        size(window.x,window.y)
    elif event.key=="P":
        polar=not polar
def setup():
    size(window.x,window.y)
def draw():
    global col,comp,update
    trans=Vector(width/2,height/2)
    background(0)
    stroke(96)
    line((trans.x,height),(trans.x,0))
    line((0,trans.y),(width,trans.y))
    translate(trans.x,trans.y)
    if polar:
        rad=ceil((trans.x+trans.y)/2)+scale
        for r in range(scale,rad*2+scale,scale):
            no_fill()
            ellipse((0,0),r*2,r*2)
        rad*=2
        for t in [PI/4,PI/3,PI/6,0]:
            line((rad*cos(t),rad*sin(t)),(rad*cos(t+PI),rad*sin(t+PI)))
            line((rad*cos(-t),rad*sin(-t)),(rad*cos(-t+PI),rad*sin(-t+PI)))
    else:
        range_x=ceil(trans.x)
        range_y=ceil(trans.y)
        for x in range(-scale,-range_x,-scale):
            line((x,5),(x,-5))
        for x in range(scale,range_x,scale):
            line((x,5),(x,-5))
        for y in range(-scale,-range_y,-scale):
            line((5,y),(-5,y))
        for y in range(scale,range_y,scale):
            line((5,y),(-5,y))
    if not paused and update==None:
        comp=complex(mouse_x-trans.x,-mouse_y+trans.y)
    if update!=None:
        comp=update*scale
    fill(255,255,0)
    ellipse((comp.real,-comp.imag),5,5)
    comps=zeta(comp/scale,201)
    for i in range(0,len(comps)-1):
        stroke(col.col)
        c=comps[i]*scale
        c2=comps[i+1]*scale
        line((c.real,-c.imag),(c2.real,-c2.imag))
        col=col.invert
    update=None
run()
