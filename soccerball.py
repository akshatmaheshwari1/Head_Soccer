import pygame
from pygame.sprite import Sprite
from random import randint

class SoccerBall(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/ball.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.xmovement = 0
        self.ymovement = 7.58
        self.bounce_frame = 0
        self.move_rate_right = 0
        self.move_rate_left = 0

    def update(self):
        self.x += self.xmovement
        self.y += self.ymovement

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y < self.rect.height:
            self.ymovement *= -1
            self.bounce_frame = 0

        if self.x < self.rect.width or self.x > 1200 - self.rect.width:
            self.xmovement *= -1


        if self.y > 600 - self.rect.height:
            self.bounce_frame = randint(40,100)

        if self.bounce_frame > 0:
            self.ymovement = -2.58
            self.bounce_frame -=1

        if self.bounce_frame < 1:
            self.ymovement = 2.58

        if self.move_rate_right > 0:
            self.move_rate_right -=1
            self.xmovement -= 0.1

            if self.xmovement < 0:
                self.move_rate_right = 0

        if self.move_rate_left > 0:
            self.move_rate_left -=1
            self.xmovement += 0.1

            if self.xmovement > 0:
                self.move_rate_right = 0



