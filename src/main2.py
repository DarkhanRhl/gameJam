import pygame

pygame.init()

ecran = pygame.display.set_mode((1920, 1080))
image = pygame.image.load("image.png").convert_alpha()

continuer = True
ecran.blit(image, (0, 50))
pygame.display.flip()

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()