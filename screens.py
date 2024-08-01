from math import *
from graphics2 import *

win = GraphWin("CS Paint", 500, 500, autoflush=False)

global currentScreen
currentScreen = None

#Make a button class with methods
class Button:
    def __init__(self, x, y, xr, yr, shape, c, text, func=None):
        self.x = x
        self.y = y
        self.xr = xr
        self.yr = yr
        self.shape = shape
        self.c = c
        self.func = func
        self.text = text
    
    #Makes a button that doesn't do anything
    def cloneFake(self):
        return Button(self.x, self.y, self.xr, self.yr, self.shape, self.c, self.text)
        
    def drawBtn(self):
        if self.shape == 'r':
            self.b = Rectangle(Point(self.x, self.y), Point(self.x + self.xr, self.y + self.yr))
            self.btext = Text(Point(self.x + self.xr/2, self.y + self.yr/2), self.text)
        elif self.shape == 'c':
            self.b = Circle(Point(self.x, self.y), (self.xr + self.yr)/2)
            self.btext = Text(Point(self.x, self.y), self.text)
        self.b.setFill(self.c)
        self.btext.setFill('black')
        self.b.draw(win)
        self.btext.draw(win)
            
    def undrawBtn(self):
        self.b.undraw()
        self.btext.undraw()
    
    def onClick(self, mx, my):
        if self.func != None:
            if self.shape == 'r':
                if self.x <= mx <= self.x + self.xr and self.y <= my <= self.y + self.yr:
                    self.func()
                else:
                    return False
            elif self.shape == 'c':
                if sqrt((self.x - mx)**2 + (self.y - my)**2) <= (self.xr+self.yr)/2:
                    self.func(self)
                else:
                    return False

#Screen class with methods
class Screen:
    def __init__(self, replace, c, btns, text, x=-10, y=-10, x2=510, y2=510):
        self.replace = replace
        self.c = c
        self.btns = btns
        self.text = text
        self.drawn = False
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    
    def drawScrn(self):
        if not self.drawn:
            self.drawn = True
            self.bg = Rectangle(Point(self.x, self.y), Point(self.x2, self.y2))
            self.bg.setFill(self.c)
            self.bg.draw(win)
            self.stext = Text(Point(int((self.x+self.x2)/2), int(3*(self.y+self.y2)/20)+min(self.y, 60)), self.text)
            self.stext.setSize(int(3*(self.x+self.x2)/50))
            self.stext.draw(win)
            for b in self.btns:
                b.drawBtn()
    
    def undrawScrn(self):
        if self.drawn:
            self.drawn = False
            self.bg.undraw()
            self.stext.undraw()
            for b in self.btns:
                b.undrawBtn()
    
    def changeScrn(self, new):
        if new.replace:
            self.undrawScrn()
        new.drawScrn()
        return new
    
    def checkFuncs(self, m=None):
        if m != None:
            for b in self.btns:
                b.onClick(m[0], m[1])
