import pygame
import sys
import random
from pygame.math import Vector2


class BALL:
    def __init__(self):
        # create x and y position
        self.x = 5
        self.y = 4
        self.x_speed = 5
        self.y_speed = 4
        self.direction = 1
        self.pos = Vector2(self.x, self.y)

    # draw a square 
    def draw_ball(self):
        # create rect
        ball_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)

        # move rect
        # left right
        if ball_rect.left <= 20 or ball_rect.right >= 580:
            self.direction *= -1
            self.x_speed = random.randint(0,8) * self.direction
            self.y_speed = random.randint(0,8) * self.direction

            if self.x_speed == 0 and self.y_speed == 0:
                self.x_speed = random.randint(2,8) * self.direction
                self.y_speed = random.randint(2,8) * self.direction
        # top bottom
        if ball_rect.top <= 20 or ball_rect.bottom >= 580:
            self.direction *= -1
            self.x_speed = random.randint(0,8) * self.direction
            self.y_speed = random.randint(0,8) * self.direction

            if self.x_speed == 0 and self.y_speed == 0:
                self.x_speed = random.randint(2,8) * self.direction
                self.y_speed = random.randint(2,8) * self.direction

        ball_rect.left += self.x_speed
        ball_rect.top += self.y_speed

        # draw rect
        pygame.draw.rect(screen, (124,165,112),ball_rect) #surface, color, rect


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

ball_speed_x = 3
ball_speed_y = 3
ball_pos_x = 300
ball_pos_y = 300
ball = pygame.draw.circle(screen, (42,95,23), [ball_pos_x,ball_pos_y], 5, 0)


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
    # ball
    ball = ball.move(ball_speed_x, ball_speed_y)
    if ball.left <=0 or ball.right >=600:
        ball_speed_x = -ball_speed_x
    if ball.top <=0 or ball.top >=600:
        ball_speed_y= -ball_speed_y

    # color for window background
    screen.fill((34,3,3))
    # draw the paddle 1
    pygame.draw.rect(screen, (123,26,136), (u1_x,u1_y,u1_width,u1_height))
    # draw the paddle 2
    pygame.draw.rect(screen, (12,26,116), (u2_x,u2_y,u2_width,u2_height))
    # draw ball
    pygame.draw.circle(screen, (42,95,23), ball.center, 5, 0)
    print(ball.center)

    pygame.display.update()
    clock.tick(60)