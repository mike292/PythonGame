import time
import random
import os
import pygame
pygame.font.init()

WIDTH, HEIGHT = 750, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader")

#Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_ship_blue_small.png"))

#Player Image Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_ship_yellow.png"))

#Lasers
RED_LASER = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("spaceInvaders/assets", "pixel_laser_yellow.png"))

#Background
BGIMAGE = pygame.image.load(os.path.join("spaceInvaders/assets", "background-black.png"))
BG = pygame.transform.scale(BGIMAGE, (WIDTH,HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        # pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50), 2)
        window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comisans", 50)
    player_vel = 5

    player = Player(300, 500)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw Text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update() #Refresh display

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: #Left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel < WIDTH: #Right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: #Up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel < HEIGHT: #Down
            player.y += player_vel
main()