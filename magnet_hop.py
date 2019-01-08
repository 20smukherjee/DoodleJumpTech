import pygame
import random
#import necessary modules

interface_x = 1080
interface_y = 1920
#define how large game will be

init()
interface = display.set_mode((interface_x, interface_y))
score = time.score()
display.set_caption('Magnet hop!')
 
class Magneteer:
    def __init__(self):      
        self.whatever = image.load('RBF.png')
        #add more states
        self.reset()
#defines graphical states during game       
 
    def reset(self):
        self.velocity_x = 0
        self.velocity_y = 0
        self.x_acceleration = .5
        self.y_acceleration = -1
        self.jump_vy = 20
        self.max_velocity_x = 3
        self.max_velocity_y = 20
 
        self.posx = (interface_x - self.width) / 2
        self.posy = (interface_y - self.height)
 #defines intial physics and positions to reset to
 
    def update(self,p):
        self.physics(p)
        self.side_control()
        self.move()
        self.show()
 
        self.posx += self.velocity_x
        self.posy -= self.velocity_y
 
        return (self.img, (self.posx, self.posy, self.width, self.height))
 
    def physics(self, game):
    #defines gravity and how velocity and position will change
        on = False
        defines variable for true and false
        for color, rect in game:
            x,y,w,h = rect
 
            #X range
            if self.posx + self.width / 2 > x and self.posx - self.width / 2 < x + w:
                #Y range
                if self.posy + self.height >= y and self.posy + self.height <= y + h:
 
                    if self.velocity_y < 0:
                        on = True
 
        if not on and not self.posy >= interface_y - self.height:
            self.velocity_y -= 0.5
        elif on:
            self.speed_y = self.jump_velocity
        else:
            self.posy = interface_y - self.height
            self.velocity_x = 0
            self.velocity_y = 0
            if self.posx != (interface_x - self.width) / 2:
                if self.posx > (interface_x - self.width) / 2:
                    self.posx = max((interface_x - self.width) / 2, self.posx - 6)
                else:
                    self.posx = min((interface_x - self.width) / 2, self.posx + 6)
           
            else:
                keys = key.get_pressed()
                if keys[K_SPACE]:
                    self.velocity_y = self.jump_speed
     def move(self):
     #Moves the character
         while True:
             for e in pygame.event.get():
                 if e.type == pygame.QUIT:
                     sys.exit()
                 if e.type == pygame.KEYDOWN:
                     if pygame.key.name(e.key) == 'up':
                         self.velocity_y -= self.acceleration_y
                     if pygame.key.name(e.key) == 'left':
                             self.velocity_x -= self.acceleration_x
                     if pygame.key.name(e.key) == 'right':
                              self.velocity_x += self.acceleration_x
         
