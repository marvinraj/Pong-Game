import pygame
import sys
import random
from pygame.math import Vector2

pygame.init() # initiates pygame module

# create surface display
screen_width = 750
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# empty rectangles/elements (ball, players)
# (x,y) is at the left corner of the rect
ball = pygame.Rect(screen_width/2,screen_height/2,10,10) 
player1 = pygame.Rect(20,screen_height/2,10,50)
player2 = pygame.Rect(screen_width-30,screen_height/2,10,50)

# ball & players movements
ball_speed_x = 3
ball_speed_y = 3
player1_speed = 5
player2_speed = 5

# colors
p1_color = (123,26,136)
p2_color = (12,26,116)
ball_color = (42,95,23)
bg_color = (34,3,3)



# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    # move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.y>0:
        player1.y -= player1_speed
    if keys[pygame.K_s] and player1.y<screen_height-player1.height:
        player1.y += player1_speed
    if keys[pygame.K_UP] and player2.y>0:
        player2.y -= player2_speed
    if keys[pygame.K_DOWN] and player2.y<screen_height-player2.height:
        player2.y += player2_speed
     
    # move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height: # y-axis
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width: # x-axis
        # respawn ball at the center 
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x *= random.choice((1,-1))
        ball_speed_y *= random.choice((1,-1))

    # check collision between ball & players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
    
    # color for window background
    screen.fill(bg_color)
    # drawing rectangles/elements
    pygame.draw.ellipse(screen,ball_color,ball)
    pygame.draw.rect(screen,p1_color,player1)
    pygame.draw.rect(screen,p2_color,player2)


    pygame.display.update()
    clock.tick(60)