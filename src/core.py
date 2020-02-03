import os
import random
import time;
import pygame
from object import Object
from player import Player
from piece import Piece
from wall import Wall
from pieces import Pieces
from network import Network

pygame.init()


class Core:
    FPS = 60
    WINDOW_LENGTH = 1080
    WINDOW_HEIGHT = 720

    PLAYER1_NAME = "Blue"
    PLAYER1_START_POS = (WINDOW_LENGTH / 2 - 100, WINDOW_HEIGHT / 2)
    PLAYER1_COLOR = (0, 0, 255)
    PLAYER1_KEYS = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "action": pygame.K_RETURN
    }

    PLAYER2_NAME = "Red"
    PLAYER2_START_POS = (WINDOW_LENGTH / 2 + 100, WINDOW_HEIGHT / 2)
    PLAYER2_KEYS = {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "action": pygame.K_SPACE
    }
    PLAYER2_COLOR = (255, 0, 0)

    NUMBER_WALL_HOLE = 6
    NUMBER_PIECES = 40

    PIECE_SPAWN_RANGE_X_PERCENT = 0.1
    PIECE_SPAWN_RANGE_Y_PERCENT = 0.45

    # index des positions :
    # 0 = square
    # 1 = l droit
    # 2 = l gauche
    # 3 = t
    # 4 = barre vertical
    # 5 = barre horizontal

    POS_WALL_1 = [[0, 30], [0, 150], [0, 270], [0, 390], [0, 510], [0, 630]]
    POS_WALL_2 = [[1048, 30], [1048, 150], [1048, 270],
                  [1048, 390], [1048, 510], [1048, 630]]

    #middle : 540|360
    POS_PIECES = [[540, 310], [570, 330], [540, 360], [610, 360], [600, 360], [570, 390],
                  [520, 310], [490, 330], [500, 360], [440, 360], [460, 360], [490, 390]]

    def __init__(self):
        random.seed(time.time())
        pygame.init()
        self.window = pygame.display.set_mode(
            (self.WINDOW_LENGTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.network = Network(self.networkManager)

        self.objects = []
        self.objects.append(Player(Player.REAL, self.PLAYER1_NAME, self.PLAYER1_START_POS,
                                   self.PLAYER1_KEYS, self.PLAYER1_COLOR, self, self.network.sendDatagram))
        self.objects.append(Player(Player.REAL, self.PLAYER2_NAME, self.PLAYER2_START_POS,
                                   self.PLAYER2_KEYS, self.PLAYER2_COLOR, self, self.network.sendDatagram))
        # self.objects.append(Player(Player.NETWORK, self.PLAYER2_NAME, self.PLAYER2_START_POS,
        #                            None, self.PLAYER2_COLOR, self, None))
        # self.objects.append(Wall(self.window, self.POS_WALL_1))
        # self.objects.append(Wall(self.window, self.POS_WALL_2))

        # self.objects.append(Pieces(self.window, self.POS_PIECES))
        # self.objects.append(Piece("vertical", (200, 400), self))
        # self.objects.append(Piece("horizontal", (300, 400), self))
        # self.objects.append(Piece("square", (400, 400), self))
        # self.objects.append(Piece("t-shape", (500, 400), self))
        # self.objects.append(Piece("l-left", (600, 400), self))
        # self.objects.append(Piece("l-right", (700, 400), self))
        self.piecesName = []
        self.generatePieces()

    def networkManager(self, datagram):
        if (datagram[0] == '1'):
            self.getObjectsByType(Player)[1]

    def generateRandomPiecePosition(self):
        x = random.randint(self.WINDOW_LENGTH / 2 - (self.WINDOW_LENGTH * self.PIECE_SPAWN_RANGE_X_PERCENT),
                           self.WINDOW_LENGTH / 2 + (self.WINDOW_LENGTH * self.PIECE_SPAWN_RANGE_X_PERCENT))
        y = random.randint(self.WINDOW_HEIGHT / 2 - (self.WINDOW_HEIGHT * self.PIECE_SPAWN_RANGE_Y_PERCENT),
                           self.WINDOW_HEIGHT / 2 + (self.WINDOW_HEIGHT * self.PIECE_SPAWN_RANGE_Y_PERCENT))
        return (x, y)

    def generatePieces(self):
        for filename in os.listdir(os.getcwd() + "/assets/pieces"):
            self.piecesName.append(filename.split('.png')[0])

        for i in range(self.NUMBER_WALL_HOLE):
            name = self.piecesName[i]
            self.objects.append(
                Piece(name, self.generateRandomPiecePosition(), self))
            self.objects.append(
                Piece(name, self.generateRandomPiecePosition(), self))

        for i in range(self.NUMBER_PIECES - (self.NUMBER_WALL_HOLE * 2)):
            name = self.piecesName[random.randint(0, len(self.piecesName) - 1)]
            self.objects.append(
                Piece(name, self.generateRandomPiecePosition(), self))

    def eventManager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for object_ in self.objects:
                object_.eventManager(event)

    def update(self, dt):
        for object_ in self.objects:
            object_.update(dt)

    def getObjectsByType(self, type_):
        response = []

        for object_ in self.objects:
            if type(object_) == type_:
                response.append(object_)
        return response

    def gameloop(self):
        sound = pygame.mixer.Sound("assets/sound/flute.wav")
        sound.play(loops=-1, maxtime=0, fade_ms=0)
        while self.running:
            dt = self.clock.tick(self.FPS) / 1000
            self.window.fill((0, 0, 0))

            self.eventManager()
            self.update(dt)

            pygame.display.flip()
