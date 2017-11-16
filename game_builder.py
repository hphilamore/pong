import random
import pygame, sys
from pygame.locals import *

x = 0
y = 1


def ball_init(right):
    "Places the ball in the centre of the board and gives it a random velocity"
    global BALL_POS, BALL_START_POS, ball_vel 
    BALL_POS = [WIDTH//2,HEIGHT//2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_vel = [horz,-vert]


def init():
    "Sets score to zero and sets random ball direction"
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score
    #paddle1_pos = [PAD_WIDTH//2 - 1,HEIGHT//2]
    #paddle2_pos = [WIDTH +1 - PAD_WIDTH//2,HEIGHT//2]
    l_score = 0
    r_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)


def draw_board(colour=(255,255,255)):
    "Draws the marker lines in the colour specified"  
    global window, PAD_WIDTH, HEIGHT, WIDTH
    pygame.draw.line(window,   colour, [WIDTH // 2, 0],       [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(window,   colour, [PAD_WIDTH, 0],        [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(window,   colour, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH,HEIGHT], 1)
    pygame.draw.circle(window, colour, [WIDTH//2, HEIGHT//2],  HEIGHT//6, 1)


def draw_ball(radius, colour=(0,255,0), *,
              random_movement = False, 
              bounce_vert=False, 
              bounce_horiz=False):

    "Draws a circle of the radius specified, centered about the point specified"

    global window, l_score, r_score, BALL_POS, ball_vel

    if random_movement:
        BALL_POS[x] += int(ball_vel[x])
        BALL_POS[y] += int(ball_vel[y])

    pygame.draw.circle(window, colour, BALL_POS, radius)

    #ball collision check on top and bottom walls
    if bounce_vert:
        if int(BALL_POS[y]) <= radius         : ball_vel[y] = -ball_vel[y]
        if int(BALL_POS[y]) >= HEIGHT - radius: ball_vel[y] = -ball_vel[y]

    if bounce_horiz:
        if int(BALL_POS[x]) <= radius         : ball_vel[x] = -ball_vel[x]
        if int(BALL_POS[x]) >= WIDTH - radius  : ball_vel[x] = -ball_vel[x]

    # if int(BALL_POS[x]) <= BALL_RADIUS: 
    #     #r_score += 1
    #     ball_init(True)        

    # elif int(BALL_POS[x]) > WIDTH - BALL_RADIUS:
    #     #l_score += 1
    #     ball_init(False)


def draw_paddle(pad_height, pad_width, paddle_pos, paddle_vel, colour=(0,255,0)):
    "Draws a rectangular paddle, of the height and width specified, centered at the position specified"

    global window

    # if paddle in not off the board, or touching the edge but moving towards the centre, keep moving
    # if ((paddle_pos[y] >= pad_height/2 and paddle_pos[y] <= HEIGHT - pad_height/2) or
    #     (paddle_pos[y] == pad_height/2 and paddle_vel[y] > 0) or
    #     (paddle_pos[y] == HEIGHT - PAD_HEIGHT/2 and paddle_vel[y] < 0)):

    if ((paddle_pos[y] >= pad_height/2 and paddle_pos[y] <= HEIGHT - pad_height/2) or
        (paddle_pos[y] < pad_height/2 and paddle_vel[y] > 0) or
        (paddle_pos[y] > HEIGHT - PAD_HEIGHT/2 and paddle_vel[y] < 0)):

        paddle_pos[y] += paddle_vel[y]

    pygame.draw.polygon(window, colour, 
            [[paddle_pos[x] - pad_width/2, paddle_pos[y] - pad_height/2], 
             [paddle_pos[x] - pad_width/2, paddle_pos[y] + pad_height/2], 
             [paddle_pos[x] + pad_width/2, paddle_pos[y] + pad_height/2], 
             [paddle_pos[x] + pad_width/2, paddle_pos[y] - pad_height/2]])


def bounce_pad_collision(paddle_pos):
    "Ball bounces when colliding with paddles" 
    global ball_vel, BALL_RADIUS, BALL_POS

    if (abs(BALL_POS[x] - paddle_pos[x]) < (BALL_RADIUS)
        and 
        int(BALL_POS[y]) in range(paddle_pos[1] - PAD_HEIGHT//2,
                                  paddle_pos[1] + PAD_HEIGHT//2,1)):

        ball_vel[x] = -ball_vel[x]
        ball_vel[x] *= 1.1
        ball_vel[y] *= 1.1


def ball_reset_on_win():
    "Recentres the ball when a point is scored by calling the ball initialisation function"

    global l_score, r_score, BALL_POS, BALL_RADIUS        

    if int(BALL_POS[x]) <= BALL_RADIUS: 
        ball_init(True)        

    elif int(BALL_POS[x]) > WIDTH - BALL_RADIUS:
        ball_init(False)


def update_scores(*,font="Comic Sans MS", font_size=20):
    "Increments and dislpays scores when a opint is scored"
    # Available fonts: "Arial",  "Comic Sans MS", "monospace"
    # pygame.font.get_fonts() returns all fonts

    global l_score, r_score, BALL_POS, BALL_RADIUS        

    if int(BALL_POS[x]) <= BALL_RADIUS: 
        r_score += 1

    elif int(BALL_POS[x]) > WIDTH - BALL_RADIUS:
        l_score += 1

    myfont = pygame.font.SysFont(font, font_size)
    label1 = myfont.render("Score "+str(l_score), 1, (255,255,0))
    label2 = myfont.render("Score "+str(r_score), 1, (255,255,0))
    window.blit(label1, ((WIDTH/5),20))
    window.blit(label2, ((3*WIDTH/4), 20)) 





