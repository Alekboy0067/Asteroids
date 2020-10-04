import pygame 
import config as C
from screen_objects import screen_obj
from pygame import Vector2 as Vec
from bullet import bullet

class spaceship(screen_obj):

    def __init__(self, position):
        super().__init__(C.SPACESHIP_PIC, C.SPACESHIP_SIZE, position)

        self.position = position
        self.ctrl = C.SPACESHIP_CTRL
        self.bullets = []
        self.speed = Vec(0, 0)
        self.bullet_exist = False
        self.bullet = None

    def update(self):
        
        self.speed *= C.SPACESHIP_SLOW_DOWN_RATE
        key = pygame.key.get_pressed()
        count = 0
        # Left movement
        if key[self.ctrl[1]]:
            self.speed = Vec(-6, 0)
        # Right movemement
        if key[self.ctrl[2]]:
            self.speed = Vec(6, 0)
        
        if self.rect.centerx > (C.SCREEN_WIDTH-50):
            self.position[0] = C.SCREEN_WIDTH-50
        if self.rect.centerx < 50:
            self.position[0] = 50

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == C.SPACESHIP_CTRL[0] and len(self.bullets) < 1:
                    self.shoot()
                    
        for x in self.bullets:
            x.update()
            C.SCREEN.blit(x.image, x.position)
            if x.rect.centery < 0:
                self.bullets.remove(x)
                
        self.position += self.speed 
        self.rect.center = self.position
    
    def shoot(self):

        self.bullet = bullet(self.position)
        self.bullets.append(self.bullet)