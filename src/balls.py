import pygame
import random
class Ball:

    #constructor de las pelotas
    def __init__(self, x, y, radius, speedx, speedy, color):
        
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speedx
        self.speed_y = speedy
        self.color = color    
    #agrega velocidad
    #checa colisiones
    def update_balls(self):
            
        self.x += self.speed_x
        self.y += self.speed_y
        #colisiones
        if self.y > 800 - self.radius or self.y < self.radius:
            self.speed_y *= -1
        if self.x > 1200 - self.radius or self.x < self.radius :
            self.speed_x *= -1
    #agrega el constructor de la pelota 50 veces
    def add_balls(self, balls):
        ball_count = 50
        for i in range (ball_count):
            self = Ball(random.randrange(70, 600), random.randrange(70, 450), random.randint(5, 60), random.randrange(-2, 3), 
                    random.randrange(-2, 3), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            balls.append(self)
    #dibuja la pelota
    def draw_ball(self, balls, screen):
        for self in balls:
                pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)