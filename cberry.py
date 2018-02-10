from ctypes import *

cberry = CDLL('./cberrylib.so')

RED = 0xE0
BLUE = 0x03
GREEN  = 0x1C
BLACK = 0x00
WHITE = 0xFF
CYAN = 0x1F
YELLOW = 0xFC
MAGENTA = 0xE3
DARK_GREEN = 0x0C

def initScreen():
    cberry.initScreen()
    
def clearScreen():
    cberry.clearScreen()
    
def closeScreen():
    cberry.closeScreen()
    
def writeText(x, y, fontSize, text, bgColor, fgColor ):
    cberry.writeText(x, y, fontSize, text, bgColor, fgColor)
    
def drawSquare(x, y, width, height):
    cberry.drawSquare(x, y, width, height)
    
def fillSquare(x, y, width, height):
    cberry.fillSquare(x, y, width, height)
    
def drawLine(fromX, fromY, lenX, lenY):
    cberry.drawLine(fromX, fromY, lenX, lenY);
    
def drawCircle(x, y, radius):
    cberry.drawCircle(x, y, radius)
    
def fillCircle(x, y, radius):
    cberry.fillCircle(x, y, radius)
    
def setPenColor(color):
    cberry.setPenColor(color)
    