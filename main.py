import pygame
import math

fps = 60
white = (255, 255, 255)
black = (0, 0, 0)
fall = True
clock = pygame.time.Clock()
screenWidth, screenHeight = 800, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
characterWidth = 10
speed = 30
heightMultiplier = 5
canJump = True
y = 400
x = 400


def drop():
    done = False
    canMoveRight = True
    canMoveLeft = True
    fallSpeed = 1
    global canJump
    global x, y
    global heightMultiplier
    while not done:
        buttonDown = False
        screen.fill(white)
        clock.tick(fps)
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(screen, black, [x, y], 10)

        pygame.draw.line(screen, black, [x, y], [mx, my], 1)
        pygame.draw.line(screen, black, [x, y], [mx, y], 1)
        pygame.draw.line(screen, black, [mx, y], [mx, my], 1)

        obsticle = pygame.draw.rect(screen, black, [500, 500, 550, 550])
        if obsticle.collidepoint(x + characterWidth, y):
            canMoveRight = False
        else:
            canMoveRight = True

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        if x <= characterWidth:
            x = characterWidth
        elif x >= screenWidth - characterWidth:
            x = screenWidth - characterWidth

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and canMoveRight:
            x += 3

        elif keys[pygame.K_a] and canMoveLeft:
            x -= 3

        if

        if fall and y < 790:
            y += fallSpeed
            fallSpeed += 1

        else:
            fallSpeed = 0
            y = 790


        pygame.display.flip()


drop()
