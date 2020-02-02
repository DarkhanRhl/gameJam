import pygame

SQUARE = "assets/pieces/carree_sans_bordure.png"
L_RIGHT = "assets/pieces/l_cote-droit_sans_bordure.png"
L_LEFT = "assets/pieces/l_cote-gauche_sans_bordure.png"
T = "assets/pieces/t_sans_bordure.png"
STRAIGHT_LINE = "assets/pieces/trait-droit_sans_bordure.png"
HORIZONTAL_LINE = "assets/pieces/trait-horizon_sans_bordure.png"

class Pieces:
    def __init__(self, window, pos):
        self.window = window
        self.pos = pos
        self.rect = []
        self.piecesSprite = []
        self.initSprite()
    
    def initSprite(self):
        i = 0
        while i < 2:
            self.piecesSprite.append(pygame.image.load(SQUARE).convert())
            self.piecesSprite.append(pygame.image.load(L_RIGHT).convert())
            self.piecesSprite.append(pygame.image.load(L_LEFT).convert())
            self.piecesSprite.append(pygame.image.load(T).convert())
            self.piecesSprite.append(pygame.image.load(STRAIGHT_LINE).convert())
            self.piecesSprite.append(pygame.image.load(HORIZONTAL_LINE).convert())
            i += 1
        # for pi in self.piecesSprite:
        #     self.rect.append(self.pi.get_rect())
        # self.image = pygame.Surface((32, 32))
        # self.image.fill((255, 255, 255))
        
    def update(self, dt):
        i = 0
        for pi in self.piecesSprite:
            self.window.blit(pi, self.pos[i])
            i += 1
    def eventManager(self, event):
        # if event.type == pygame.KEYDOWN:
        #     print("dans event manager")
        i = 0
        
