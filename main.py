import pygame

# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Moving Image')

# Load an image
robot = pygame.image.load("robot.png")  # Ensure there's a robot.png in your project folder

# Initial position and speed
x_position = 0
speed = 2  # Speed of the movement

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the image
    x_position += speed
    
    # Check if the image needs to bounce back
    if x_position + robot.get_width() > 640 or x_position < 0:
        speed = -speed  # Reverse the direction

    # Fill the screen with black
    window.fill((0, 0, 0))

    # Blit the image at the new position
    window.blit(robot, (x_position, 50))

    # Update the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()

