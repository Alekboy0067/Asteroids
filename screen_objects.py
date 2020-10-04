import pygame
import config as C 
from pygame import Vector2 as Vec

class screen_obj(pygame.sprite.Sprite):

    """
        Parent class for all objects on screen, 
        both static and dynamic objects. Needs a picture
        a size and position on screen. 
    """

    def __init__(self, picture, size, position):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.position = Vec(position)
        self.image = pygame.Surface([C.SCREEN_WIDTH, C.SCREEN_HEIGHT])
        self.image = pygame.image.load(picture)
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.rot_picture = self.image
        
