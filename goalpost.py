import pygame
from pygame.sprite import Sprite

class GoalPost(Sprite):
    def __init__(self, side):
        self.side = side
        if side == "left":
            self.image = pygame.surface.Surface((64, 64*2))
            self.image.blit(pygame.image.load("Assets/top.png"), (0,0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
        if side == "right":
            self.image = pygame.surface.Surface((64, 64 * 2))
            self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()



