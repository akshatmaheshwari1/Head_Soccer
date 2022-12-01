import pygame
from pygame.sprite import Sprite

class Powerup(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/powerup.png')
