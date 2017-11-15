import random
import pygame, sys
from pygame.locals import *


def draw_board(colour=(255,255,255)):
    "Draws the marker lines in the colour specified"  
    global window, PAD_WIDTH, HEIGHT, WIDTH
    pygame.draw.line(window,   colour, [WIDTH // 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(window,   colour, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(window,   colour, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(window, colour, [WIDTH//2, HEIGHT//2], 70, 1)


# def draw_ball(radius, ball_pos, ball_vel, colour=(0,255,0), *,
#               bounce_vert=True, bounce_horiz=False):
#     "Draws a circle of the radius specified, centered about the point specified"

#     global window

#     pygame.draw.circle(window, colour, ball_pos, radius)

#     #ball collision check on top and bottom walls
#     if bounce_vert:
#         if int(ball_pos[y]) <= radius         : ball_vel[y] = -ball_vel[y]
#         if int(ball_pos[y]) >= HEIGHT - radius: ball_vel[y] = -ball_vel[y]

#     # if bounce_horiz:
#     #     if int(ball_pos[x]) <= radius         : ball_vel[x] = -ball_vel[x]
#     #     if int(ball_pos[x]) >= WIDTH - radius : ball_vel[x] = -ball_vel[x]


def draw_paddle(pad_height, pad_width, paddle_pos, paddle_vel, colour=(0,255,0)):
    "Draws a rectangular paddle, of the height and width specified, centered at the position specified"

    global window
    # # update paddle's vertical position, keep paddle on the screen
    # # if paddle in not off the board keep moving
    # if (paddle_pos[y] > PAD_HEIGHT//2 and paddle_pos[y] < HEIGHT - PAD_HEIGHT//2):
    #     paddle_pos[y] += paddle_vel

    # # if paddle is touching the top of the board, but controller is moving paddle towards the middle of the board, keep moving
    # elif (paddle_pos[y] == PAD_HEIGHT//2 and paddle_vel > 0):
    #     paddle_pos[y] += paddle_vel

    # # if paddle is touching the bottom of the board, but controller is moving paddle towards the middle of the board, keep moving
    # elif (paddle_pos[y] == HEIGHT - PAD_HEIGHT//2 and paddle_vel < 0):
    #     paddle_pos[y] += paddle_vel

        # if paddle in not off the board, or touching the edge but moving towards the centre, keep moving
    if ((paddle_pos[y] > PAD_HEIGHT//2 and paddle_pos[y] < HEIGHT - PAD_HEIGHT//2) or
        (paddle_pos[y] == PAD_HEIGHT//2 and paddle_vel > 0) or
        (paddle_pos[y] == HEIGHT - PAD_HEIGHT//2 and paddle_vel < 0)):
        paddle_pos[y] += paddle_vel

    pygame.draw.polygon(window, colour, 
            [[paddle_pos[x] - pad_width/2, paddle_pos[y] - pad_height/2], 
             [paddle_pos[x] - pad_width/2, paddle_pos[y] + pad_height/2], 
             [paddle_pos[x] + pad_width/2, paddle_pos[y] + pad_height/2], 
             [paddle_pos[x] + pad_width/2, paddle_pos[y] - pad_height/2]])



