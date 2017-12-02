from p5 import Color
from random import randrange,choice
class CoolColor(object):
    def __init__(self,*args):
        self.redUp,self.greenUp,self.blueUp,self.alphaUp=(choice((-1,1)) for x in range(4))
        self.red,self.green,self.blue=(randrange(256) for x in range(3))
        self.alpha=255
        if len(args)==1:
            if type(args[0])==Color:
                self.red=args[0].red
                self.green=args[0].green
                self.blue=args[0].blue
                self.alpha=args[0].alpha
            else:
                self.red=args[0]
                self.green=args[0]
                self.blue=args[0]
        elif len(args)>2:
            self.red=args[0]
            self.green=args[1]
            self.blue=args[2]
            if len(args)==4:
                self.alpha=args[3]
    @property
    def col(self):
        return Color(self.red,self.green,self.blue,self.alpha)
    @property
    def invert(self):
        return CoolColor(abs(self.red-255),abs(self.green-255),abs(self.blue-255),self.alpha)
    def changeColor(self,diff=1,doAlpha=False):
        if self.red>=255:
            self.redUp=-1
        if self.red<=0:
            self.redUp=1
        self.red+=self.redUp*diff
        if self.green>=255:
            self.greenUp=-1
        if self.green<=0:
            self.greenUp=1
        self.green+=self.greenUp*diff
        if self.blue>=255:
            self.blueUp=-1
        if self.blue<=0:
            self.blueUp=1
        self.blue+=self.blueUp*diff
        if doAlpha:
            if self.alpha>=255:
                self.alphaUp=-1
            if self.alpha<=0:
                self.alphaUp=1
            self.alpha+=self.alphaUp*diff
    def __str__(self):
        return self.col.hex
CC=CoolColor
