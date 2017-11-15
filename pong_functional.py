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

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
# def ball_init(right):
#     global BALL_POS, BALL_START_POS, ball_vel # these are vectors stored as lists
#     BALL_POS = [WIDTH//2,HEIGHT//2]
#     print(WIDTH)
#     print(HEIGHT)
#     print(BALL_POS)
#     horz = random.randrange(2,4)
#     vert = random.randrange(1,3)
    
#     if right == False:
#         horz = - horz
        
#     ball_vel = [horz,-vert]
#     #game_builder.ball_vel = ball_vel

# # define event handlers
# def init():
#     global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score  # these are floats
#     global score1, score2  # these are ints
#     paddle1_pos = [PAD_WIDTH//2 - 1,HEIGHT//2]
#     paddle2_pos = [WIDTH +1 - PAD_WIDTH//2,HEIGHT//2]
#     l_score = 0
#     r_score = 0
#     if random.randrange(0,2) == 0:
#         ball_init(True)
#     else:
#         ball_init(False)

# def draw_board(colour=(255,255,255), *, screen=window):
#     "Draws the marker lines in the colour specified"    
#     global PAD_WIDTH, HEIGHT, WIDTH
#     pygame.draw.line(screen,   colour, [WIDTH // 2, 0],[WIDTH / 2, HEIGHT], 1)
#     pygame.draw.line(screen,   colour, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
#     pygame.draw.line(screen,   colour, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
#     pygame.draw.circle(screen, colour, [WIDTH//2, HEIGHT//2], 70, 1)


# def draw_paddle(pad_height, pad_width, paddle_pos, paddle_vel, colour=(0,255,0), *, screen=window):
#     "Draws a rectangular paddle, of the height and width specified, centered at the position specified"

#     # # update paddle's vertical position, keep paddle on the screen
#     # # if paddle in not off the board keep moving
#     # if (paddle_pos[y] > PAD_HEIGHT//2 and paddle_pos[y] < HEIGHT - PAD_HEIGHT//2):
#     #     paddle_pos[y] += paddle_vel

#     # # if paddle is touching the top of the board, but controller is moving paddle towards the middle of the board, keep moving
#     # elif (paddle_pos[y] == PAD_HEIGHT//2 and paddle_vel > 0):
#     #     paddle_pos[y] += paddle_vel

#     # # if paddle is touching the bottom of the board, but controller is moving paddle towards the middle of the board, keep moving
#     # elif (paddle_pos[y] == HEIGHT - PAD_HEIGHT//2 and paddle_vel < 0):
#     #     paddle_pos[y] += paddle_vel

#         # if paddle in not off the board, or touching the edge but moving towards the centre, keep moving
#     if ((paddle_pos[y] > PAD_HEIGHT//2 and paddle_pos[y] < HEIGHT - PAD_HEIGHT//2) or
#         (paddle_pos[y] == PAD_HEIGHT//2 and paddle_vel > 0) or
#         (paddle_pos[y] == HEIGHT - PAD_HEIGHT//2 and paddle_vel < 0)):
#         paddle_pos[y] += paddle_vel

#     pygame.draw.polygon(screen, colour, 
#             [[paddle_pos[x] - pad_width/2, paddle_pos[y] - pad_height/2], 
#              [paddle_pos[x] - pad_width/2, paddle_pos[y] + pad_height/2], 
#              [paddle_pos[x] + pad_width/2, paddle_pos[y] + pad_height/2], 
#              [paddle_pos[x] + pad_width/2, paddle_pos[y] - pad_height/2]])





# def draw_ball(radius, ball_pos, colour=(0,255,0), *,
#               bounce_vert=True, bounce_horiz=False, 
#               screen=window):

#     "Draws a circle of the radius specified, centered about the point specified"

#     global BALL_POS, ball_vel, l_score, r_score

#     pygame.draw.circle(screen, colour, BALL_POS, radius)

#     #ball collision check on top and bottom walls
#     if bounce_vert:
#         if int(BALL_POS[y]) <= BALL_RADIUS         : ball_vel[y] = -ball_vel[y]
#         if int(BALL_POS[y]) >= HEIGHT - BALL_RADIUS: ball_vel[y] = -ball_vel[y]

#     if bounce_horiz:
#         if int(BALL_POS[x]) <= BALL_RADIUS         : ball_vel[x] = -ball_vel[x]
#         if int(BALL_POS[x]) >= WIDTH - BALL_RADIUS : ball_vel[x] = -ball_vel[x]

#     # ball collision with paddles
#     if (int(BALL_POS[x]) <= BALL_RADIUS + PAD_WIDTH 
#         and int(BALL_POS[y]) in range(paddle1_pos[1] 
#             - PAD_HEIGHT//2,paddle1_pos[1] + PAD_HEIGHT//2,1)):
#         ball_vel[x] = -ball_vel[x]
#         ball_vel[x] *= 1.1
#         ball_vel[y] *= 1.1

#     elif int(BALL_POS[x]) <= BALL_RADIUS + PAD_WIDTH:
#         r_score += 1
#         ball_init(True)
#         print("INITIALISE_BALL")
#         print(BALL_POS)
        
#     if (int(BALL_POS[x]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH 
#     and int(BALL_POS[y]) in range(paddle2_pos[1] 
#         - PAD_HEIGHT//2,paddle2_pos[1] + PAD_HEIGHT//2,1)):
#         ball_vel[x] = -ball_vel[x]
#         ball_vel[x] *= 1.1
#         ball_vel[y] *= 1.1

