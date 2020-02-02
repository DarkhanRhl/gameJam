import pygame

SQUARE = "assets/pieces/carree_sans_bordure.png"
L_RIGHT = "assets/pieces/l_cote-droit_sans_bordure.png"
L_LEFT = "assets/pieces/l_cote-gauche_sans_bordure.png"
T = "assets/pieces/t_sans_bordure.png"
STRAIGHT_LINE = "assets/pieces/trait-droit_sans_bordure.png"
HORIZONTAL_LINE = "assets/pieces/trait-horizon_sans_bordure.png"

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
        self.wallParts.append(pygame.image.load(SQUARE).convert())
        self.wallParts.append(pygame.image.load(L_RIGHT).convert())
        self.wallParts.append(pygame.image.load(L_LEFT).convert())
        self.wallParts.append(pygame.image.load(T).convert())
        self.wallParts.append(pygame.image.load(STRAIGHT_LINE).convert())
        self.wallParts.append(pygame.image.load(HORIZONTAL_LINE).convert())

        # self.wallParts[0].move_ip(self.pos[0])
        # self.wallParts[1].move_ip(self.pos[1])
        # self.wallParts[2].move_ip(self.pos[2])
        # self.wallParts[3].move_ip(self.pos[3])
        # self.wallParts[4].move_ip(self.pos[4])
        # self.wallParts[5].move_ip(self.pos[5])

    def update(self, dt):
        i = 0
        for pi in self.wallParts:
            self.window.blit(pi, self.pos[i])
            i += 1
    def eventManager(self, event):
        # if event.type == pygame.KEYDOWN:
        #     print("dans event manager")
        i = 0
        
