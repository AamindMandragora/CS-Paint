from graphicsHax import *
from screens import *
from canvas import *

from math import *
from random import *

#Sets the frames per second of the window
fps = 60

def main():
    while win.isOpen():
        global currentScreen
        global r
        currentScreen = getCurrentScreen()
        if not currentScreen.drawn:
            currentScreen.drawScrn()
        if currentScreen != canvas:
            if not win.isOpen():
                break
            mPos = win.getMouse()
            abc = [mPos.getX(), mPos.getY()]
            currentScreen.checkFuncs(abc)
        if currentScreen == canvas:
            #Binds mouse actions to different events
            bindEvent(win, '<B1-Motion>', saveEvent)
            bindEvent(win, '<Button-1>', saveEvent)
            bindEvent(win, '<ButtonRelease-1>', deletePast)
            abc = xy(getSavedEvent())
            #Check if mouse is outside or inside canvas
            if abc != None:
                if 100 + r < abc[0] < 400 - r:
                    drawOnScreen(abc)
                else:
                    currentScreen.checkFuncs(abc)
            update(fps)
main()