import pygame
from pygame.locals import *
import sys
import ctypes
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IB equations calculator")

MAIN_COLOR = (169, 192, 226)
SETTINGS_COLOR = (214, 240, 234)

FPS = 60

ICON = pygame.image.load(os.path.join('icons', 'calc.png'))
SETTINGS = pygame.image.load(os.path.join('icons', 'settings.png'))
SETTINGS = pygame.transform.smoothscale(SETTINGS, (40, 40))
HAMTHREE = pygame.image.load(os.path.join('icons', 'hamthree.svg'))
HAMTHREE = pygame.transform.smoothscale(HAMTHREE, (50, 50))

pygame.display.set_icon(ICON)


def main():
    clock = pygame.time.Clock()
    run = True
    drawWindow()
    while run:
        clock.tick(FPS)
        x, y = WIN.get_size()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                clickx, clicky = event.pos
                if pygame.Rect(x-50, 10, 50, 50).collidepoint(event.pos):
                    settings = drawSettings(x, y)
                elif (pygame.Rect(0, 0, x, y).collidepoint(event.pos)) and (not settings.collidepoint((clickx, clicky))):
                        drawWindow()
                if pygame.Rect(20, 10, 50, 50).collidepoint(event.pos):
                    print("HamThree")
    pygame.quit()

def drawWindow():
    x, y = WIN.get_size()
    WIN.fill(MAIN_COLOR)
    WIN.blit(SETTINGS, (x-50, 10))
    WIN.blit(HAMTHREE, (20, 10))
    pygame.display.update()

def drawSettings(x, y):
    settings = pygame.Rect(85, 70, x-140, y-170)
    pygame.draw.rect(WIN, SETTINGS_COLOR, settings, 0)
    return settings

if __name__ == '__main__':
    if sys.platform.startswith("win32"):
        appid = 'IBStudents.EquationCalculator.CASProject' # Unique string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    main()
