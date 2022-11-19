import pygame
pygame.init()

WIGHT, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIGHT, PADDLE_HEIGHT  = 20, 100 
BALL_RADIUS = 7

class Paddle:
    COLOR = WHITE
    VELOCITY = 2    

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, UP = True):
        if UP:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY


class Ball:
    COLOR = WHITE
    m_vel = 3

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.m_vel
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel    
        

def draw(win, paddles, ball):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 10):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIGHT // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)
    
    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1 

    if ball.x_vel > 0:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x - ball.radius >= right_paddle.x - right_paddle.width // 2:
                ball.x_vel *= -1


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(UP = True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY <= HEIGHT - PADDLE_HEIGHT:
        left_paddle.move(UP = False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(UP = True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY <= HEIGHT - PADDLE_HEIGHT:
        right_paddle.move(UP = False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIGHT, PADDLE_HEIGHT)
    right_paddle = Paddle(WIGHT - 10 - PADDLE_WIGHT, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIGHT, PADDLE_HEIGHT)
    ball = Ball(WIGHT // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        handle_collision(ball, left_paddle, right_paddle)

        ball.move()

    pygame.quit()


if __name__ == '__main__':
    main()