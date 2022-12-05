import pygame
from pygame.sprite import Sprite

class GoalPost(Sprite):
    def __init__(self, side):
        super().__init__()
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
        self.start_tick = 0
        self.big = False


    def change_goal(self, tick):
        self.start_tick = tick
        self.big = True
        if self.side == "right":
            self.image = pygame.surface.Surface((64, 64 * 3))
            self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 128))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = (1200 - 64, 600 - 192)
        if self.side == "left":
            self.image = pygame.surface.Surface((64, 64 * 3))
            self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 128))
            self.rect = (0, 600 - 192)


    def update(self,tick):
        if self.big and tick - self.start_tick > 300:
            if self.side == "left":
                self.image = pygame.surface.Surface((64, 64 * 2))
                self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
                self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
                self.rect = (0, 600 - 128)
            if self.side == "right":
                self.image = pygame.surface.Surface((64, 64 * 2))
                self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
                self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = (1200 - 64, 600 - 128)
            self.big = False



