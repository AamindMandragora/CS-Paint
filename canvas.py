from graphics2 import *
from graphicsHax import *
from screens import *

from random import *

px = ''
py = ''

sEvent = None

#Saves a mouse action
def saveEvent(event):
    global sEvent
    sEvent = event

#Returns saved mouse action
def getSavedEvent():
    global sEvent
    return sEvent

#Returns x and y of that mouse action
def xy(event):
    if event != None:
        abc = [event.x, event.y]
    else:
        abc = None
    return abc

def getCurrentScreen():
    global currentScreen
    return currentScreen

c = 'black'
r = 1

#Changes drawing color
def changeColor(self):
    global c
    c = self.c

#Changes stroke size
def makeLarger():
    global r
    if (r + 1) < 10:
        r += 1
    
def makeSmaller():
    global r
    if (r-1) > 0:
        r -= 1
 
#Changes screens
def makeHome():
    global currentScreen
    currentScreen = currentScreen.changeScrn(home)
    
def makeCanvas():
    global currentScreen
    currentScreen = currentScreen.changeScrn(canvas)
    
def makeTutorial():
    global currentScreen
    currentScreen = currentScreen.changeScrn(tutorial)
    for x in range(len(canvas.btns)):
        #Makes helper text
        if not x in [0, 3, 4, 5]:
            if x == 1 or x == 2:
                p = Point(160, canvas.btns[x].y+canvas.btns[x].yr/2)
                t = Text(p, 'Changes size of the stroke')
            elif x == 14:
                p = Point(320, canvas.btns[x].y)
                t = Text(p, 'Sets mouse to an eraser')
            elif 6 <= x <= 13:
                p = Point(320, canvas.btns[x].y)
                t = Text(p, 'Sets color to color of button on click')
            t.setSize(7)
            t.draw(win)

#Makes stroke an eraser
def erase(self):
    global c
    c = 'erase'

#Clears whole screen
def clear():
    deleteObjWithTags(win, 'drew')

#Initializes screens and their buttons
homeBtns = [Button(50, 435, 100, 40, 'r', color_rgb(200, 200, 200), 'Start', makeCanvas),
            Button(200, 435, 100, 40, 'r', color_rgb(200, 200, 200), 'Tutorial', makeTutorial),
            Button(350, 435, 100, 40, 'r', color_rgb(200, 200, 200), 'Exit', win.close)]
home = Screen(True, color_rgb(255, 255, 255), homeBtns, 'CS Paint')

global currentScreen
currentScreen = home

canvasBtns = [Button(10, 0, 80, 500, 'r', color_rgb(220, 220, 220), ''),
              Button(20, 150, 60, 60, 'r', color_rgb(220, 220, 220), '+', makeLarger),
              Button(20, 220, 60, 60, 'r', color_rgb(220, 220, 220), '-', makeSmaller),
              Button(20, 410, 60, 30, 'r', color_rgb(200, 200, 200), 'Clear', clear),
              Button(20, 450, 60, 30, 'r', color_rgb(200, 200, 200), 'Exit', win.close),
              Button(410, 0, 80, 500, 'r', color_rgb(220, 220, 220), ''),
              Button(450, 45, 15, 15, 'c', color_rgb(255, 0, 0), '', changeColor),
              Button(450, 90, 15, 15, 'c', color_rgb(255, 165, 0), '', changeColor),
              Button(450, 135, 15, 15, 'c', color_rgb(255, 255, 0), '', changeColor),
              Button(450, 180, 15, 15, 'c', color_rgb(0, 255, 0), '', changeColor),
              Button(450, 225, 15, 15, 'c', color_rgb(0, 255, 255), '', changeColor),
              Button(450, 270, 15, 15, 'c', color_rgb(0, 0, 255), '', changeColor),
              Button(450, 315, 15, 15, 'c', color_rgb(255, 0, 255), '', changeColor),
              Button(450, 360, 15, 15, 'c', color_rgb(0, 0, 0), '', changeColor),
              Button(450, 405, 15, 15, 'c', color_rgb(255, 255, 255), '', erase)]
canvas = Screen(True, color_rgb(255, 255, 255), canvasBtns, '')

tutorialBtns = [Button(100, 435, 90, 40, 'r', color_rgb(200, 200, 200), 'Home', makeHome),
                Button(205, 435, 90, 40, 'r', color_rgb(200, 200, 200), 'Start', makeCanvas),
                Button(310, 435, 90, 40, 'r', color_rgb(200, 200, 200), 'Exit', win.close)]

#Makes fake canvas butttons for tutorial screen
for x in canvasBtns:
    y = x.cloneFake()
    tutorialBtns.append(y)

tutorial = Screen(True, color_rgb(255, 255, 255), tutorialBtns, '')

#Deletes saved event
def deletePast(event=None):
    global px
    global py
    px = ''
    py = ''
    saveEvent(None)

#Drawing function
def drawOnScreen(m):
    global px
    global py
    global r
    if px == '':
        if getSavedEvent() != None:
            px = m[0]
            py = m[1]
    l = Line(Point(px, py), Point(m[0], m[1]))
    if c == 'erase':
        er = Circle(Point(m[0], m[1]), 9+r)
        l.setWidth(2*(9+r))
        c1 = 'white'
    else:
        er = Circle(Point(m[0], m[1]), r)
        l.setWidth(2*r)
        c1 = c
    er.setWidth(0)
    er.setFill(c1)
    er.draw(win)
    l.setFill(c1)
    l.draw(win)
    #Sets tags for everything drawn so it can be deleted
    tag(win, er, 'drew')
    tag(win, l, 'drew')
    
    px = m[0]
    py = m[1]
