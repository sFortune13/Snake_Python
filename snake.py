import math
import random
import pygame 
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirx=1, diry=0,colour=(144, 238, 144)):
        pass
    def move(self, dirx, diry):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, colour, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass


def drawMap(w, rows, surface):
    
    size_between = w // rows

    x = 0
    y = 0

    for i in range(rows):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))
    pass


def redrawWindow(surface):
    
    global rows, width
    surface.fill((0,0,0))
    drawMap(width, rows, surface)
    pygame.display.update()

    pass


def snakeFood(rows, items):
    pass


def message_box(subject, content):
    pass


def main():

    global rows, width
    width = 1000
    rows = 40
    win = pygame.display.set_mode((width, width))
    s = snake(1(24,252,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:

        pygame.time.delay(50) #lower the faster
        clock.tick(10)      #lower the slower

        redrawWindow(win)
    

main()