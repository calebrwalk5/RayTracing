# it's incredibly slow
import pygame
import math

pygame.init()

# Set the window size
window_size = (1366, 768)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("RayTracing with Camera Movement")

# Set the background color
bg_color = (0, 0, 0)

# Set the player's movement speed
player_speed = 5

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def rotate_left(self):
        self.angle -= 5

    def rotate_right(self):
        self.angle += 5

# Create the player
player = Player(window_size[0] / 2, window_size[1] / 2)

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rotate_left()
            elif event.key == pygame.K_RIGHT:
                player.rotate_right()

    # Check for movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_s]:
        player.y += player_speed
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed

    # Clear the screen
    screen.fill(bg_color)

    # Cast rays from the player's position at a range of angles
    for i in range(window_size[0]):
        angle = player.angle - 30 + i

        radians = math.radians(angle)

        distance = float('inf')

        x = player.x
        y = player.y

        dx = math.cos(radians)
        dy = math.sin(radians)

        # Draw lines from the player's position to the points where the rays intersect with the edges of the screen
        while True:
            if x < 0 or x >= window_size[0] or y < 0 or y >= window_size[1]:
                break

            pygame.draw.line(screen, (255, 255, 255), (player.x, player.y), (x, y))

            x += dx
            y += dy

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(144)
