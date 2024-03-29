import pygame
import random

pygame.init()

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

running = True
while running:

    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()


    pass

    pygame.quit