import pygame
from object import Object

class PlayerNetwork(Object):
    SPEED = 200

    def __init__(self, window):
        self.window = window

        self.velocity = [0, 0]
        self.initSprite()

    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, dt):
        move = [v * self.SPEED * dt for v in self.velocity]
        self.rect.move_ip(*move)
        self.window.blit(self.image, self.rect)

    def receiveInsctruction(self, instruction):
        if (instruction[0] == '1'):
            self.movePlayer(instruction[1],instruction[2])

    def eventManager(self, event):
        event = event
        # hihi c moche

    def movePlayer(self, inputType, direction):
        if inputType == "1":
            if direction == "1":
                self.velocity[1] += -1
            if direction == "2":
                self.velocity[1] += 1
            if direction == "3":
                self.velocity[0] += -1
            if direction == "4":
                self.velocity[0] += 1
        if inputType == "1":
            if direction == "1":
                self.velocity[1] -= -1
            if direction == "2":
                self.velocity[1] -= 1
            if direction == "3":
                self.velocity[0] -= -1
            if direction == "4":
                self.velocity[0] -= 1
