import pygame
import os
from os import path
pygame.mixer.init()

# Window 
SCREEN_WIDTH                = 600 
SCREEN_HEIGHT               = 1000
SCREEN_SIZE                 = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN                      = pygame.display.set_mode(SCREEN_SIZE) 

# Background
BACKGROUND_PIC              = "pics/background.png"
BACKGROUND_SIZE             = (600, 3000)
BACKGROUND_POS              = (SCREEN_WIDTH/2, 0)
BACKGROUND_POS2             = (SCREEN_WIDTH/2, -SCREEN_HEIGHT)

# Spaceships
SPACESHIP_START_POS         = (SCREEN_WIDTH/2, 900)
SPACESHIP_SIZE              = (30, 40)
SPACESHIP_PIC               = "pics/spaceship.png"
SPACESHIP_CTRL              = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
SPACESHIP_SLOW_DOWN_RATE    = 0.92

# Bullet
BULLET_SIZE                 = (20, 30)
BULLET_PIC                  = "pics/bullet.png"

# Font
WHITE                       = (255, 255, 255)
BLACK                       = (0, 0, 0)
ORANGE                      = (225, 106, 40)

# Asteroid
ASTEROID_MAX_SPEED          = 6
ASTEROID_MIN_SPEED          = 2
ASTEROID_MAX_SIZE           = 90
ASTEROID_MIN_SIZE           = 60
ASTEROID_MAX_ROTATION       = 20
ASTEROID_MIN_ROTATION       = 5

#Explosion

img_dir = path.join(path.dirname(__file__), "animation")

EXPLOSION_ANIMATION = {}
EXPLOSION_ANIMATION["standard"] = []

for i in range(9):
    filename = "explosion0{}.png".format(i)
    image = pygame.image.load(path.join(img_dir, filename)).convert()
    image.set_colorkey(BLACK)
    img_standard = pygame.transform.scale(image, (200, 200))
    EXPLOSION_ANIMATION["standard"].append(img_standard)

IMAGE = EXPLOSION_ANIMATION["standard"][0]