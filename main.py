import pygame
from time import sleep

pygame.init()

WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

# М'яч
r = 10
x, y = WIDTH // 2, HEIGHT // 2
vx, vy = 5, 5

# Межі
border_l = bound + r
border_r = WIDTH - bound - r
border_u = bound + r
border_d = HEIGHT - r

# Майданчик
height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

# Очки
score = 0
num = 1.5


def drawScore():
    win.fill(black)
    font = pygame.font.Font(None, 36)
    text = font.render("Your score: " + str(score), True, white)
    win.blit(text, (WIDTH // 2 - 100, HEIGHT // 3))
    pygame.display.update()


def drawWindow():
    win.fill(black)

    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))

    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.draw.circle(win, white, (int(x), int(y)), r)

    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not run:
        break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp

    if keys[pygame.K_RIGHT] and xp < WIDTH - width - bound:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx

    if y + vy < border_u:
        vy = -vy

    if vy > 0 and y + vy + r >= yp:
        if xp - r <= x + vx <= xp + width + r:
            vy = -abs(vy)
            score += 1
            vx *= num
            vy *= num
        else:
            drawScore()
            sleep(10)
            run = False
            break

    x += vx
    y += vy

    drawWindow()

pygame.quit()