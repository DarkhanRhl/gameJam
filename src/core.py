import pygame
from player import Player

class Core:
    FPS = 60
    LENGTH = 1080
    HEIGHT = 720

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.LENGTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player1 = Player(self.window)

    def gameloop(self):
        while self.running:
            dt = self.clock.tick(self.FPS) / 1000
            self.window.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.player1.eventManager(event)
            
            self.player1.update(dt)
            pygame.display.flip()