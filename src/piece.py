import pygame
from object import Object

class Piece(Object):
    def __init__(self, pos, core):
        self.core = core

        self.initSprite(pos)

    def initSprite(self, pos):
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)

    def update(self, dt):
        self.core.window.blit(self.image, self.rect)