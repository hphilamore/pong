#PONG pygame

import random
import pygame, sys
from pygame.locals import *
import game_builder
from game_builder import *


pygame.init()
fps = pygame.time.Clock()

# colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


# globals
WIDTH = 600
HEIGHT = 400 
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS = 20
BALL_POS = [WIDTH//2,HEIGHT//2]
x = 0
y = 1
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

paddle1_pos = [PAD_WIDTH//2 - 1,HEIGHT//2]
paddle2_pos = [WIDTH +1 - PAD_WIDTH//2,HEIGHT//2]

game_builder.BALL_RADIUS = BALL_RADIUS
game_builder.WIDTH = WIDTH
game_builder.HEIGHT = HEIGHT 
game_builder.PAD_WIDTH = PAD_WIDTH
game_builder.PAD_HEIGHT = PAD_HEIGHT
game_builder.x = x
game_builder.y = y
game_builder.l_score= l_score
game_builder.r_score = r_score
game_builder.paddle1_pos = paddle1_pos
game_builder.paddle2_pos = paddle2_pos

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
game_builder.window = window


def draw():
    global paddle1_pos, paddle2_pos
           
    window.fill(BLACK)
    draw_board()


    #draw_ball(BALL_RADIUS, BALL_POS, RED)

    draw_ball(BALL_RADIUS, colour=(0,255,0))
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle1_pos, paddle1_vel, GREEN)
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle2_pos, paddle2_vel, colour=(0,0,255))
    print(paddle1_pos, paddle2_pos)
    

    bounce_pad_collision(paddle1_pos)
    bounce_pad_collision(paddle2_pos)
    ball_reset_on_win()

   
    
#keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel
    
    if event.key == K_UP:
        paddle2_vel = -8

    elif event.key == K_DOWN:
        paddle2_vel = 8

    elif event.key == K_w:
        paddle1_vel = -8

    elif event.key == K_s:
        paddle1_vel = 8

#keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel
    
    if event.key in (K_w, K_s):
        paddle1_vel = 0

    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

init()


#game loop
while True:

    draw()

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
