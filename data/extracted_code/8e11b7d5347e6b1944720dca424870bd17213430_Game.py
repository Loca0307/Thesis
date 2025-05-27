import pygame
import random

# Initialize PyGame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Over Spikes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_size = 40
player_x = 100
player_y = HEIGHT - player_size
player_velocity = 0
jump_force = -15
gravity = 1

# Spike settings
spike_width = 20
spike_height = 40
spike_x = WIDTH
spike_y = HEIGHT - spike_height
spike_speed = 10

# Game variables
running = True
is_jumping = False
score = 0
font = pygame.font.Font(None, 36)

# Main loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not is_jumping:
                is_jumping = True
                player_velocity = jump_force

    # Player movement
    if is_jumping:
        player_y += player_velocity
        player_velocity += gravity
        if player_y >= HEIGHT - player_size:
            player_y = HEIGHT - player_size
            is_jumping = False

    # Spike movement
    spike_x -= spike_speed
    if spike_x < -spike_width:
        spike_x = WIDTH
        score += 1

    # Collision detection
    if spike_x < player_x + player_size and spike_x + spike_width > player_x:
        if player_y + player_size >= spike_y:
            running = False  # End the game if the player hits a spike

    # Draw player, spike, and score
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    pygame.draw.polygon(screen, RED, [(spike_x, spike_y), (spike_x + spike_width // 2, spike_y - spike_height), (spike_x + spike_width, spike_y)])
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit PyGame
pygame.quit()