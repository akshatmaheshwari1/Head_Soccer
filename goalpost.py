import pygame
from pygame.sprite import Sprite

class GoalPost(Sprite):
    def __init__(self, side):
        super().__init__()
        self.side = side
        if side == "left": #form the image of the goalpost based on what side
            self.image = pygame.surface.Surface((64, 64*2))
            self.image.blit(pygame.image.load("Assets/top.png"), (0,0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
        if side == "right":
            self.image = pygame.surface.Surface((64, 64 * 2))
            self.image.blit(pygame.image.load("Assets/top.png"), (0, 0))
            self.image.blit(pygame.image.load("Assets/middle.png"), (0, 64))
            self.image = pygame.transform.flip(self.image, True, False) #mirrors the image for the right side
        self.rect = self.image.get_rect()
        self.start_tick = 0 #clock starts ticking
        self.big = False


    def change_goal(self, tick): #changes the size of the goal by adding another image within the surface
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
        if self.big and tick - self.start_tick > 300:  #the goal is only big for 5 seconds
            if self.side == "left": #reverts back to original goalpost size
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
            self.big = False #sets the big variable to false



