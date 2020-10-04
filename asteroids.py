import pygame
import config as C 
from pygame import Vector2 as Vec
from screen_objects import screen_obj

class asteroid(screen_obj):
    def __init__(self, picture, size, position, rotation_speed, speed):
        super().__init__(picture, size, position)

        self.rotation_speed = rotation_speed
        self.speed = Vec(speed)

    def update(self):
        
        self.rotation_speed += 5
        self.rotate(self.rotation_speed)
        self.position += self.speed
        self.rect.center = self.position

    def rotate(self, rotation_speed):

        center = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.rot_picture, rotation_speed)
        self.rect = self.image.get_rect(center = (self.rect.center))
