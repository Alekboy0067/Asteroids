import pygame 
import config as C
from screen_objects import screen_obj
from pygame import Vector2 as Vec

class bullet(screen_obj):

    def __init__(self, position):
        super().__init__(C.BULLET_PIC, C.BULLET_SIZE, position)

        self.position = Vec(position)
        self.speed = Vec(0, -20)

    def update(self):
        
        self.position += self.speed
        self.rect.center = self.position
        
        
