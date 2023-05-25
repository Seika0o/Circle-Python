import pygame
import math

pygame.init()         # Initializing pygame

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Drawing Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Adding circle parameters
circle_radius = 100
circle_center = (width // 2, height // 2)

mouse_position = (0, 0)         # Mouse position

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            
            
            mouse_position = pygame.mouse.get_pos()             # Updating the mouse position

    # Очистка
    screen.fill(BLACK)

    # Draw the perfect circle
    pygame.draw.circle(screen, WHITE, circle_center, circle_radius, 1)

    # Draw the user's circle
    pygame.draw.circle(screen, WHITE, mouse_position, circle_radius, 1)

    # Calculate the mean sqrt errror
    dx = circle_center[0] - mouse_position[0]
    dy = circle_center[1] - mouse_position[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)
    mse = (distance - circle_radius) ** 2

    # Calculate the score
    perfection = max(0, 1 - (mse / (circle_radius ** 2)))

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Perfection: {perfection:.2%}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update
    pygame.display.flip()

# Quit
pygame.quit()