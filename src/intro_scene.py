from Scene import Scene
import pygame
import random
from balls import Ball

class IntroScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('IntroScene') 
        self.count_balls = 30
        self.ball_list=[]
        self.ball = Ball(random.randrange(40, 500), random.randrange(50, 400), random.randint(5, 60), random.randrange(-2, 3), 
            random.randrange(-2, 3), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
  
    def start(self):
        
        self.ball.add_balls(self.ball_list)
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')
            print('se presiono una tecla')

    def update(self):
        for ball in self.ball_list:
            ball.update_balls()
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        self.ball.draw_ball(self.ball_list, self.screen)

    def exit(self):
        print('termina: ', self.name)

    
    