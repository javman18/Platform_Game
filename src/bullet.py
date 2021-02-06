import pygame
import math

class Bullet:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8*direction
    def draw_bullet(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)