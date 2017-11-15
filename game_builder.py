import random
import pygame, sys
from pygame.locals import *

#l_score = 0
#r_score = 0


def ball_init(right):
    global BALL_POS, BALL_START_POS, ball_vel # these are vectors stored as lists
    BALL_POS = [WIDTH//2,HEIGHT//2]
    print(WIDTH)
    print(HEIGHT)
    print(BALL_POS)
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_vel = [horz,-vert]
    #game_builder.ball_vel = ball_vel

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score  # these are floats
    #global score1, score2  # these are ints
    paddle1_pos = [PAD_WIDTH//2 - 1,HEIGHT//2]
    paddle2_pos = [WIDTH +1 - PAD_WIDTH//2,HEIGHT//2]
    l_score = 0
    r_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)



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



def draw_ball(radius, ball_pos, colour=(0,255,0), *,
              bounce_vert=True, bounce_horiz=True):

    "Draws a circle of the radius specified, centered about the point specified"

    global window, l_score, r_score, ball_vel

    ball_pos[x] += int(ball_vel[x])
    ball_pos[y] += int(ball_vel[y])

    pygame.draw.circle(window, colour, ball_pos, radius)

    #ball collision check on top and bottom walls
    if bounce_vert:
        if int(ball_pos[y]) <= radius         : ball_vel[y] = -ball_vel[y]
        if int(ball_pos[y]) >= HEIGHT - radius: ball_vel[y] = -ball_vel[y]

    if bounce_horiz:
        if int(ball_pos[x]) <= radius         : ball_vel[x] = -ball_vel[x]
        if int(ball_pos[x]) >= WIDTH - radius  : ball_vel[x] = -ball_vel[x]


def bounce_pad_collision(ball_pos, paddle_pos, radius):
    # ball collision with paddles
    global ball_vel
    if (int(ball_pos[x]) <= radius + PAD_WIDTH 
        and int(ball_pos[y]) in range(paddle_pos[1] 
            - PAD_HEIGHT//2,paddle_pos[1] + PAD_HEIGHT//2,1)):
        ball_vel[x] = -ball_vel[x]
        ball_vel[x] *= 1.1
        ball_vel[y] *= 1.1



def ball_reset_on_win(ball_pos, radius):

    global l_score, r_score

    if int(ball_pos[x]) <= radius + PAD_WIDTH:
        r_score += 1
        ball_init(True)
        print("INITIALISE_BALL")
        print(ball_pos)
        

    elif int(ball_pos[x]) >= WIDTH + 1 - radius - PAD_WIDTH:
        l_score += 1
        ball_init(False)
        print("INITIALISE_BALL")
        print(BALL_POS)


def update_scores():
    #update scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    window.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    window.blit(label2, (470, 20)) 



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



