import pygame
from object import Object

class Piece(Object):
    def __init__(self, name, pos, core):
        self.name = name
        self.core = core
        self.initSprite(pos)

    def initSprite(self, pos):
        print(self.name)
        self.image = pygame.image.load("assets/pieces/" + self.name + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)

    def update(self, dt):
        self.core.window.blit(self.image, self.rect)