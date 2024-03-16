import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("../New Piskel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 50])
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect[1] -= 3
        elif keys[pygame.K_s]:
            self.rect[1] += 3
        elif keys[pygame.K_a]:
            self.rect[0] -= 3
        elif keys[pygame.K_d]:
            self.rect[0] += 3
