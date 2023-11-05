import pygame
import sys
import random
from pygame.math import Vector2

class PADDLE:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    
    def draw_paddle(self):
        display = pygame.display.get_surface()
        pygame.draw.rect(display, (self.color), (self.x,self.y, self.width, self.height), 0)

    def move_player_1(self, cell_number, cell_size):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_w] and self.y>0:
            self.y-=self.speed
        if self.keys[pygame.K_s] and self.y<(cell_number*cell_size)-self.height:
            self.y+=self.speed

    def move_player_2(self, cell_number, cell_size):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] and self.y>0:
            self.y-=self.speed
        if self.keys[pygame.K_DOWN] and self.y<(cell_number*cell_size)-self.height:
            self.y+=self.speed

class BALL:
    def __init__(self, ball_speed_x, ball_speed_y, ball_pos_x, ball_pos_y):
        self.ball_speed_x = ball_speed_x
        self.ball_speed_y = ball_speed_y
        self.ball_pos_x = ball_pos_x
        self.ball_pos_y = ball_pos_y

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


# objects
ball = BALL(random.randint(1,4), random.randint(1,4), 300, 300)
paddle1 = PADDLE(30,150,10,50,(123,26,136),5)
paddle2 = PADDLE(560,150,10,50,(12,26,116),5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ball collision
    
    # color for window background
    screen.fill((34,3,3))
    # draw the paddle 1 & 2
    paddle1.draw_paddle()
    paddle2.draw_paddle()
    # draw the paddle 2
    paddle1.move_player_1(cell_number, cell_size)
    paddle2.move_player_2(cell_number, cell_size)
    # draw ball
    ball.draw_ball()
    print(ball.ball_pos_x)

    pygame.display.update()
    clock.tick(60)