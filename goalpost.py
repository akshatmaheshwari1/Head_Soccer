import pygame
from pygame.sprite import Sprite

class GoalPost(Sprite):
    def __init__(self, side):
        self.image = pygame.surface.Surface((64, 64*3))