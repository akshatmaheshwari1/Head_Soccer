import pygame
from settings import Settings
import sys
import time
from player import Player

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

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            self.player1.update()
            self.update_screen()

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
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player1.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player1.moving_left = True
                if event.key == pygame.K_UP:
                    self.player1.jumping_frame = 80
                    self.player1.jump_count +=1
            elif event.type == pygame.KEYUP:
                self.player1.moving_right = False
                self.player1.moving_left = False


if __name__ == "__main__":
    headsoccer = HeadSoccer()
    headsoccer.run_game()