#     elif int(BALL_POS[x]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
#         l_score += 1
#         ball_init(False)
#         print("INITIALISE_BALL")
#         print(BALL_POS)






#draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, BALL_POS, ball_vel, l_score, r_score
           
    canvas.fill(BLACK)
    draw_board()

    # BALL_POS[x] += int(ball_vel[x])
    # BALL_POS[y] += int(ball_vel[y])

    #draw_ball(BALL_RADIUS, BALL_POS, RED)

    draw_ball(BALL_RADIUS, BALL_POS, colour=(0,255,0))
    print("ball vel=", ball_vel)

    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle1_pos, paddle1_vel, GREEN)

    draw_paddle(PAD_HEIGHT, PAD_WIDTH, paddle2_pos, paddle2_vel, colour=(0,0,255))
    

    #bounce_pad_collision(BALL_POS, paddle1_pos, BALL_RADIUS)
    #bounce_pad_collision(BALL_POS, paddle2_pos, BALL_RADIUS)
    ball_reset_on_win(BALL_POS, BALL_RADIUS)
    # update_scores()

    # draw_ball(BALL_RADIUS, BALL_POS, colour=(0,255,0))
    # print(ball_vel)

    


    # # draw the board
    # pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0],[WIDTH / 2, HEIGHT], 1)
    # pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    # pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    # pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    #if paddle1_pos[1] > PAD_HEIGHT//2 and paddle1_pos[1] < HEIGHT - PAD_HEIGHT//2:
    #     paddle1_pos[1] += paddle1_vel

    # elif paddle1_pos[1] == PAD_HEIGHT//2 and paddle1_vel > 0:
    #     paddle1_pos[1] += paddle1_vel

    # elif paddle1_pos[1] == HEIGHT - PAD_HEIGHT//2 and paddle1_vel < 0:
    #     paddle1_pos[1] += paddle1_vel
    
    # if paddle2_pos[1] > PAD_HEIGHT//2 and paddle2_pos[1] < HEIGHT - PAD_HEIGHT//2:
    #     paddle2_pos[1] += paddle2_vel

    # elif paddle2_pos[1] == PAD_HEIGHT//2 and paddle2_vel > 0:
    #     paddle2_pos[1] += paddle2_vel

    # elif paddle2_pos[1] == HEIGHT - PAD_HEIGHT//2 and paddle2_vel < 0:
    #     paddle2_pos[1] += paddle2_vel

    

    #draw paddles and ball
    #pygame.draw.circle(canvas, RED, ball_pos, 20)
    # pygame.draw.polygon(canvas, GREEN, 
    #     [[paddle1_pos[x] - PAD_WIDTH//2, paddle1_pos[y] - PAD_HEIGHT//2], 
    #      [paddle1_pos[x] - PAD_WIDTH//2, paddle1_pos[y] + PAD_HEIGHT//2], 
    #      [paddle1_pos[x] + PAD_WIDTH//2, paddle1_pos[y] + PAD_HEIGHT//2], 
    #      [paddle1_pos[x] + PAD_WIDTH//2, paddle1_pos[y] - PAD_HEIGHT//2]], 0)


    # pygame.draw.polygon(canvas, GREEN, 
    #     [[paddle2_pos[x] - PAD_WIDTH//2, paddle2_pos[y] - PAD_HEIGHT//2],
    #      [paddle2_pos[x] - PAD_WIDTH//2, paddle2_pos[y] + PAD_HEIGHT//2], 
    #      [paddle2_pos[x] + PAD_WIDTH//2, paddle2_pos[y] + PAD_HEIGHT//2], 
    #      [paddle2_pos[x] + PAD_WIDTH//2, paddle2_pos[y] - PAD_HEIGHT//2]], 0)

   #update ball
   
    

    # #ball collision check on top and bottom walls
    # if int(BALL_POS[1]) <= BALL_RADIUS:
    #     ball_vel[1] = - ball_vel[1]
    # if int(BALL_POS[1]) >= HEIGHT + 1 - BALL_RADIUS:
    #     ball_vel[1] = -ball_vel[1]
    
    # #ball collison check on gutters or paddles
    # if (int(BALL_POS[0]) <= BALL_RADIUS + PAD_WIDTH 
    #     and int(BALL_POS[1]) in range(paddle1_pos[1] 
    #         - PAD_HEIGHT//2,paddle1_pos[1] + PAD_HEIGHT//2,1)):
    #     ball_vel[0] = -ball_vel[0]
    #     ball_vel[0] *= 1.1
    #     ball_vel[1] *= 1.1

    # elif int(BALL_POS[0]) <= BALL_RADIUS + PAD_WIDTH:
    #     r_score += 1
    #     ball_init(True)
        
    # if (int(BALL_POS[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH 
    #     and int(BALL_POS[1]) in range(paddle2_pos[1] - PAD_HEIGHT//2,
    #         paddle2_pos[1] + PAD_HEIGHT//2,1)):

    #     ball_vel[0] = -ball_vel[0]
    #     ball_vel[0] *= 1.1
    #     ball_vel[1] *= 1.1

    # elif int(BALL_POS[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
    #     l_score += 1
    #     ball_init(False)

    #update scores
    # myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    # label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    # canvas.blit(label1, (50,20))

    # myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    # label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    # canvas.blit(label2, (470, 20))  

   
    
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

    draw(window)

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
