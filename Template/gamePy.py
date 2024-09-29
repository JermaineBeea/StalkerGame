import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Icon")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define initial position of the icon
icon_size = 50
icon_x, icon_y = screen_width // 2, screen_height // 2
icon_speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get all keys currently pressed
    keys = pygame.key.get_pressed()

    # Update the icon's position based on the arrow keys
    if keys[pygame.K_LEFT]:
        icon_x -= icon_speed
    if keys[pygame.K_RIGHT]:
        icon_x += icon_speed
    if keys[pygame.K_UP]:
        icon_y -= icon_speed
    if keys[pygame.K_DOWN]:
        icon_y += icon_speed

    # Prevent the icon from moving out of the screen bounds
    icon_x = max(0, min(icon_x, screen_width - icon_size))
    icon_y = max(0, min(icon_y, screen_height - icon_size))

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the icon (rectangle)
    pygame.draw.rect(screen, BLUE, (icon_x, icon_y, icon_size, icon_size))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
