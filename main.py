import pygame
from pygame.locals import *
import sys
import ctypes
import os
pygame.font.init()

# Default window sizes # Other possible sizes? idrk yet
SMALL = (880, 530)
MEDIUM = (1000, 650)
LARGE = (1280, 760)
WIDTH, HEIGHT = SMALL
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window title
pygame.display.set_caption("IB equations calculator")

# Colours
MAIN_COLOUR = (133,220,186)
SETTINGS_COLOUR = (226, 125, 96)
FRAME_COLOUR = (232,168,124)
OPTION_COLOUR = (50, 50, 50)

# Fonts
BASICFONT = pygame.font.SysFont("Arial", 30)
TITLEFONT = pygame.font.SysFont("Arial", 50)
TITLE2FONT = pygame.font.SysFont("Arial", 40)

# Other variables
FPS = 60

# Load images
ICON = pygame.image.load(os.path.join('icons', 'calc.png'))
SETTINGS = pygame.image.load(os.path.join('icons', 'settings.png'))
SETTINGS = pygame.transform.smoothscale(SETTINGS, (40, 40))
HAMTHREE = pygame.image.load(os.path.join('icons', 'hamthree.svg'))
HAMTHREE = pygame.transform.smoothscale(HAMTHREE, (50, 50))

# Set window icon
pygame.display.set_icon(ICON)


def main():
    clock = pygame.time.Clock()
    run = True
    drawWindow()
    show_settings = False
    while run:
        clock.tick(FPS)
        x, y = WIN.get_size()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                clickx, clicky = event.pos
                # If click on a rect exactly the same as SETTINGS icon, draw the settings menu
                if pygame.Rect(x-50, 10, 50, 50).collidepoint(event.pos) and not show_settings:
                    rect1, rect2, rect3 = drawSettings(x, y)
                    show_settings = True
                # Elif the click was in a rectangle equal to the settings menu...
                elif pygame.Rect(70, 85, x-140, y-170).collidepoint((clickx, clicky)) and show_settings:
                        if rect1.collidepoint(event.pos) and (x, y) != SMALL:
                            resize(SMALL)
                        if rect2.collidepoint(event.pos) and (x, y) != MEDIUM:
                            resize(MEDIUM)
                        if rect3.collidepoint(event.pos) and (x, y) != LARGE:
                            resize(LARGE)
                    # Elif the click was within the window but outside of a rectangle equal to the settings menu, redraw the normal window
                elif pygame.Rect(0, 0, x, y).collidepoint(event.pos) and show_settings:
                        drawWindow()
                        show_settings = False
                # If click on a rect exactly the same as HAMTHREE icon, draw equations menu
                if pygame.Rect(20, 10, 50, 50).collidepoint(event.pos):
                    print("HamThree")
                    drawHam()

    pygame.quit()

# Draw the main window
def drawWindow():
    x, y = WIN.get_size()
    WIN.fill(MAIN_COLOUR)
    WIN.blit(SETTINGS, (x-50, 10))
    WIN.blit(HAMTHREE, (20, 10))
    pygame.display.update()

# Draw the settings window
def drawSettings(x, y):
    settings = pygame.Rect(70, 85, x-140, y-170)
    frame = pygame.Rect(75, 90, x-150, y-180)
    pygame.draw.rect(WIN, SETTINGS_COLOUR, settings, 0)
    pygame.draw.rect(WIN, FRAME_COLOUR, frame, 0)

    title = TITLEFONT.render("Settings", 1, OPTION_COLOUR)
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, 90))

    set1 = TITLE2FONT.render("Window Size", 1, OPTION_COLOUR)
    WIN.blit(set1, (95, 160))

    opt1 = BASICFONT.render("Small", 1, OPTION_COLOUR)
    if (x, y) == SMALL: drawShowSelect(180 + 1.5*opt1.get_height())
    rect1 = pygame.Rect(120, 180 + opt1.get_height(), opt1.get_width(), opt1.get_height())
    WIN.blit(opt1, (120, 180 + opt1.get_height()))

    opt2 = BASICFONT.render("Medium", 1, OPTION_COLOUR)
    if (x, y) == MEDIUM: drawShowSelect(180 + 2.5*opt1.get_height())
    rect2 = pygame.Rect(120, 180 + 2*opt1.get_height(), opt2.get_width(), opt1.get_height())
    WIN.blit(opt2, (120, 180 + 2*opt1.get_height()))

    opt3 = BASICFONT.render("Large", 1, OPTION_COLOUR)
    if (x, y) == LARGE: drawShowSelect(180 + 3.5*opt1.get_height())
    rect3 = pygame.Rect(120, 180 + 3*opt1.get_height(), opt3.get_width(), opt1.get_height())
    WIN.blit(opt3, (120, 180 + 3*opt1.get_height()))
    return rect1, rect2, rect3

# Draws the circle to show which size is selected
def drawShowSelect(y):
    pygame.draw.circle(WIN, OPTION_COLOUR, (100, y + 2), 10)

def drawHam():
    pass

# Changes the global variables to the new desired size
def resize(size):
    global WIDTH, HEIGHT, WIN
    WIDTH, HEIGHT = size
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    drawWindow()
    drawSettings(WIDTH, HEIGHT)


if __name__ == '__main__':
    # For Windows operating system, make a unique appid in order to show icon in taskbar
    if sys.platform.startswith("win32"):
        appid = 'IBStudents.EquationCalculator.CASProject' # Unique string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    main()
