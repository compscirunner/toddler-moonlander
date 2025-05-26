import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Toddler Moonlander")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Simple lander
lander = pygame.Rect(375, 50, 50, 80)
velocity_y = 0

# Joystick setup
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None

def draw():
    screen.fill(GRAY)
    # Simulate "moon"
    pygame.draw.circle(screen, WHITE, (400, 600), 300)
    pygame.draw.rect(screen, BLUE, lander)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joystick controls
    x_move = 0
    thrust = False
    if joystick:
        x_axis = joystick.get_axis(0)  # Left/right
        button = joystick.get_button(0)  # Main button
        if x_axis < -0.2:
            x_move = -5
        elif x_axis > 0.2:
            x_move = 5
        if button:
            thrust = True

    # Move lander
    lander.x += x_move
    if thrust:
        velocity_y = 1  # Gentle descent
    else:
        velocity_y = 0

    lander.y += velocity_y

    if lander.y > 500:
        lander.y = 500  # "landed"

    draw()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()