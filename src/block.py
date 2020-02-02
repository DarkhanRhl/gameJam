import pygame
from object import Object

class Block(Object):
    def __init__(self, core):
        self.core = core

        self.initSprite((500, 400))

    def initSprite(self, startPos):
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.move_ip(*startPos)

    def update(self, dt):
        self.core.window.blit(self.image, self.rect)