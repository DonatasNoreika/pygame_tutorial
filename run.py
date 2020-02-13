
import pygame
pygame.init()
# https://youtu.be/i6xMBig-pP4

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mano pirmas žaidimas")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 50
char_width = 40
char_height = 40
vel = 2

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - char_width:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - char_height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, char_width, char_height))
    pygame.display.update()

pygame.quit()