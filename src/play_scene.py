import pygame
from Scene import Scene
from player import Player
from platfmorms import Platform
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')
        
        
        self.player = Player(pygame.Rect(self.app.width/2, 0, 30, 30))
        self.platform = Platform(pygame.Rect(0, 0,150, 30), (255,100,0))        
        self.plat_list = [Platform(pygame.Rect(300, 450, 150, 30), (100,255,0)), Platform(pygame.Rect(400, 300, 150, 30), (255, 100, 0)), 
        Platform(pygame.Rect(200, 200, 150, 30), (100,255,0))]
        self.plat_count = 3

    def start(self):
        self.platform.add_platform(self.plat_list)
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                self.player.speed_x = -3
                print(self.player.speed_x)
            elif event.key == pygame.K_RIGHT:
                self.player.speed_x = +3
                print(self.player.speed_x)
            elif event.key == pygame.K_SPACE:
                self.player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.speed_x = 0
            elif event.key == pygame.K_RIGHT:
                self.player.speed_x = 0
            
    
    def update(self):
        self.player.gravity()
        self.player.move()
        #if self.player.isGrounded:
            #print ('grounded')

        self.player.collision(self.plat_list)
        #self.player.jump()
        #for platform in self.plat_list:
#
        #    if self.player.collision(platform):
        #        self.player.rect.y = self.platform.rect.y - self.player.radius
        #        self.player.speed_y = 0
        #        self.player.isFalling = False
        #    else:
        #        self.player.isFalling = True
    
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.player.draw_player(self.screen)
        self.platform.draw_rect(self.screen, self.plat_list)
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
