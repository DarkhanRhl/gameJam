import pygame
from piece import Piece
from object import Object
from random import *


SQUARE = "square"
L_RIGHT = "l-right"
L_LEFT = "l-left"
T = "t-shape"
VERTICAL = "vertical"
HORIZONTAL = "horizontal"


class Wall(Object):
    def __init__(self, window, pos):
        self.window = window
        self.wallParts = []
        self.pos = pos
        self.pieces = [SQUARE, L_RIGHT, L_LEFT, T, VERTICAL, HORIZONTAL]
        self.initSprite()
        self.initWallPart()
    
    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
    
    def initWallPart(self):
        i = 5
        j = 0
        while i >= 0:        
            r = randint(0, i)
            self.wallParts.append(Piece(self.pieces[r], self.pos[j], self))
            self.pieces.pop(r)
            i -= 1
            j += 1
            
    def update(self, dt):
        for w in self.wallParts:
            w.update(dt)
    def eventManager(self, event):
        # for w in self.wallParts:
        #     if event
        print("on m'appelle l'ovni")




