import pygame
import operator
from object import Object
from piece import Piece


class Player(Object):
    IA = "IA"
    NETWORK = "NETWORK"
    REAL = "REAL"

    SPEED = 250
    SPEED_HOLDING_PERCENT = 0.85

    DASH_DURATION = 0.3
    DASH_SPEED_BONUS = 500
    DASH_COOLDOWN = 2

    STUNT_DURATION = 0.5
    STUNT_FADE_INTENSITY = 150

    def __init__(self, playerType, name, pos, keys, color, core, sendDataFunc):
        self.name = name
        self.playerType = playerType
        if (playerType == self.REAL):
            self.keys = keys
            self.sendDataFunc = sendDataFunc
        self.color = color
        self.core = core

        self.velocity = [0, 0]
        self.hold = None
        self.stunt = 0
        self.dash = 0

        self.initSprite(pos)

    def initSprite(self, pos):
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)

    def checkCollision(self, otherRect):
        return self.rect.colliderect(otherRect)

    def checkPlayerAction(self):
        players = self.core.getObjectsByType(Player)
        for player in players:
            if player != self:
                if self.checkCollision(player.rect):
                    if player.hold:
                        player.hold = None
                    if player.stunt == 0:
                        player.stunt = self.STUNT_DURATION
                    return True
        return False

    def checkBlockAction(self):
        blocks = self.core.getObjectsByType(Piece)
        for block in blocks:
            if self.checkCollision(block.rect):
                self.hold = block
                return True
        return False

    def checkAction(self):
        if self.hold:
            self.hold = None
            return

        willDash = True
        if self.checkBlockAction():
            willDash = False
        if self.checkPlayerAction():
            willDash = False
        if willDash and not self.hold:
            self.dash = self.DASH_SPEED_BONUS

    def setStuntColor(self):
        fade = self.stunt * (self.STUNT_FADE_INTENSITY / self.STUNT_DURATION)
        newColor = (
            0 if self.color[0] == 0 else fade,
            0 if self.color[1] == 0 else fade,
            0 if self.color[2] == 0 else fade)
        self.image.fill(tuple(map(operator.sub, self.color, newColor)))

    def update(self, dt):
        if self.stunt == 0:
            speed = self.SPEED * self.SPEED_HOLDING_PERCENT if self.hold else self.SPEED
            speed += self.dash if self.dash > 0 else 0
            move = [v * speed * dt for v in self.velocity]
            self.rect.move_ip(*move)
            self.dash -= self.DASH_SPEED_BONUS * (dt / self.DASH_DURATION)
        else:
            self.stunt -= self.stunt if dt > self.stunt else dt
            self.setStuntColor()

        if self.hold:
            self.hold.rect = self.rect.copy()
            self.hold.rect.bottom -= 15

        self.core.window.blit(self.image, self.rect)

    def networkManager(self, datagram):
        print("OKKKK")
        if datagram[1] == "0":
            self.velocity[0] = int(datagram[2:])
        if datagram[1] == "1":
            self.velocity[1] = int(datagram[2:])
        if datagram[1] == "2" and self.stunt == 0:
            self.checkAction()

    def eventManager(self, event):
        if (self.playerType != self.REAL):
            return
        if event.type == pygame.KEYDOWN:
            if event.key == self.keys["left"]:
                self.velocity[0] += -1
                self.sendDataFunc("10" + str(self.velocity[0]))
            if event.key == self.keys["right"]:
                self.velocity[0] += 1
                self.sendDataFunc("10" + str(self.velocity[0]))
            if event.key == self.keys["up"]:
                self.velocity[1] += -1
                self.sendDataFunc("11" + str(self.velocity[1]))
            if event.key == self.keys["down"]:
                self.velocity[1] += 1
                self.sendDataFunc("11" + str(self.velocity[1]))
            if event.key == self.keys["action"] and self.stunt == 0:
                self.checkAction()
                self.sendDataFunc("12")
        if event.type == pygame.KEYUP:
            if event.key == self.keys["left"]:
                self.velocity[0] -= -1
                self.sendDataFunc("10" + str(self.velocity[0]))
            if event.key == self.keys["right"]:
                self.velocity[0] -= 1
                self.sendDataFunc("10" + str(self.velocity[0]))
            if event.key == self.keys["up"]:
                self.velocity[1] -= -1
                self.sendDataFunc("11" + str(self.velocity[1]))
            if event.key == self.keys["down"]:
                self.velocity[1] -= 1
                self.sendDataFunc("11" + str(self.velocity[1]))
