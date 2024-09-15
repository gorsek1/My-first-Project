import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 15
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create paddles and ball
player1 = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Move ball
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED_X = -BALL_SPEED_X

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH//2, HEIGHT//2)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Update display
    pygame.display.flip()
    clock.tick(60)
