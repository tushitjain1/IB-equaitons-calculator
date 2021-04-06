import pygame
from pygame.locals import *
import sys
import ctypes
import os
pygame.font.init()

# Default window sizes # Other possible sizes? idrk yet
SMALL = (1090, 650) # (900, 550)
MEDIUM = (1440, 800) # (1200, 680)
LARGE = (2300, 1280) # (1920, 1125)
WIDTH, HEIGHT = MEDIUM
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window title
pygame.display.set_caption("IB equations calculator")

# Colours
MAIN_COLOUR = (169, 192, 226)
SETTINGS_COLOUR = (214, 240, 234)
OPTION_COLOUR = (50, 50, 50)
SELECTED_COLOUR = (90, 90, 90)

# Fonts
BASICFONT = pygame.font.SysFont('notosans', 30)
TITLEFONT = pygame.font.SysFont('notosans', 50)
TITLE2FONT = pygame.font.SysFont('notosans', 40)

# Other variables
FPS = 60
SHOW_SETTINGS = False

# Load images
ICON = pygame.image.load(os.path.join('icons', 'calc.png'))
SETTINGS = pygame.image.load(os.path.join('icons', 'settings.png'))
SETTINGS = pygame.transform.smoothscale(SETTINGS, (40, 40))
HAMTHREE = pygame.image.load(os.path.join('icons', 'hamthree.svg'))
HAMTHREE = pygame.transform.smoothscale(HAMTHREE, (50, 50))

# Set window icon
pygame.display.set_icon(ICON)


def main():
    global SHOW_SETTINGS
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
                # If click on a rect exactly the same as SETTINGS icon, draw the settings menu
                if pygame.Rect(x-50, 10, 50, 50).collidepoint(event.pos) and not SHOW_SETTINGS:
                    rect1, rect2, rect3 = drawSettings(x, y)
                # Elif the click was in a rectangle equal to the settings menu...
                elif pygame.Rect(70, 85, x-140, y-170).collidepoint((clickx, clicky)) and SHOW_SETTINGS:
                    if rect1.collidepoint(event.pos) and (x, y) != SMALL:
                        resize(SMALL)
                    if rect2.collidepoint(event.pos) and (x, y) != MEDIUM:
                        resize(MEDIUM)
                    if rect3.collidepoint(event.pos) and (x, y) != LARGE:
                        resize(LARGE)
                # Elif the click was within the window but outside of a rectangle equal to the settings menu, redraw the normal window
                elif pygame.Rect(0, 0, x, y).collidepoint(event.pos) and SHOW_SETTINGS:
                    drawWindow()
                    SHOW_SETTINGS = False
                # If click on a rect exactly the same as HAMTHREE icon, draw equations menu
                if pygame.Rect(20, 10, 50, 50).collidepoint(event.pos):
                    print("HamThree")

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
    global SHOW_SETTINGS
    SHOW_SETTINGS = True
    settings = pygame.Rect(70, 85, x-140, y-170)
    pygame.draw.rect(WIN, SETTINGS_COLOUR, settings, 0)

    title = TITLEFONT.render("Settings", 1, (0, 0, 0))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, 85))

    set1 = TITLE2FONT.render("Window Size", 1, (25, 25, 25))
    WIN.blit(set1, (95, 160))

    opt1 = BASICFONT.render("Small", 1, OPTION_COLOUR)
    drawShowSelect(180 + 1.5*opt1.get_height()) if (x, y) == SMALL else ""
    rect1 = pygame.Rect(120, 180 + opt1.get_height(), opt1.get_width(), opt1.get_height())
    WIN.blit(opt1, (120, 180 + opt1.get_height()))

    opt2 = BASICFONT.render("Medium", 1, OPTION_COLOUR)
    drawShowSelect(180 + 2.5*opt1.get_height()) if (x, y) == MEDIUM else ""
    rect2 = pygame.Rect(120, 180 + 2*opt1.get_height(), opt2.get_width(), opt1.get_height())
    WIN.blit(opt2, (120, 180 + 2*opt1.get_height()))

    opt3 = BASICFONT.render("Large", 1, OPTION_COLOUR)
    drawShowSelect(180 + 3.5*opt1.get_height()) if (x, y) == LARGE else ""
    rect3 = pygame.Rect(120, 180 + 3*opt1.get_height(), opt3.get_width(), opt1.get_height())
    WIN.blit(opt3, (120, 180 + 3*opt1.get_height()))
    return rect1, rect2, rect3

# Draws the circle to show which size is selected
def drawShowSelect(y):
    pygame.draw.circle(WIN, SELECTED_COLOUR, (100, y + 2), 10)

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
