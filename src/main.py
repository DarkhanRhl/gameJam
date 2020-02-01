import pygame
from pygame.locals import *

 
def main():
     
    pygame.init()
     
    window = pygame.display.set_mode((920,680))
     
    background = pygame.image.load("assets/weiqi-cover.jpg").convert()
    window.blit(background, (0,0))
    pygame.display.flip()

    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     

if __name__=="__main__":
    main()