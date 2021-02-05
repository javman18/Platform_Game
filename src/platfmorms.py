import pygame
import random
class Platform:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw_rect(self, screen, plats):
        for self in plats:
            pygame.draw.rect(screen, self.color, self.rect)

    def add_platform(self,plats):
        
        plats = [Platform(pygame.Rect(760, 450, 150, 30), self.color), Platform(pygame.Rect(400, 300, 150, 30), self.color)]
            
            

