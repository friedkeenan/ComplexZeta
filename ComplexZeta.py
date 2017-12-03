import math
from p5 import *
from CoolColor import CC
col=CC(255,0,0)
scale=75
polar=False #Toggles polar style graph
paused=False
update=None
def zeta(s,n):
    total=[1]
    for i in range(2,n+1):
        total.append(total[-1]+i**-s)
    return total
def mouse_pressed(event):
    global paused
    if event.button=="MIDDLE":
        paused=not paused
def key_pressed(event):
    global paused,update
    if event.key=="SPACE":
        paused=True
        update=complex(input("Complex number: "))
def setup():
    size(600,600)
    global trans
    trans=Vector(width/2,height/2)
def draw():
    global col,update
    if paused and update==None:
        return
    background(0)
    stroke(96)
    line((trans.x,height),(trans.x,0))
    line((0,trans.y),(width,trans.y))
    #with push_matrix():
    translate(trans.x,trans.y)
    if polar:
        rad=ceil((trans.x+trans.y)/2+scale)
        for r in range(0,rad*2+scale,scale):
            no_fill()
            ellipse((0,0),r,r)
        for t in [PI/4,PI/3,PI/6,0]:
            line((rad*cos(t),rad*sin(t)),(rad*cos(t+PI),rad*sin(t+PI)))
            line((rad*cos(-t),rad*sin(-t)),(rad*cos(-t+PI),rad*sin(-t+PI)))
    else:
        range_x=ceil(trans.x)
        range_y=ceil(trans.y)
        for x in range(-range_x,range_x,scale):
            line((x,5),(x,-5))
        for y in range(-range_y,range_y,scale):
            line((5,y),(-5,y))
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
