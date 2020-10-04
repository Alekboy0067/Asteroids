import pygame
import random
import config as C 

from background import background
from spaceship  import spaceship
from bullet     import bullet
from asteroids  import asteroid
from explosion  import Explosion

class Game(pygame.sprite.Sprite):
    """
    Main game class
    """

    def __init__(self):
        pygame.init()     
        pygame.font.init()                                               

        self.font       = pygame.font.Font('freesansbold.ttf', 16) 
        self.background = background(C.BACKGROUND_POS)
        self.background2 = background(C.BACKGROUND_POS2)
        self.spaceship = spaceship(C.SPACESHIP_START_POS)
        self.group = pygame.sprite.Group(self.background, self.background2, self.spaceship)
        self.asteroids = pygame.sprite.Group()
        self.score = 0

    def run(self):

        running = True
        time = pygame.time.Clock()
        frame_rate = 60
        count = 0
        while running:

            time.tick(frame_rate)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                   
                    running = False

            key = pygame.key.get_pressed()                      

            if key[pygame.K_ESCAPE]:                           
                running = False
            # Spawn random asteroid for every 10 score
            if count % 25 == 0:
                tmp = self.random_asteroid()
                self.group.add(tmp)
                self.asteroids.add(tmp)
            # If asteroid falls out of screen, remove it
            for asteroid in self.group:
                if asteroid.position[1] > (C.SCREEN_HEIGHT+60):
                    self.group.remove(asteroid)
                    self.asteroids.remove(asteroid)
            # Draw all objects to screen
            self.group.draw(C.SCREEN)   
            # Update all objects on screen                        
            self.group.update() 
            self.asteroids.update()  
            # Score 
            self.score_text(running)
            for asteroid in self.asteroids:
                self.destroy_asteroid(asteroid)
            # Increment count
            count += 1
            # Add 1 score for each 10 count
            if count % 10 == 0:
                self.score += 1

            pygame.display.flip()
        pygame.quit()

    def score_text(self, running):

        score = self.font.render("Score: " + str(self.score), running, C.ORANGE, C.BLACK)
        score_area = score.get_rect()
        score_area.center = (40, 980)
        C.SCREEN.blit(score, score_area)

    def random_asteroid(self):

        size = (random.randint(C.ASTEROID_MIN_SIZE, C.ASTEROID_MAX_SIZE), random.randint(C.ASTEROID_MIN_SIZE, C.ASTEROID_MAX_SIZE))
        position = (random.randint(20, (C.SCREEN_WIDTH-20)), -40)
        rotation_speed = random.randint(C.ASTEROID_MIN_ROTATION, C.ASTEROID_MAX_ROTATION)
        speed = (0, random.randint(C.ASTEROID_MIN_SPEED, C.ASTEROID_MAX_SPEED))

        asteroid_ = asteroid("pics/asteroid.png", size, position, rotation_speed, speed)

        return asteroid_

    def destroy_asteroid(self, asteroid):

        for bullet in self.spaceship.bullets:
            if pygame.sprite.collide_rect(bullet, asteroid):
                self.spaceship.bullets.remove(bullet)
                self.group.remove(asteroid)
                self.asteroids.remove(asteroid)
                explosion = Explosion(self.spaceship.bullet.rect.center) 
                self.group.add(explosion)

                