import pygame
from object import Object
from random import *


SQUARE = "assets/pieces/square.png"
L_RIGHT = "assets/pieces/l-right.png"
L_LEFT = "assets/pieces/l-left.png"
T = "assets/pieces/t-shape.png"
STRAIGHT_LINE = "assets/pieces/vertical.png"
HORIZONTAL_LINE = "assets/pieces/horizontal.png"


class Wall(Object):
    def __init__(self, window, pos):
        self.window = window
        self.wallParts = []
        self.pos = pos
        self.pieces = [SQUARE, L_RIGHT, L_LEFT, T, STRAIGHT_LINE, HORIZONTAL_LINE]
        self.initSprite()
        self.initWallPart()
    
    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
    
    def initWallPart(self):

        # self.wallParts.append(self.image.get_rect())
        i = 6
        while i > 0:        
            r = randint(0, i)
            self.wallParts.append(pygame.image.load(self.pieces[r]).convert())
            self.pieces.pop(r)
            i -= 1

        self.wallParts[0].move_ip(self.pos[0])
        self.wallParts[1].move_ip(self.pos[1])
        self.wallParts[2].move_ip(self.pos[2])
        self.wallParts[3].move_ip(self.pos[3])
        self.wallParts[4].move_ip(self.pos[4])
        self.wallParts[5].move_ip(self.pos[5])

    def update(self, dt):
        for w in self.wallParts:
            self.window.blit(self.image, w)

