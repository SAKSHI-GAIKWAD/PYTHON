import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = 5 * random.choice([-1, 1])
        self.dy = 5 * random.choice([-1, 1])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Reflect the ball if it hits the top or bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)

# Create paddles and ball
player_paddle = Paddle(WIDTH - 2 * PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
opponent_paddle = Paddle(0, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_paddle.move((keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 10)

    # Ball movement
    ball.move()

    # Ball and paddle collisions
    if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(opponent_paddle.rect):
        ball.dx = -ball.dx

    # Draw everything
    screen.fill((0, 0, 0))

    player_paddle.draw()
    opponent_paddle.draw()
    ball.draw()

    pygame.display.flip()
    clock.tick(FPS)
