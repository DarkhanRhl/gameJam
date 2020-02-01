import pygame
from object import Object
from player import Player

class Toto(Object):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)

class Core:
    FPS = 60
    LENGTH = 1080
    HEIGHT = 720

    PLAYER1_KEYS = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "action": pygame.K_RETURN
    }

    PLAYER2_KEYS = {
        "up": pygame.K_z,
        "down": pygame.K_s,
        "left": pygame.K_q,
        "right": pygame.K_d,
        "action": pygame.K_SPACE
    }

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.LENGTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.objects = []
        self.objects.append(Player(self, self.PLAYER1_KEYS, "player 1", (255, 0, 0)))
        self.objects.append(Player(self, self.PLAYER2_KEYS, "player 2", (0, 0, 255)))
        self.objects.append(Toto("toto"))
        self.objects.append(Toto("tata"))

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
        while self.running:
            dt = self.clock.tick(self.FPS) / 1000
            self.window.fill((0, 0, 0))

            self.eventManager()
            self.update(dt)

            pygame.display.flip()