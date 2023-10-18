import pygame
import sys
import random
from pygame.math import Vector2

class BALL:
    def __init__(self):
        self.ball_speed_x = random.randint(1,4)
        self.ball_speed_y = random.randint(1,4)
        self.ball_pos_x = 300
        self.ball_pos_y = 300
        

    def draw_ball(self):
        # create ball
        ball1 = pygame.draw.circle(screen, (42,95,23), [self.ball_pos_x,self.ball_pos_y], 5, 0)

        ball = ball1.move(self.ball_speed_x, self.ball_speed_y)
        # move rect
        if ball.left <=0 or ball.right >=600:
            self.ball_speed_x = -self.ball_speed_x
        if ball.top <=0 or ball.top >=600:
            self.ball_speed_y= -self.ball_speed_y
        
        self.ball_pos_x += self.ball_speed_x
        self.ball_pos_y += self.ball_speed_y

        # draw ball
        pygame.draw.circle(screen, (42,95,23), ball1.center, 5, 0)

pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

u1_x = 30
u1_y = 250
u1_width = 10
u1_height = 50
u1_speed = 5

u2_x = 560
u2_y = 150
u2_width = 10
u2_height = 50
u2_speed = 5

#ball
ball = BALL()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # user input 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and u1_y>0:
        u1_y-=u1_speed
    if keys[pygame.K_DOWN] and u1_y<(cell_number*cell_size)-u1_height:
        u1_y+=u1_speed
    # user input 2
    if keys[pygame.K_w] and u2_y>0:
        u2_y-=u2_speed
    if keys[pygame.K_s] and u2_y<(cell_number*cell_size)-u2_height:
        u2_y+=u2_speed

    # color for window background
    screen.fill((34,3,3))
    # draw the paddle 1
    pygame.draw.rect(screen, (123,26,136), (u1_x,u1_y,u1_width,u1_height))
    # draw the paddle 2
    pygame.draw.rect(screen, (12,26,116), (u2_x,u2_y,u2_width,u2_height))
    # draw ball
    ball.draw_ball()
    

    pygame.display.update()
    clock.tick(60)