import pygame
from random import uniform as func
from time import sleep

# Ініціалізація Pygame
pygame.init()

# Вікно
WIDTH, HEIGHT = 600, 400
bound = 10
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bounce Game")

# Кольори
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# М'яч — початкові значення
x, y = WIDTH // 2, HEIGHT // 2
radius = 10
vx, vy = func(-4, 4), -4

# Межі (границі)
border_l = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius
border_d = HEIGHT - bound - radius

# Платформа (майданчик)
height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

# Підрахунок очок
score = 0

# Функція виводу фінального результату
def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = ''.join([chr(int(str(el), 8)) for el in [107, 141, 155, 145, 40, 157, 166, 145, 162]])
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))

    score_text = Font.render(f"Your score: {score}", 1, (255, 255, 255))
    win.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 3 + 50))

    pygame.display.update()

# Функція малювання вікна
def drawWindow():
    win.fill(black)
    # Межі (окрім нижньої)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # верхня
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # ліва
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # права

    # М'яч
    pygame.draw.circle(win, green, (int(x), int(y)), radius)

    # Платформа
    pygame.draw.rect(win, white, (xp, yp, width, height))

    pygame.display.update()

# Основний цикл гри
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    # Вихід по події закриття
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Обробка клавіш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    # Відбиття м'яча від боків і верху
    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    # Відбиття або поразка
    if y + vy > border_d:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= 1.1
            vy *= 1.1
            score += 1
        else:
            drawScore()
            sleep(10)
            run = False

    # Оновлення позиції м'яча
    x += vx
    y += vy

    # Малювання
    drawWindow()

pygame.quit()
