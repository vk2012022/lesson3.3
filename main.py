import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/maxresdefault.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

move_frequency = 3000  # Частота смены позиции мишени в кадрах
frame_count = 0  # Счетчик кадров

running = True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    frame_count += 1
    if frame_count >= move_frequency:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        frame_count = 0  # Сброс счетчика кадров после перемещения мишени

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
