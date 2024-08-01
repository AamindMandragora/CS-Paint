from tkinter import *
from graphics2 import *
from screens import *

#Added imortant functions in a graphics file add-on

def bindEvent(win, event, func):
    win.bind(event, func)
    
def unbindEvent(win, event):
    win.unbind(event)
    
def getColor(win, obj):
    return obj.config['fill']

def tag(win, obj, t):
    win.addtag(t, 'withtag', obj.id)
    
def deleteObjWithTags(win, t):
    win.delete(t)