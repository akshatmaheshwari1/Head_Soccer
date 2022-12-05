import pygame
from pygame.sprite import Sprite
from goalpost import GoalPost

class Powerup(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/powerup.png')
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self):
        self.y += 3
        self.rect.y = self.y
        self.rect.x = self.x

        if self.y >= 600:
            self.y = -3000


