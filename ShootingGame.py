import pygame
import random
import sys  # Необходимо для выхода

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

target_speed_x = random.uniform(-0.2, 0.2)
target_speed_y = random.uniform(-0.2, 0.2)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)


def pause_message():
    pause_font = pygame.font.Font(None, 72)
    pause_surf = pause_font.render('Pause. Press any key to continue.', True, (255, 0, 0))
    pause_rect = pause_surf.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(pause_surf, pause_rect)
    pygame.display.flip()
    pygame.event.clear()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                paused = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
                score += 1  # Увеличение счетчика очков при попадании в цель
            else:
                score -= 1  # Вычитание очков при промахе

            # Проверка достижения количества очков для паузы
            if score % 10 == 0 and score > 0:
                pause_message()

    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= screen_width - target_width:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= screen_height - target_height:
        target_speed_y *= -1

    screen.blit(target_image, (target_x, target_y))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()