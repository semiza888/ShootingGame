import pygame
import random

running = True
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ShootingGame')
icon = pygame.image.load('img/ShootingGame.png')
pygame.display.set_icon(icon)
target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80
target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while running:
    pass

    pygame.quit