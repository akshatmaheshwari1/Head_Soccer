import pygame
import sys
import time
from player import Player
from soccerball import SoccerBall
from goalpost import GoalPost
from random import randint
from powerup import Powerup
from pygame import mixer


class HeadSoccer:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

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

        #draw powerup
        self.powerup = Powerup()
        self.powerup.y = -100
        self.powerup.x = randint(100,1100)

        #fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.player1score = 0
        self.player2score = 0

        self.white = (255, 255, 255)
        self.black = (0,0,0)

        #set score to the textboxes
        self.player1text = self.font.render(str(self.player1score), True, self.white)
        self.player1text_rect = self.player1text.get_rect()
        self.player1text_rect.center = (50, 50)

        self.player2text = self.font.render(str(self.player2score), True, self.white)
        self.player2text_rect = self.player2text.get_rect()
        self.player2text_rect.center = (1150, 50)

        self.endgame = False

        #sounds
        mixer.init()
        mixer.music.set_volume(0.7)
        mixer.music.load("Assets/waka.wav")
        mixer.music.play(-1)
    def run_game(self):
        clock = pygame.time.Clock()
        tick = 0
        while True:
            while not self.endgame:
                self._check_events()
                self.player1.update()
                self.player2.update()
                self.ball.update()
                self.update_screen()
                self.check_collision_with_player()
                self.check_collision_with_goalpost()
                self.check_goal()
                self.powerup.update()
                self.check_powerup(tick)
                self.goalpost2.update(tick)
                self.goalpost1.update(tick)
                clock.tick(60)
                tick+=1
                if self.player1score == 5 or self.player2score == 5:
                    self.endgame = True
            #this only runs once a player wins
            clock.tick(60)
            self.draw_second_background()
            self.display_winner()
            time.sleep(3)
            sys.exit()

    def draw_background(self):
        #draw the grass
        for x in range(self.screen_width//self.grass_rect.width + 1):
            for y in range(int(self.screen_height // self.grass_rect.height * (1/3) + 1)):
                self.screen.blit(self.grass_tile, (x*self.grass_rect.width, self.screen_height - (y+1) * self.grass_rect.height))
        #draw the sky
        for x in range(self.screen_width // self.sky_rect.width + 1):
            for y in range(int(self.screen_height // self.sky_rect.height * (2 / 3) + 1)):
                self.screen.blit(self.sky_tile, (x * self.sky_rect.width, y * self.sky_rect.height))


    def update_screen(self):
        #make the backgrounds and blit game objects
        self.draw_background()
        self.screen.blit(self.player1.image, self.player1.rect)
        self.screen.blit(self.player2.image, self.player2.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
        self.screen.blit(self.goalpost1.image, self.goalpost1.rect)
        self.screen.blit(self.goalpost2.image, self.goalpost2.rect)
        self.screen.blit(self.powerup.image, self.powerup.rect)
        self.screen.blit(self.player1text, self.player1text_rect)
        self.screen.blit(self.player2text, self.player2text_rect)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #player1
                if event.key == pygame.K_w: #up
                    self.player1.jumping_frame = 20
                    self.player1.jump_count +=1
                if event.key == pygame.K_d: #right
                    self.player1.moving_right = True
                if event.key == pygame.K_a: #left
                    self.player1.moving_left = True
                #player2
                if event.key == pygame.K_UP: #up
                    self.player2.jumping_frame = 20
                    self.player2.jump_count +=1
                if event.key == pygame.K_RIGHT: #right
                    self.player2.moving_right = True
                if event.key == pygame.K_LEFT: #left
                    self.player2.moving_left = True
                #escape key
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYUP: #if not pressing any buttons
                self.player1.moving_right = False
                self.player1.moving_left = False
                self.player2.moving_right = False
                self.player2.moving_left = False

    def check_collision_with_player(self):
        if self.ball.rect.colliderect(self.player1.rect):
            if abs(self.ball.rect.left - self.player1.rect.right) < 15: #collision with right side of player
                self.ball.xmovement = abs(self.ball.xmovement)
                self.ball.xmovement += 2
                self.ball.move_rate_right = 20
            if abs(self.ball.rect.bottom - self.player1.rect.top) < 10: #collision with top of player
                self.ball.bounce_frame = randint(100, 200)
            if abs(self.ball.rect.right - self.player1.rect.left) < 15: #collision with left side of player
                self.ball.xmovement = - abs(self.ball.xmovement)
                self.ball.xmovement += -2
                self.ball.move_rate_left = 20
            if abs(self.ball.rect.top - self.player1.rect.bottom) < 10: #collision with bottom side of player
                self.ball.ymovement *= -1
        if self.ball.rect.colliderect(self.player2.rect): #same code for player 2
            if abs(self.ball.rect.left - self.player2.rect.right) < 15:
                self.ball.xmovement = abs(self.ball.xmovement)
                self.ball.xmovement += 2
                self.ball.move_rate_right = 20
            if abs(self.ball.rect.bottom - self.player2.rect.top) < 10:
                self.ball.bounce_frame = randint(100, 200)
            if abs(self.ball.rect.right - self.player2.rect.left) < 15:
                self.ball.xmovement = - abs(self.ball.xmovement)
                self.ball.xmovement += -2
                self.ball.move_rate_left = 20
            if abs(self.ball.rect.top - self.player2.rect.bottom) < 10:
                self.ball.ymovement *= -1

    def check_collision_with_goalpost(self):
        if self.goalpost2.big: #settings to bounce off bigger goalpost
            if self.ball.rect.x > 1136 and self.ball.rect.y > 400:
                self.ball.bounce_frame = randint(30, 100)
        if self.goalpost1.big:
            if self.ball.rect.x < 64 and self.ball.rect.y > 400:
                self.ball.bounce_frame = randint(30, 100)

        if self.ball.rect.x < 64 and self.ball.rect.y > 460: #settings to bounce off normal size goalpost
            self.ball.bounce_frame = randint(30,100)
        if self.ball.rect.x > 1136 and self.ball.rect.y > 460:
            self.ball.bounce_frame = randint(30,100)

    def check_goal(self):
        if self.goalpost2.big: #settings to check if ball scored in big goal
            if self.ball.rect.x > 1136 and self.ball.rect.y > 410 and self.ball.rect.y < 600:
                mixer.music.pause()
                mixer.Sound.play(mixer.Sound("Assets/goal.wav"))
                mixer.music.unpause()
                self.player1score +=1
                self.reset_game()
        if self.goalpost1.big:
            if self.ball.rect.x < 64 and self.ball.rect.y > 410 and self.ball.rect.y < 600:
                mixer.music.pause()
                mixer.Sound.play(mixer.Sound("Assets/goal.wav"))
                mixer.music.unpause()
                self.reset_game()
                self.player2score += 1
        if self.ball.rect.x < 64 and self.ball.rect.y > 480 and self.ball.rect.y < 600: #settings to check if ball scored in normal goal
            mixer.music.pause()
            mixer.Sound.play(mixer.Sound("Assets/goal.wav"))
            mixer.music.unpause()
            self.reset_game()
            self.player2score += 1

        if self.ball.rect.x >1136 and self.ball.rect.y > 480 and self.ball.rect.y < 600:
            mixer.music.pause()
            mixer.Sound.play(mixer.Sound("Assets/goal.wav"))
            mixer.music.unpause()
            self.reset_game()
            self.player1score += 1

        self.player1text = self.font.render(str(self.player1score), True, self.white) #update the score texts
        self.player2text = self.font.render(str(self.player2score), True, self.white)
    def reset_game(self):
        self.ball.x = 600
        self.ball.y = 100
        self.player1.x = 200
        self.player1.y = 600 - self.player1.rect.height
        self.player2.x = 1000
        self.player2.y = 600 - self.player2.rect.height
        self.ball.xmovement = 0

    def check_powerup(self, tick):
        if self.powerup.rect.colliderect(self.player1.rect): #if the player hits the powerup, the other goalpost gets bigger
            print("Oh no!")
            self.goalpost2.change_goal(tick)
            self.powerup.y = -6000 #repositions the powerup
            self.powerup.x = randint(100,1100)

        if self.powerup.rect.colliderect(self.player2.rect):
            print("Oh no!")
            self.goalpost1.change_goal(tick)
            self.powerup.y = -6000
            self.powerup.x = randint(100, 1100)
    def draw_second_background(self): #background for game over display
        for x in range(self.screen_width // self.sky_rect.width + 1):
            for y in range(int(self.screen_height // self.sky_rect.height + 1)):
                self.screen.blit(self.sky_tile, (x * self.sky_rect.width, y * self.sky_rect.height))

    def display_winner(self): #displays which player wins in the center of the screen
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        if self.player1score == 5:
            self.wintext = self.font.render("Player 1 Wins!", True, self.white)
        else:
            self.wintext = self.font.render("Player 2 Wins!", True, self.white)
        self.wintext_rect = self.player1text.get_rect()
        self.wintext_rect.center = (250, 300)
        self.screen.blit(self.wintext, self.wintext_rect)
        pygame.display.flip()

if __name__ == "__main__":
    headsoccer = HeadSoccer()
    headsoccer.run_game()
