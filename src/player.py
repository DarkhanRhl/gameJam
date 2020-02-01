import pygame

class Player:
    SPEED = 200

    def __init__(self, window):
        self.window = window

        self.velocity = [0, 0]
        self.initSprite()

    def initSprite(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, dt):
        move = [v * self.SPEED * dt for v in self.velocity]
        self.rect.move_ip(*move)
        self.window.blit(self.image, self.rect)

    def eventManager(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.velocity[1] += -1
            if event.key == pygame.K_DOWN:
                self.velocity[1] += 1
            if event.key == pygame.K_LEFT:
                self.velocity[0] += -1
            if event.key == pygame.K_RIGHT:
                self.velocity[0] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.velocity[1] -= -1
            if event.key == pygame.K_DOWN:
                self.velocity[1] -= 1
            if event.key == pygame.K_LEFT:
                self.velocity[0] -= -1
            if event.key == pygame.K_RIGHT:
                self.velocity[0] -= 1

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((32, 32))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
#         self.velocity = [0, 0]

#     def update(self):
#         self.rect.move_ip(*self.velocity)


# player = Player()
# running = True
# while running:
#     dt = clock.tick(FPS) / 1000
#     window.fill(BLACK)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:
#                 player.velocity[1] = -200 * dt
#             elif event.key == pygame.K_s:
#                 player.velocity[1] = 200 * dt
#             elif event.key == pygame.K_a:
#                 player.velocity[0] = -200 * dt
#             elif event.key == pygame.K_d:
#                 player.velocity[0] = 200 * dt
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_w or event.key == pygame.K_s:
#                 player.velocity[1] = 0
#             elif event.key == pygame.K_a or event.key == pygame.K_d:
#                 player.velocity[0] = 0

#     player.update()

#     window.blit(player.image, player.rect)
#     pygame.display.update()  # Or pygame.display.flip()

# print("Exited the game loop. Game will quit...")
# quit()  # Not actually necessary since the script will exit anyway.