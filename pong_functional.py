#PONG pygame
import random
import pygame, sys
from pygame.locals import *
import game_builder
from game_builder import *
pygame.init()
clock = pygame.time.Clock()

# colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

# globals
x = 0
y = 1
WIDTH = 600
HEIGHT = 400 
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS = 20
ball_vel = [0,0]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
BALL_POS = [WIDTH//2,HEIGHT//2]
paddle1_pos = [WIDTH - PAD_WIDTH//2, HEIGHT//2]
paddle2_pos = [PAD_WIDTH//2,         HEIGHT//2]

game_builder.WIDTH = WIDTH
game_builder.HEIGHT = HEIGHT 
game_builder.PAD_WIDTH = PAD_WIDTH
game_builder.PAD_HEIGHT = PAD_HEIGHT
game_builder.BALL_RADIUS = BALL_RADIUS
game_builder.paddle1_pos = paddle1_pos
game_builder.paddle2_pos = paddle2_pos


#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT))
game_builder.window = window

init()

#game loop
while True:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
           
    window.fill(BLACK)
    draw_board()
    
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle1_pos, paddle1_vel, colour=(0,0,255))
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle2_pos, paddle2_vel, colour=(0,0,255))
    draw_ball(BALL_RADIUS, colour=(0,255,0), random_movement = True, bounce_vert=True)
    bounce_pad_collision(paddle1_pos)
    bounce_pad_collision(paddle2_pos)
    update_scores()  
    ball_reset_on_win()     

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] & pressed[pygame.K_DOWN]: paddle1_vel[y] = 0
    elif pressed[pygame.K_UP]: paddle1_vel[y] = -8
    elif pressed[pygame.K_DOWN]: paddle1_vel[y] = 8
    else: paddle1_vel[y] = 0

    if pressed[pygame.K_w] & pressed[pygame.K_s]: paddle2_vel[y] = 0
    elif pressed[pygame.K_w]: paddle2_vel[y] = -8
    elif pressed[pygame.K_s]: paddle2_vel[y] = 8
    else: paddle2_vel[y] = 0
            
    pygame.display.update()
    clock.tick(60)
