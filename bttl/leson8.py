import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('ping pong')

ball_image = pygame.image.load('assets/ball.png')
paddle_image = pygame.image.load('assets/paddle.png')

ball_x = 200
ball_y = 150

player1_x = 5
player1_y = 150

player1_x = 500
player1_y = 150

w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


