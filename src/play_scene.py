import pygame
from Scene import Scene
from player import Player
from platfmorms import Platform
from bullet import Bullet
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')
        
        self.player = Player(pygame.Rect(50, 0, 30, 30))
        self.platform = Platform(pygame.Rect(0, 0,150, 30), (255,100,0), 2)        
        self.plat_list = [Platform(pygame.Rect(0, 200, 150, 30), (100,255,0), 1), Platform(pygame.Rect(200, 500, 150, 30), (255, 100, 0), 2), 
        Platform(pygame.Rect(450, 200, 150, 30), (100,255,0), 1), Platform(pygame.Rect(600, 350, 150, 30), (255, 100, 0), 2)]
        self.plat_count = 3
        self.bullets = []
        self.facing = 0
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                self.player.speed_x = -3
                self.player.left = True
                self.player.right = False
                self.player.idle = False
            elif event.key == pygame.K_RIGHT:
                self.player.speed_x = +3
                self.player.right = True
                self.player.left = False
                self.player.idle = False
                print(self.player.speed_x)
            elif event.key == pygame.K_SPACE:
                self.player.jump()
            elif event.key == pygame.K_q:
                if self.player.left:
                    facing = -1
                else:
                    facing = 1

                
                self.bullets.append(Bullet(round(self.player.rect.x), round(self.player.rect.y), 6, (0,0,0), facing))
            elif event.key == pygame.K_l:
                self.player.rect.x=50
                self.player.rect.y=0
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.speed_x = 0
            elif event.key == pygame.K_RIGHT:
                self.player.speed_x = 0
            
    
    def update(self):
        self.player.gravity()
        self.player.move()
        for bullet in self.bullets:
            if bullet.x < self.app.width and bullet.x>0:
                bullet.x += bullet.vel
            else:
                self.bullets.pop(self.bullets.index(bullet))
        #if self.player.isGrounded:
            #print ('grounded')

        self.player.collision(self.plat_list)

    
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.player.draw_player(self.screen)
        self.platform.draw_rect(self.screen, self.plat_list)
        for bullet in self.bullets:
            bullet.draw_bullet(self.screen)

        pygame.display.update()
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
