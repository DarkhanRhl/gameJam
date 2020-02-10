import pygame
import operator
import utils

from object import Object
from piece import Piece
from wall import Wall

class Player(Object):
    IA = "IA"
    NETWORK = "NETWORK"
    REAL = "REAL"

    SPEED = 300
    SPEED_HOLDING_PERCENT = 0.85

    DASH_DURATION = 0.3
    DASH_SPEED_BONUS = 500
    DASH_COOLDOWN = 2

    STUNT_DURATION = 1.5
    STUNT_FADE_INTENSITY = 150

    # NETWORK
    def __init__(self, playerType, name, pos, keys, color, core, sendDataFunc):
    
    # LOCAL
    # def __init__(self, name, pos, keys, color, core):
        self.name = name
        self.networkGame = True if sendDataFunc else False

        # NETWORK
        self.playerType = playerType
        if (playerType == self.REAL):
            self.keys = keys
            self.sendDataFunc = sendDataFunc

        # LOCAL
        self.keys = keys

        self.color = color
        self.core = core

        self.velocity = [0, 0]
        self.hold = None
        self.stunt = 0
        self.dash = 0

        self.initSprite(pos)

    def initSprite(self, pos):
        # self.image = pygame.image.load("assets/pieces/horizontal.png").convert_alpha()
        # self.changeSpriteColor((255, 0, 0))
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)

    def checkPlayerAction(self):
        players = self.core.getObjectsByType(Player)
        for player in players:
            if player != self:
                if utils.checkCollision(self.rect, player.rect):
                    if player.hold:
                        player.hold = None
                    if player.stunt == 0:
                        player.stunt = self.STUNT_DURATION
                    return True
        return False

    def checkBlockAction(self):
        blocks = self.core.getObjectsByType(Piece)
        for block in blocks:
            if utils.checkCollision(self.rect, block.rect):
                self.hold = block
                return True
        return False

    def checkWallCollision(self, rectToCheck):
        walls = self.core.getObjectsByType(Wall)
        for wall in walls:
            for part in wall.wallParts:
                if utils.checkCollision(rectToCheck, part.rectPart):
                    return part
        return None

    def checkWallPartAction(self):
        partCollided = self.checkWallCollision(self.rect)
        if partCollided != None and self.hold:
            return partCollided.checkPutPiece(self.hold.name)
        return None

    def checkAction(self):
        wallPartCollided = self.checkWallPartAction()
        if self.hold and wallPartCollided != None:
            if wallPartCollided == True:
                self.core.objects.remove(self.hold)
                self.hold = None
            return

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

    def checkIfMove(self, move):
        if (not self.checkWallCollision(self.rect)) or (self.checkWallCollision(self.rect) and not self.checkWallCollision(self.rect.move(*move))) or (self.rect.x == self.rect.x + move[0]):
            return True
        return False

    def update(self, dt):
        if self.stunt == 0:
            speed = self.SPEED * self.SPEED_HOLDING_PERCENT if self.hold else self.SPEED
            speed += self.dash if self.dash > 0 else 0
            move = [v * speed * dt for v in self.velocity]

            if self.checkIfMove(move):
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
        if datagram[0] == "1":
            self.rect.x = int(datagram[1:].split(",")[0])
            self.rect.y = int(datagram[1:].split(",")[1])
        if datagram[0] == "2" and self.stunt == 0:
            self.checkAction()
    
    def getPosition(self):
        return str(self.rect.x), str(self.rect.y)

    def eventManager(self, event):
        # NETWORK
        if (self.playerType != self.REAL):
            return
        if event.type == pygame.KEYDOWN:
            if event.key == self.keys["left"]:
                self.velocity[0] += -1
            if event.key == self.keys["right"]:
                self.velocity[0] += 1
            if event.key == self.keys["up"]:
                self.velocity[1] += -1
            if event.key == self.keys["down"]:
                self.velocity[1] += 1
            if event.key == self.keys["action"] and self.stunt == 0:
                if (self.networkGame):
                    self.sendDataFunc("2")
                self.checkAction()
        if event.type == pygame.KEYUP:
            if event.key == self.keys["left"]:
                self.velocity[0] -= -1
            if event.key == self.keys["right"]:
                self.velocity[0] -= 1
            if event.key == self.keys["up"]:
                self.velocity[1] -= -1
            if event.key == self.keys["down"]:
                self.velocity[1] -= 1
