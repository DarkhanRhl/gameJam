import pygame
import operator
from object import Object

class Player(Object):
    SPEED = 200
    STUNT_DURATION = 3

    def __init__(self, core, keys, name, color):
        self.core = core
        self.keys = keys
        self.name = name
        self.color = color

        self.velocity = [0, 0]
        self.action = False
        self.hold = None
        self.stunt = 0

        self.initSprite()

    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def checkCollision(self, otherRect):
        return self.rect.colliderect(otherRect)

    def checkAction(self):
        players = self.core.getObjectsByType(Player)
        for player in players:
            if player != self:
                if self.checkCollision(player.rect):
                    if player.hold:
                        player.hold = None
                    else:
                        player.stunt = self.STUNT_DURATION

    def update(self, dt):
        if self.action:
            self.checkAction()
            self.action = False

        if self.stunt == 0:
            move = [v * self.SPEED * dt for v in self.velocity]
            self.rect.move_ip(*move)
        else:
            self.stunt -= self.stunt if dt > self.stunt else dt
            fade = self.stunt * (200 / self.STUNT_DURATION)
            newColor = (
                0 if self.color[0] == 0 else fade,
                0 if self.color[1] == 0 else fade,
                0 if self.color[2] == 0 else fade)
            self.image.fill(tuple(map(operator.sub, self.color, newColor)))

        self.core.window.blit(self.image, self.rect)

    def eventManager(self, event):
        if self.stunt != 0:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == self.keys["up"]:
                self.velocity[1] += -1
            if event.key == self.keys["down"]:
                self.velocity[1] += 1
            if event.key == self.keys["left"]:
                self.velocity[0] += -1
            if event.key == self.keys["right"]:
                self.velocity[0] += 1
            if event.key == self.keys["action"]:
                self.action = True
        if event.type == pygame.KEYUP:
            if event.key == self.keys["up"]:
                self.velocity[1] -= -1
            if event.key == self.keys["down"]:
                self.velocity[1] -= 1
            if event.key == self.keys["left"]:
                self.velocity[0] -= -1
            if event.key == self.keys["right"]:
                self.velocity[0] -= 1