import badger2040

bitmaps = {
    'up': [0, 0, 0, 24, 60, 102, 195, 129, 231, 36, 36, 36, 60, 0, 0, 0],
    'down': [0, 0, 0, 60, 36, 36, 36, 231, 129, 195, 102, 60, 24, 0, 0, 0],
    'right': [0, 0, 48, 56, 44, 230, 131, 131, 230, 44, 56, 48, 0, 0, 0, 0],
    'left': [0, 0, 12, 28, 52, 103, 193, 193, 103, 52, 28, 12, 0, 0, 0, 0],
    'close': [0, 0, 124, 56, 186, 146, 214, 198, 214, 146, 186, 56, 124, 0, 0, 0],
    'resize': [0, 0, 254, 254, 254, 252, 252, 248, 250, 242, 246, 230, 238, 0, 0, 0],
    'full': [0, 0, 238, 198, 214, 146, 186, 56, 186, 146, 214, 198, 238, 0, 0, 0],
    'fujil': [0, 5, 5, 5, 5, 13, 13, 29, 57, 121, 113, 113, 97, 65, 0, 0],
    'fujir': [0, 160, 160, 160, 160, 176, 176, 184, 156, 158, 142, 142, 134, 130, 0, 0],    ' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    '!': [0, 0, 24, 24, 24, 24, 24, 24, 24, 24, 0, 0, 24, 24, 0, 0],
    '"': [0, 0, 102, 102, 102, 102, 102, 102, 0, 0, 0, 0, 0, 0, 0, 0],
    '#': [0, 0, 102, 102, 255, 255, 102, 102, 255, 255, 102, 102, 0, 0, 0, 0],
    '$': [24, 24, 62, 126, 96, 96, 124, 62, 6, 6, 126, 124, 24, 24, 0, 0],
    '%': [0, 0, 102, 102, 108, 12, 24, 24, 48, 54, 102, 102, 0, 0, 0, 0],
    '&': [56, 124, 108, 108, 56, 56, 112, 112, 222, 222, 204, 204, 254, 118, 0, 0], 
    "'": [0, 0, 24, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0],
    '(': [0, 0, 6, 12, 28, 24, 24, 24, 24, 24, 24, 28, 12, 6, 0, 0],
    ')': [0, 0, 96, 48, 56, 24, 24, 24, 24, 24, 24, 56, 48, 96, 0, 0],
    '*': [0, 0, 102, 102, 60, 60, 255, 255, 60, 60, 102, 102, 0, 0, 0, 0],
    '+': [0, 0, 0, 24, 24, 24, 126, 126, 24, 24, 24, 0, 0, 0, 0, 0],
    ',': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 24, 48, 32],
    '-': [0, 0, 0, 0, 0, 0, 126, 126, 0, 0, 0, 0, 0, 0, 0, 0],
    '.': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 24, 0, 0],
    '/': [0, 0, 6, 6, 6, 12, 12, 24, 24, 48, 48, 96, 96, 96, 0, 0],
    '0': [0, 0, 60, 126, 102, 102, 102, 110, 118, 102, 102, 102, 126, 60, 0, 0],
    '1': [0, 0, 24, 24, 56, 56, 24, 24, 24, 24, 24, 24, 126, 126, 0, 0],
    '2': [0, 0, 60, 126, 102, 102, 12, 12, 24, 24, 48, 48, 126, 126, 0, 0],
    '3': [0, 0, 126, 126, 12, 12, 24, 24, 12, 12, 102, 102, 126, 60, 0, 0],
    '4': [0, 0, 12, 12, 28, 28, 60, 60, 108, 108, 126, 126, 12, 12, 0, 0],
    '5': [0, 0, 126, 126, 96, 96, 124, 126, 6, 6, 6, 102, 126, 60, 0, 0],
    '6': [0, 0, 28, 60, 112, 96, 96, 124, 126, 102, 102, 102, 126, 60, 0, 0],
    '7': [0, 0, 126, 126, 6, 6, 12, 12, 24, 24, 48, 48, 48, 48, 0, 0],
    '8': [0, 0, 60, 126, 102, 102, 60, 60, 102, 102, 102, 102, 126, 60, 0, 0],
    '9': [0, 0, 60, 126, 102, 102, 126, 62, 6, 6, 6, 14, 60, 56, 0, 0],
    ':': [0, 0, 0, 0, 24, 24, 24, 24, 0, 0, 24, 24, 24, 24, 0, 0],
    ';': [0, 0, 0, 0, 24, 24, 24, 24, 0, 0, 24, 24, 24, 24, 48, 32],
    '<': [0, 0, 0, 14, 28, 56, 112, 224, 112, 56, 28, 14, 0, 0, 0, 0],
    '=': [0, 0, 0, 0, 126, 126, 0, 0, 126, 126, 0, 0, 0, 0, 0, 0],
    '>': [0, 0, 0, 224, 112, 56, 28, 14, 28, 56, 112, 224, 0, 0, 0, 0],
    '?': [0, 0, 60, 126, 102, 102, 12, 12, 24, 24, 24, 0, 24, 24, 0, 0],
    '@': [0, 0, 56, 124, 230, 194, 218, 214, 214, 220, 192, 226, 126, 60, 0, 0],
    'A': [0, 0, 24, 60, 126, 102, 102, 102, 126, 126, 102, 102, 102, 102, 0, 0],
    'B': [0, 0, 124, 126, 102, 102, 126, 124, 102, 102, 102, 102, 126, 124, 0, 0],
    'C': [0, 0, 60, 126, 102, 102, 96, 96, 96, 96, 102, 102, 126, 60, 0, 0],
    'D': [0, 0, 120, 124, 110, 102, 102, 102, 102, 102, 102, 110, 124, 120, 0, 0],
    'E': [0, 0, 126, 126, 96, 96, 124, 124, 96, 96, 96, 96, 126, 126, 0, 0],
    'F': [0, 0, 126, 126, 96, 96, 124, 124, 96, 96, 96, 96, 96, 96, 0, 0],
    'G': [0, 0, 62, 126, 96, 96, 110, 110, 102, 102, 102, 102, 126, 60, 0, 0],
    'H': [0, 0, 102, 102, 102, 102, 126, 126, 102, 102, 102, 102, 102, 102, 0, 0],
    'I': [0, 0, 126, 126, 24, 24, 24, 24, 24, 24, 24, 24, 126, 126, 0, 0],
    'J': [0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 102, 102, 126, 60, 0, 0],
    'K': [0, 0, 204, 204, 216, 216, 240, 240, 216, 216, 204, 204, 198, 198, 0, 0],
    'L': [0, 0, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 126, 126, 0, 0],
    'M': [0, 0, 198, 198, 238, 238, 254, 214, 214, 198, 198, 198, 198, 198, 0, 0],
    'N': [0, 0, 102, 102, 102, 118, 118, 126, 126, 110, 110, 102, 102, 102, 0, 0],
    'O': [0, 0, 60, 126, 102, 102, 102, 102, 102, 102, 102, 102, 126, 60, 0, 0],
    'P': [0, 0, 124, 126, 102, 102, 102, 102, 126, 124, 96, 96, 96, 96, 0, 0],
    'Q': [0, 0, 60, 126, 102, 102, 102, 102, 102, 102, 102, 106, 124, 54, 0, 0],
    'R': [0, 0, 248, 252, 204, 204, 204, 252, 248, 216, 204, 204, 198, 198, 0, 0],
    'S': [0, 0, 62, 126, 96, 96, 112, 56, 28, 14, 6, 6, 126, 124, 0, 0],
    'T': [0, 0, 126, 126, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 0, 0],
    'U': [0, 0, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 126, 60, 0, 0],
    'V': [0, 0, 102, 102, 102, 102, 102, 102, 102, 102, 60, 60, 24, 24, 0, 0],
    'W': [0, 0, 198, 198, 198, 198, 198, 214, 214, 254, 254, 238, 198, 130, 0, 0],
    'X': [0, 0, 102, 102, 102, 60, 60, 24, 24, 60, 60, 102, 102, 102, 0, 0],
    'Y': [0, 0, 102, 102, 102, 102, 60, 60, 24, 24, 24, 24, 24, 24, 0, 0],
    'Z': [0, 0, 126, 126, 12, 12, 24, 24, 48, 48, 96, 96, 126, 126, 0, 0],
    '[': [0, 0, 30, 30, 24, 24, 24, 24, 24, 24, 24, 24, 30, 30, 0, 0],
    '\\': [0, 0, 96, 96, 96, 48, 48, 24, 24, 12, 12, 6, 6, 6, 0, 0],
    ']': [0, 0, 120, 120, 24, 24, 24, 24, 24, 24, 24, 24, 120, 120, 0, 0],
    '^': [0, 16, 16, 56, 56, 108, 108, 198, 198, 0, 0, 0, 0, 0, 0, 0],
    '_': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 254, 0, 0],
    '`': [64, 96, 112, 56, 28, 12, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'a': [0, 0, 0, 0, 0, 60, 62, 6, 62, 126, 102, 102, 126, 62, 0, 0],
    'b': [0, 0, 96, 96, 96, 124, 126, 102, 102, 102, 102, 102, 126, 124, 0, 0],
    'c': [0, 0, 0, 0, 0, 60, 124, 96, 96, 96, 96, 96, 126, 62, 0, 0],
    'd': [0, 0, 6, 6, 6, 62, 126, 102, 102, 102, 102, 102, 126, 62, 0, 0],
    'e': [0, 0, 0, 0, 0, 60, 126, 102, 102, 126, 96, 96, 126, 62, 0, 0],
    'f': [0, 0, 14, 30, 24, 24, 126, 126, 24, 24, 24, 24, 24, 24, 0, 0],
    'g': [0, 0, 0, 0, 0, 62, 126, 102, 102, 102, 102, 126, 62, 6, 126, 124],
    'h': [0, 0, 96, 96, 96, 124, 126, 102, 102, 102, 102, 102, 102, 102, 0, 0],
    'i': [0, 0, 24, 24, 0, 56, 56, 24, 24, 24, 24, 24, 60, 60, 0, 0],
    'j': [0, 0, 12, 12, 0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 124, 120],
    'k': [0, 0, 192, 192, 192, 204, 220, 248, 240, 248, 216, 204, 206, 198, 0, 0],
    'l': [0, 0, 56, 56, 24, 24, 24, 24, 24, 24, 24, 24, 60, 60, 0, 0],
    'm': [0, 0, 0, 0, 0, 108, 254, 254, 214, 214, 214, 198, 198, 198, 0, 0],
    'n': [0, 0, 0, 0, 0, 60, 126, 102, 102, 102, 102, 102, 102, 102, 0, 0],
    'o': [0, 0, 0, 0, 0, 60, 126, 102, 102, 102, 102, 102, 126, 60, 0, 0],
    'p': [0, 0, 0, 0, 0, 124, 126, 102, 102, 102, 102, 102, 126, 124, 96, 96],
    'q': [0, 0, 0, 0, 0, 62, 126, 102, 102, 102, 102, 102, 126, 62, 6, 6],
    'r': [0, 0, 0, 0, 0, 124, 126, 102, 96, 96, 96, 96, 96, 96, 0, 0],
    's': [0, 0, 0, 0, 0, 62, 126, 96, 112, 60, 14, 6, 126, 124, 0, 0],
    't': [0, 0, 0, 24, 24, 126, 126, 24, 24, 24, 24, 24, 30, 14, 0, 0],
    'u': [0, 0, 0, 0, 0, 102, 102, 102, 102, 102, 102, 102, 126, 62, 0, 0],
    'v': [0, 0, 0, 0, 0, 102, 102, 102, 102, 102, 60, 60, 24, 24, 0, 0],
    'w': [0, 0, 0, 0, 0, 198, 198, 214, 214, 254, 254, 238, 198, 130, 0, 0],
    'x': [0, 0, 0, 0, 0, 102, 102, 60, 60, 24, 60, 60, 102, 102, 0, 0],
    'y': [0, 0, 0, 0, 0, 102, 102, 102, 102, 102, 102, 126, 62, 6, 126, 124],
    'z': [0, 0, 0, 0, 0, 126, 126, 12, 24, 24, 48, 48, 126, 126, 0, 0],
    '{': [0, 14, 24, 24, 24, 24, 56, 240, 240, 56, 24, 24, 24, 24, 14, 0],
    '|': [0, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 0],
    '}': [0, 224, 48, 48, 48, 48, 56, 30, 30, 56, 48, 48, 48, 48, 224, 0],
    '~': [0, 0, 0, 0, 0, 98, 242, 190, 156, 0, 0, 0, 0, 0, 0, 0]
}

def char(display, c, x, y, inv = 0):
    inv = inv * 255
    bits = bytearray((b ^ inv) for b in bitmaps[c])
    display.image(bits, 8, 16, x, y)   

def write(display, s, x, y, inv = 0):
    for c in s:
        char(display, c, x, y, inv)
        x = x + 8

def printline(display, line, x, y, width, centre):
    line = line[:-1]
    size = display.measure_text(line, 1.0) - (len(line) * 0.2)
    off = int((width - size) * centre / 2)
    display.text(line, x + off, y)
    
    
def para(display, s, x, y, width, centre = 0):
    display.pen(0)
    display.thickness(1)
    display.font("bitmap8")
    line = ''
    words = s.split(' ')
    
    for word in words:
        size = display.measure_text(line + word + ' ', 1.0) - (len(line) * 0.2)
        if size < width:
            line += word + ' '
        else:
            printline(display, line, x, y, width, centre) 
            y += 12
            line = word + ' '
            
    printline(display, line, x, y, width, centre) 
