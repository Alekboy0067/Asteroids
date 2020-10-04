import pygame
import config as C 
from screen_objects import screen_obj
from pygame import Vector2 as Vec

class background(screen_obj):

    def __init__(self, position):
        super().__init__(C.BACKGROUND_PIC, C.BACKGROUND_SIZE, position)

        self.position = position

    def update(self):
        # Background constantly scrolls downwards
        speed = Vec(0, 0.5)

        self.position += speed
        self.rect.center = self.position

        if self.position[1] > C.SCREEN_HEIGHT:
            self.position[1] = -C.SCREEN_HEIGHT