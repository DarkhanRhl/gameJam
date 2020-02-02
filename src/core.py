import pygame
from player import Player
from wall import Wall

class Core:
    FPS = 60
    LENGTH = 1080
    HEIGHT = 720

    PLAYER1_KEYS = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT
    }

    PLAYER2_KEYS = {
        "up": pygame.K_z,
        "down": pygame.K_s,
        "left": pygame.K_q,
        "right": pygame.K_d
    }

    POS_WALL_1 = [[0,30], [0, 150], [0, 270], [0, 390], [0, 510], [0, 630]]
    POS_WALL_2 = [[1048 ,30], [1048, 150], [1048, 270], [1048, 390], [1048, 510], [1048, 630]]

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.LENGTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.objects = []
        self.objects.append(Player(self.window, self.PLAYER1_KEYS))
        self.objects.append(Player(self.window, self.PLAYER2_KEYS))
        self.objects.append(Wall(self.window, self.POS_WALL_1))
        self.objects.append(Wall(self.window, self.POS_WALL_2))


    def eventManager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for object_ in self.objects:
                object_.eventManager(event)

    def update(self, dt):
        for object_ in self.objects:
            object_.update(dt)

    def gameloop(self):
        sound = pygame.mixer.Sound("assets/sound/flute.wav")
        sound.play(loops=-1, maxtime=0, fade_ms=0)
        while self.running:
            dt = self.clock.tick(self.FPS) / 1000
            self.window.fill((0, 0, 0))

            self.eventManager()
            self.update(dt)

            pygame.display.flip()