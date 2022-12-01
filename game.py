import pygame
from settings import Settings
import sys
import time
from player import Player
from soccerball import SoccerBall
from goalpost import GoalPost
from random import randint

class HeadSoccer:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        #initialize the screen and get variables for width and height
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200,600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #upload assets
        self.grass_tile = pygame.image.load('Assets/grass_tile.png')
        self.grass_rect = self.grass_tile.get_rect()
        self.sky_tile = pygame.image.load('Assets/sky_tile.png')
        self.sky_rect = self.sky_tile.get_rect()

        #draw background
        self.draw_background()

        #draw player1
        self.player1 = Player(1, pygame.image.load('Assets/player1.png'))
        self.player1.x = 200
        self.player1.y = 600 - self.player1.rect.height

        #draw player2
        self.player2 = Player(2, pygame.image.load('Assets/player2.png'))
        self.player2.x = 1000
        self.player2.y = 600 - self.player2.rect.height

        #draw ball
        self.ball = SoccerBall()
        self.ball.x = 600
        self.ball.y = 100

        #draw goalpost
        self.goalpost1 = GoalPost("left")
        self.goalpost1.rect = (0, 600-128)
        self.goalpost2 = GoalPost("right")
        self.goalpost2.rect = (1200-64, 600 - 128)

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            self.player1.update()
            self.player2.update()
            self.ball.update()
            self.update_screen()
            self.check_collision_with_player()
            self.check_collision_with_goalpost()
            self.check_goal()

        clock.tick(60)
    def draw_background(self):
        for x in range(self.settings.screen_width//self.grass_rect.width + 1):
            for y in range(int(self.settings.screen_height // self.grass_rect.height * (1/3) + 1)):
                self.screen.blit(self.grass_tile, (x*self.grass_rect.width, self.settings.screen_height - (y+1) * self.grass_rect.height))

        for x in range(self.settings.screen_width // self.sky_rect.width + 1):
            for y in range(int(self.settings.screen_height // self.sky_rect.height * (2 / 3) + 1)):
                self.screen.blit(self.sky_tile, (x * self.sky_rect.width, y * self.sky_rect.height))

    def update_screen(self):
        self.draw_background()
        self.screen.blit(self.player1.image, self.player1.rect)
        self.screen.blit(self.player2.image, self.player2.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
        self.screen.blit(self.goalpost1.image, self.goalpost1.rect)
        self.screen.blit(self.goalpost2.image, self.goalpost2.rect)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #player1
                if event.key == pygame.K_RIGHT:
                    self.player1.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player1.moving_left = True
                if event.key == pygame.K_UP:
                    self.player1.jumping_frame = 80
                    self.player1.jump_count +=1
                #player2
                if event.key == pygame.K_d:
                    self.player2.moving_right = True
                if event.key == pygame.K_a:
                    self.player2.moving_left = True
                if event.key == pygame.K_w:
                    self.player2.jumping_frame = 80
                    self.player2.jump_count +=1
            elif event.type == pygame.KEYUP:
                self.player1.moving_right = False
                self.player1.moving_left = False
                self.player2.moving_right = False
                self.player2.moving_left = False

    def check_collision_with_player(self):
        if self.ball.rect.collidepoint(self.player1.rect.midright) or self.ball.rect.collidepoint(self.player1.rect.bottomright) or self.ball.rect.collidepoint(self.player1.rect.topright):
            self.ball.xmovement = 0.5
            self.ball.move_rate_right = 300
        elif self.ball.rect.collidepoint(self.player1.rect.midtop):
            self.ball.bounce_frame = 1500
        elif self.ball.rect.collidepoint(self.player1.rect.midleft) or self.ball.rect.collidepoint(self.player1.rect.topleft) or self.ball.rect.collidepoint(self.player1.rect.bottomleft) :
            self.ball.xmovement = -0.5
            self.ball.move_rate_left = 300

        if self.ball.rect.collidepoint(self.player2.rect.midright) or self.ball.rect.collidepoint(self.player2.rect.bottomright) or self.ball.rect.collidepoint(self.player2.rect.topright):
            self.ball.xmovement = 0.5
            self.ball.move_rate_right = 300
        elif self.ball.rect.collidepoint(self.player2.rect.midtop):
            self.ball.bounce_frame = 1500
        elif self.ball.rect.collidepoint(self.player2.rect.midleft) or self.ball.rect.collidepoint(self.player2.rect.topleft) or self.ball.rect.collidepoint(self.player2.rect.bottomleft) :
            self.ball.xmovement = -0.5
            self.ball.move_rate_left = 300

    def check_collision_with_goalpost(self):
        if self.ball.rect.x < 64 and self.ball.rect.y > 460:
            self.ball.bounce_frame = randint(150,400)
        if self.ball.rect.x > 1136 and self.ball.rect.y > 460:
            self.ball.bounce_frame = randint(150,400)

    def check_goal(self):
        if self.ball.rect.x < 64 and self.ball.rect.y > 480 and self.ball.rect.y < 600:
            print("GOAAAL!")
            self.reset_game()

        if self.ball.rect.x >1136 and self.ball.rect.y > 480 and self.ball.rect.y < 600:
            print("GOAAAL!")
            self.reset_game()
    def reset_game(self):
        self.ball.x = 600
        self.ball.y = 100
        self.player1.x = 200
        self.player1.y = 600 - self.player1.rect.height
        self.player2.x = 1000
        self.player2.y = 600 - self.player2.rect.height

if __name__ == "__main__":
    headsoccer = HeadSoccer()
    headsoccer.run_game()
