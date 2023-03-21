import badger2040
from text import char, write, para

def background(display):
    display.pen(8)
    display.rectangle(0, 0, badger2040.WIDTH, badger2040.HEIGHT)
    

def menu(display):
    display.pen(15)
    display.rectangle(0, 0, badger2040.WIDTH, 17)
    display.pen(0)
    display.line(0, 17, badger2040.WIDTH, 17)
    write(display, ' Desk  File  View  Options ', 0, 0)
    
    
def desktop(display):
    background(display)
    menu(display)
    

def window(display, s, x, y, w, h):
    display.pen(15)
    display.rectangle(x, y, w, h)
    display.pen(0)
    display.thickness(1)

    # Header
    char(display, 'close', x + 4, y + 1)
    char(display, 'full', x + w - 11, y + 1)
    display.pen(12)
    display.rectangle(x + 17, y + 1, w - 34, 16)
    display.pen(0)
    display.line(x, y + 17, x + w, y + 17)
    display.line(x + 15, y, x + 15, y + 17)
    display.line(x + 16, y, x + 16, y + 17)
    display.line(x + w - 17, y, x + w - 17, y + 17)
    display.line(x + w - 16, y, x + w - 16, y + 17)
    off = int((w - (len(s) * 8)) / 2)
    write(display, s, x + off, y + 1)
    
    # Scroll bars
    char(display, 'resize', x + w - 11, y + h - 15)
    char(display, 'left', x + 4, y + h - 15)
    char(display, 'right', x + w - 27, y + h - 15)
    char(display, 'up', x + w - 11, y + 18)
    char(display, 'down', x + w - 11, y + h - 31)
    display.line(x + w - 16, y + 16, x + w - 16, y + h)
    display.line(x, y + h - 16, x + w, y + h - 16)
    display.line(x + w - 16, y + 34, x + w, y + 34)
    display.line(x + w - 16, y + h - 32, x + w, y + h - 32)
    display.line(x + 16, y + h - 16, x + 16, y + h)
    display.line(x + w - 32, y + h - 16, x + w - 32, y + h)
    
    # Border
    display.line(x, y, x + w, y)
    display.line(x + w, y, x + w, y + h)
    display.line(x + w + 1, y + 1, x + w + 1, y + h + 1)
    display.line(x + w, y + h, x, y + h)
    display.line(x + w + 1, y + h + 1, x + 1, y + h + 1)
    display.line(x, y + h, x, y)
    
def msgbox(display, s, x, y, w, h):
    display.pen(15)
    display.rectangle(x, y, w, h)
    display.pen(0)
    display.thickness(1)
    display.line(x, y, x + w, y)
    display.line(x + w, y, x + w, y + h)
    display.line(x + w, y + h, x, y + h)
    display.line(x, y + h, x, y)
    display.thickness(2)
    display.line(x + 3, y + 3, x + w - 2, y + 3)
    display.line(x + w - 2, y + 3, x + w - 2, y + h - 2)
    display.line(x + w - 2, y + h - 2, x + 3, y + h - 2)
    display.line(x + 3, y + h - 2, x + 3, y + 3)
    
    para(display, s, x + 8, y + 8, w - 16, 1)