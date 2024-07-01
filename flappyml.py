import pygame
import neat
import time
import random
import os

WIN_WIDTH = 600
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

