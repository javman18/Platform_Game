
import pygame
from platfmorms import Platform
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,rect):  #(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
         
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 20
        self.isJump = False
        self.jumpCount = 10
        self.isGrounded = False
        self.isFalling = True 
        self.idle = True
        self.left = False
        self.right = False 
        #player_img = pygame.image.load('tile046.png')      
        
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        print(self.speed_y)
        if self.speed_x < 0:
            print("left")
            self.left = True
        elif self.speed_x > 0:
            print("right")
            self.right=True
        elif self.speed_x == 0:
            print ("idle")
            self.idle = True
        if self.rect.x > 800 - self.radius:
            self.rect.x = 800 - self.radius
        elif self.rect.x < self.radius:
            self.rect.x = self.radius
        

    def draw_player(self, screen):
        pygame.draw.circle(screen, (0,0,255), (self.rect.x, self.rect.y), self.radius)
        #screen.blit(player_img(self.rect.x, self.rect.y))
        #pygame.display.update()


    def gravity(self):
        
        if self.isFalling:
            self.speed_y += 0.5
            self.isGrounded=False
        '''   
        if self.speed_y<0.5:
            print('isJumping')
        if self.speed_y>0.5:
            print('isFalling')
        #print(self.speed_y) 
        if(self.speed_y==0.5):
            print('isGrounded')
        '''

        if self.speed_y==0:
            self.isFalling=False

        if self.rect.y >= 600 - self.radius - 50 and self.speed_y>=0:
            
            self.speed_y = 0
            self.rect.y = 600 - self.radius - 50
            self.isGrounded = True
            self.isFalling = False        

    def jump(self):
        jump_vel = 12
        if self.isGrounded:
            
            self.speed_y -= jump_vel
            self.isJump = True
            
            
            

    def collision(self, plats):
        #return (pygame.Rect(self.rect.x, self.rect.y + self.radius, self.radius, self.radius).colliderect(platform.rect))
        for platform in plats:

            #colisiones de abajo
            if(self.rect.x + self.radius  > platform.rect.x and self.rect.x < platform.rect.x + platform.rect.width
            and self.rect.y < platform.rect.y + platform.rect.height + self.radius and self.rect.y > platform.rect.y+30):
                self.rect.y = platform.rect.y + self.radius + 30
                self.speed_y = 0
            #colisiones de arriba
            if (self.rect.x + self.radius  >= platform.rect.x and self.rect.x - self.radius <= platform.rect.x + platform.rect.width 
            and self.rect.y + self.radius >= platform.rect.y -5 and self.rect.y + self.radius <= platform.rect.y + 30):
                
                self.rect.y = platform.rect.y - self.radius 
                self.speed_y = 0
                
                self.isGrounded = True
                self.isFalling=False
            else:
                self.isFalling=True

            #if(self.x + self.radius > self.platform.x and self.x + self.radius < self.platform.x + 10
            #and self.y + self.radius > self.platform.y - 5 and self.y < self.platform.y + 30):
            #    self.y = self.platform.y - self.radius
            #    self.speed_y = 0
            #if (self.x + self.radius > self.platform.x and self.x - self.radius < self.platform.x + self.platform.width 
            #and self.y + self.radius > self.platform.y - 5 and self.y - self.radius < self.platform.y + 30):
            #    self.y = self.platform.y - self.radius
            #    print('col')
            #    self.speed_y = 0
            #    self.isGrounded = True
            #    self.isFalling=False
            #else:
            #    self.isFalling=True
        
        
            
