import pygame
import random
class Platform:
    def __init__(self, rect, color, _type):
        self.rect = rect
        self.color = color
        self._type = _type

    def draw_rect(self, screen, plats):
        for self in plats:
            pygame.draw.rect(screen, self.color, self.rect)

    
            

