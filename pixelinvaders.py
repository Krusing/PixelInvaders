
# PixelInvaders Prototype
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
INVADER_SIZE = 30
CIVILIAN_SIZE = 20
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelInvaders Prototype")
clock = pygame.time.Clock()

# Initialize variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * PLAYER_SIZE]
invaders = []
civilians = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Draw background
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
