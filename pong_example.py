import random, pygame, sys, game_builder
from pygame.locals import *
import game_builder.game_builder as gb
from game_builder.game_builder import *
pygame.init()
init()

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

x = 0
y = 1
WIDTH = 600
HEIGHT = 400 
PAD_WIDTH = 10
PAD_HEIGHT = 80
BALL_RADIUS = 20
ball_vel = [0,0]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
paddle1_pos = [WIDTH - PAD_WIDTH//2, HEIGHT//2]
paddle2_pos = [PAD_WIDTH//2,         HEIGHT//2]

gb.WIDTH = WIDTH
gb.HEIGHT = HEIGHT 
gb.PAD_WIDTH = PAD_WIDTH
gb.PAD_HEIGHT = PAD_HEIGHT
gb.BALL_RADIUS = BALL_RADIUS

window = game_window(WIDTH, HEIGHT)
gb.window = window

while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()

    window.fill(blue)
    draw_board(green)
    #draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle1_pos, paddle1_vel)
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle1_pos, paddle1_vel, white)
    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle2_pos, paddle2_vel, black)
    draw_ball(BALL_RADIUS, colour=red, random_movement=True, bounce_vert=True)
    bounce_pad_collision(paddle1_pos)
    bounce_pad_collision(paddle2_pos)
    update_scores(font="Arial", font_size=30) 
    ball_reset_on_win()
    pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_UP] & pressed[pygame.K_DOWN] : paddle1_vel[y] = 0
    # elif pressed[pygame.K_UP]                        : paddle1_vel[y] = -8
    # elif pressed[pygame.K_DOWN]                      : paddle1_vel[y] = 8
    # else: paddle1_vel[y] = 0
    if pressed[pygame.K_UP] & pressed[pygame.K_DOWN]: paddle1_vel[y] = 0
    elif pressed[pygame.K_UP]: paddle1_vel[y] = -8
    elif pressed[pygame.K_DOWN]: paddle1_vel[y] = 8
    else: paddle1_vel[y] = 0

    if pressed[pygame.K_w] & pressed[pygame.K_s]: paddle2_vel[y] = 0
    elif pressed[pygame.K_w]: paddle2_vel[y] = -8
    elif pressed[pygame.K_s]: paddle2_vel[y] = 8
    else: paddle2_vel[y] = 0

    clock = pygame.time.Clock().tick(60)
    pygame.display.update()
