import pygame

class Wall:
    def __init__(self, window, pos):
        self.window = window
        self.wallParts = []
        self.pos = pos
        self.initSprite()
        self.initWallPart()
    
    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
    
    def initWallPart(self):
        self.wallParts.append(self.image.get_rect())
        self.wallParts.append(self.image.get_rect())
        self.wallParts.append(self.image.get_rect())
        self.wallParts.append(self.image.get_rect())
        self.wallParts.append(self.image.get_rect())
        self.wallParts.append(self.image.get_rect())

        self.wallParts[0].move_ip(self.pos[0])
        self.wallParts[1].move_ip(self.pos[1])
        self.wallParts[2].move_ip(self.pos[2])
        self.wallParts[3].move_ip(self.pos[3])
        self.wallParts[4].move_ip(self.pos[4])
        self.wallParts[5].move_ip(self.pos[5])

    def update(self, dt):
        for w in self.wallParts:
            self.window.blit(self.image, w)
    def eventManager(self, event):
        if event.type == pygame.KEYDOWN:
            print("dans event manager")
        
