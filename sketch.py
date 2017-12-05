#! /usr/bin/env python
import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =  (0, 0, 255)
MY_COLOUR = (240, 20, 230)

WIDTH = 640
HEIGHT = 400
RADIUS = 20
H = 320
V = 200

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(MY_COLOUR)

pygame.draw.circle(screen, 
	BLUE, 
	[H, V], 
	RADIUS) 

pygame.display.flip()


finished = False

while not finished:
	event = pygame.event.poll()

	if event.type == pygame.QUIT:
	    	finished = True

	clock.tick(60) 
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: V -= 3
	if pressed[pygame.K_DOWN]: V += 3
	if pressed[pygame.K_LEFT]: H -= 3
	if pressed[pygame.K_RIGHT]: H += 3

	if V < RADIUS//2: V = RADIUS//2 
	if V > HEIGHT - (RADIUS//2): V = HEIGHT - (RADIUS//2)
	if H < RADIUS//2: H = RADIUS//2 
	if H > WIDTH - (RADIUS//2): H = WIDTH - (RADIUS//2)


	screen.fill(MY_COLOUR)

	pygame.draw.circle(screen, 
						BLUE, 
						[H, V], 
						RADIUS) 

	pygame.display.flip()
	
     
         
    


