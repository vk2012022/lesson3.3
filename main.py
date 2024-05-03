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

list = ("img/target.png", "img/target10.png", "img/target7.png", "img/target3.png", "img/target4.png", "img/target5.png", "img/target8.png")

move_frequency = 3000  # Частота смены позиции мишени в кадрах
frame_count = 0  # Счетчик кадров
hits = 0  # Счетчик попаданий

# Настройка шрифта для вывода текста
font = pygame.font.Font(None, 36)

running = True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1  # Увеличение счетчика попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                random_fact = random.choice(list)
                target_img = pygame.image.load(random_fact)
    frame_count += 1
    if frame_count >= move_frequency:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        frame_count = 0  # Сброс счетчика кадров после перемещения мишени

    # Отображение счетчика попаданий
    hits_text = font.render(f"Попаданий: {hits}", True, (255, 255, 255))
    screen.blit(hits_text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()

