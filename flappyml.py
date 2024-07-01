import pygame
import neat
import time
import random
import os

WIN_WIDTH = 500
WIN_HEIGHT = 800

#loading images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 #bird tilt
    ROT_VEL = 20 #rot/frame
    ANIMATION_TIME = 5 #how long to show each animation

    def __init__(self, x, y):
        #starting posns
        self.x = x 
        self.y = y
        self.tilt = 0 #how tilted at the start
        self.tick_count = 0 #
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
    def jump(self):
        self.vel = -10.5 #moving upwards toward y = 0
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1 #a frame went by, we moved
        
        d = self.vel * self.tick_count + 1.5 * self.tick_count**2

        if d >= 16:
            d = 16
        if d < 0:
            d -= 2 #if we're moving upwards, move up a bit more to make the jump a bit nicer
        
        self.y = self.y + d #move slowly up or slowly down

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
        
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1] #should look like it's nosediving
            self.img_count = self.ANIMATION_TIME*2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    

def draw_window(win, bird):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)
        # keep track of something the user does like click the mous
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        draw_window(win, bird)
    
    pygame.quit()
    quit()
        
main()


