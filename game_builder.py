import random
import pygame, sys
from pygame.locals import *


def draw_ball(radius, ball_pos, ball_vel, colour=(0,255,0), *,
              bounce_vert=True, bounce_horiz=False):

    "Draws a circle of the radius specified, centered about the point specified"

    global window

    pygame.draw.circle(window, colour, ball_pos, radius)

    #ball collision check on top and bottom walls
    if bounce_vert:
        if int(ball_pos[y]) <= radius         : ball_vel[y] = -ball_vel[y]
        if int(ball_pos[y]) >= HEIGHT - radius: ball_vel[y] = -ball_vel[y]

    if bounce_horiz:
        if int(ball_pos[x]) <= radius         : ball_vel[x] = -ball_vel[x]
        if int(ball_pos[x]) >= WIDTH - radius : ball_vel[x] = -ball_vel[x]




# def draw_board(colour=(255,255,255), *, screen=window):
#     "Draws the marker lines in the colour specified"  
#     global window, PAD_WIDTH, HEIGHT, WIDTH
#     pygame.draw.line(window,   colour, [WIDTH // 2, 0],[WIDTH / 2, HEIGHT], 1)
#     pygame.draw.line(window,   colour, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
#     pygame.draw.line(window,   colour, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
#     pygame.draw.circle(window, colour, [WIDTH//2, HEIGHT//2], 70, 1)