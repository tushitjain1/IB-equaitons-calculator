import pygame
from pygame.locals import *
import sys
import ctypes
import os
import math
from sideMenu import SideMenu, REDRAW_WINDOW
pygame.font.init()

# Default window sizes # Other possible sizes? idrk yet
SMALL = (880, 530)
MEDIUM = (1000, 650)
LARGE = (1270, 690)
WIDTH, HEIGHT = SMALL
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window title
pygame.display.set_caption("IB Equations Calculator")

# Colours
MAIN_COLOUR = (133, 220, 186)
SETTINGS_COLOUR = (226, 125, 96)
FRAME_COLOUR = (232, 168, 124)
OPTION_COLOUR = (50, 50, 50)
CALC_SCREEN = (228, 230, 230)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

# Fonts
BASICFONT = pygame.font.SysFont("Arial", 30)
TITLEFONT = pygame.font.SysFont("Arial", 50)
TITLE2FONT = pygame.font.SysFont("Arial", 40)
TITLEFONT2 = pygame.font.SysFont("Arial", 15)
CALCFONT = pygame.font.SysFont("Arial", 35)
# print(CALCFONT.render("test", 1, (0, 0, 0)).get_height())

# Other variables
FPS = 120

# Load images
ICON = pygame.image.load(os.path.join('icons', 'calc.png'))
SETTINGS = pygame.image.load(os.path.join('icons', 'settings.png'))
SETTINGS = pygame.transform.smoothscale(SETTINGS, (40, 40))
HAMTHREE = pygame.image.load(os.path.join('icons', 'hamthree.svg'))
HAMTHREE = pygame.transform.smoothscale(HAMTHREE, (50, 50))
CALCIMAGE = pygame.image.load(os.path.join('icons', 'calculatorart-01.png'))
CALCIMAGE = pygame.transform.smoothscale(CALCIMAGE, (390, 500))

# Set window icon
pygame.display.set_icon(ICON)

# Hamburger menu
option_rect = (0, 10, 370, 90)
ham_pos = (20, 10)
opts = ["Equation %i" %i for i in range(14)]
opts.insert(0, "Area of Parallelogram")
opts.insert(0, "Main")
ham = SideMenu(
    [(0, 0, 0), (0, 0, 0)],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    option_rect,
    BASICFONT,
    HAMTHREE, ham_pos, opts)
hamSurf = pygame.Surface((option_rect[2]+20, option_rect[3]*len(opts) + HEIGHT/2))

calcText = pygame.Surface((200, 41))
calcText.fill(CALC_SCREEN)


def main():
    clock = pygame.time.Clock()
    run = True
    scroll_y = HAMTHREE.get_height()
    windowNum = -1
    drawWindow(windowNum)
    numericString = ""
    num = ""
    show_settings = False
    while run:
        clock.tick(FPS)
        x, y = WIN.get_size()
        pygame.display.update()
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

            calcXScroll = handleCalcText(num, calcText)
            if not show_settings:
                WIN.blit(calcText, (x-275, y-370))

            if event.type == MOUSEBUTTONDOWN:
                clickx, clicky = event.pos
                # print(clickx, clicky)
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
                # Elif click was within the window but outside of a rectangle equal to the settings menu: redraw main
                elif pygame.Rect(0, 0, x, y).collidepoint(event.pos) and show_settings:
                        drawWindow(windowNum)
                        show_settings = False
                        hamSurf.set_alpha(100)
                # If click on a rect exactly the same as HAMTHREE icon, draw equations menu
                if event.button == 4 and ham.draw_menu: scroll_y = min(scroll_y + 15, 50)
                if event.button == 5 and ham.draw_menu: scroll_y = max(scroll_y - 15, - (option_rect[3]*len(opts)) + (y-(ham_pos[1] + HAMTHREE.get_height())))
                # If the click was within a rectangle at the same position as the caclulator png
                if pygame.Rect(x-312, y-445, 275, 410).collidepoint(event.pos) and not show_settings:
                    # Checking individual buttons
                    if pygame.Rect(x-280, y-298, 40, 40).collidepoint(event.pos):  # 7
                        numericString += "7"
                        num += "7"
                    elif pygame.Rect(x-221, y-298, 40, 40).collidepoint(event.pos):  # 8
                        numericString += "8"
                        num += "8"
                    elif pygame.Rect(x-162, y-298, 40, 40).collidepoint(event.pos):  # 9
                        numericString += "9"
                        num += "9"
                    elif pygame.Rect(x-103, y-298, 40, 40).collidepoint(event.pos):  # Plus
                        numericString += "+"
                        num += "+"
                    elif pygame.Rect(x-280, y-238, 40, 40).collidepoint(event.pos):  # 4
                        numericString += "4"
                        num += "4"
                    elif pygame.Rect(x-221, y-238, 40, 40).collidepoint(event.pos):  # 5
                        numericString += "5"
                        num += "5"
                    elif pygame.Rect(x-162, y-238, 40, 40).collidepoint(event.pos):  # 6
                        numericString += "6"
                        num += "6"
                    elif pygame.Rect(x-103, y-238, 40, 40).collidepoint(event.pos):  # Minus
                        numericString += "-"
                        num += "-"
                    elif pygame.Rect(x-280, y-178, 40, 40).collidepoint(event.pos):  # 1
                        numericString += "1"
                        num += "1"
                    elif pygame.Rect(x-221, y-178, 40, 40).collidepoint(event.pos):  # 2
                        numericString += "2"
                        num += "2"
                    elif pygame.Rect(x-162, y-178, 40, 40).collidepoint(event.pos):  # 3
                        numericString += "3"
                        num += "3"
                    elif pygame.Rect(x-103, y-178, 40, 40).collidepoint(event.pos):  # Times
                        numericString += "*"
                        num += "×"
                    elif pygame.Rect(x-280, y-118, 40, 40).collidepoint(event.pos):  # 0
                        numericString += "0"
                        num += "0"
                    elif pygame.Rect(x-221, y-118, 40, 40).collidepoint(event.pos):  # Point
                        numericString += "."
                        num += "."
                    elif pygame.Rect(x-162, y-118, 40, 40).collidepoint(event.pos):  # Equals to
                        num = str(calculator(numericString))
                        print(num)
                        # numericString = ""
                        numericString = str(num)
                    elif pygame.Rect(x-103, y-118, 40, 40).collidepoint(event.pos):  # Divide
                        numericString += "/"
                        num += "/"
                    elif pygame.Rect(x-281, y-66, 30, 25).collidepoint(event.pos):  # Pi
                        numericString += str(math.pi)
                        num += str(math.pi)
                    elif pygame.Rect(x-235, y-66, 30, 25).collidepoint(event.pos):  # To the power
                        numericString += "**"
                        num += "^"
                    elif pygame.Rect(x-187, y-66, 30, 25).collidepoint(event.pos):  # *10^y
                        numericString += "*10**"
                        num += "×10^"
                    elif pygame.Rect(x-142, y-66, 30, 25).collidepoint(event.pos):  # Open bracket
                        numericString += "("
                        num += "("
                    elif pygame.Rect(x-93, y-66, 30, 25).collidepoint(event.pos):  # Close bracket
                        numericString += ")"
                        num += ")"
                    elif pygame.Rect(x-274, y-414, 32, 22).collidepoint(event.pos):  # Clear
                        numericString = ""
                        num = ""

            if event.type == KEYDOWN:
                if event.key in [pygame.K_0, pygame.K_KP0]:
                    if event.mod-4096 in [pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT]:
                        numericString += ")"
                        num += ")"
                    else:
                        numericString += "0"
                        num += "0"
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    numericString += "1"
                    num += "1"
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    numericString += "2"
                    num += "2"
                if event.key in [pygame.K_3, pygame.K_KP3]:
                    numericString += "3"
                    num += "3"
                if event.key in [pygame.K_4, pygame.K_KP4]:
                    numericString += "4"
                    num += "4"
                if event.key in [pygame.K_5, pygame.K_KP5]:
                    numericString += "5"
                    num += "5"
                if event.key in [pygame.K_6, pygame.K_KP6]:
                    if event.mod-4096 in [pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT]:
                        numericString += "**"
                        num += "^"
                    else:
                        numericString += "6"
                        num += "6"
                if event.key in [pygame.K_7, pygame.K_KP7]:
                    numericString += "7"
                    num += "7"
                if event.key in [pygame.K_8, pygame.K_KP8]:
                    if event.mod-4096 in [pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT]:
                        numericString += "*"
                        num += "×"
                    else:
                        numericString += "8"
                        num += "8"
                if event.key in [pygame.K_9, pygame.K_KP9]:
                    if event.mod-4096 in [pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT]:
                        numericString += "("
                        num += "("
                    else:
                        numericString += "9"
                        num += "9"
                if event.key in [pygame.K_PLUS, pygame.K_KP_PLUS]:
                    numericString += "+"
                    num += "+"
                if event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                    numericString += "-"
                    num += "-"
                if event.key in [pygame.K_ASTERISK, pygame.K_KP_MULTIPLY]:
                    numericString += "*"
                    num += "×"
                if event.key in [pygame.K_SLASH, pygame.K_KP_DIVIDE]:
                    numericString += "/"
                    num += "/"
                if event.key in [pygame.K_PERIOD, pygame.K_KP_PERIOD]:
                    numericString += "."
                    num += "."
                if event.key in [pygame.K_LEFTPAREN, pygame.K_LEFTBRACKET]:
                    numericString += "("
                    num += "("
                if event.key in [pygame.K_RIGHTPAREN, pygame.K_RIGHTBRACKET]:
                    numericString += ")"
                    num += ")"
                if event.key == pygame.K_CARET:
                    numericString += "**"
                    num += "^"
                if event.key == pygame.K_BACKSPACE:
                    numericString = numericString[0:-1]
                    num = num[0:-1]
                if event.key in [pygame.K_RETURN, pygame.K_EQUALS, pygame.K_KP_ENTER, pygame.K_KP_EQUALS]:
                    if event.mod-4096 in [pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT]:
                        numericString += "+"
                        num += "+"
                    else:
                        num = str(calculator(numericString))
                        print(num)
                        # numericString = ""
                        numericString = str(num)

            if event.type == REDRAW_WINDOW: drawWindow(windowNum)
        selected_option = ham.update(event_list, scroll_y)
        if selected_option >= 0:
            opt = ham.options[selected_option]
            windowNum = selected_option
            print(opt)
        ham.draw(hamSurf)
        WIN.set_clip((0, ham_pos[1] + HAMTHREE.get_height(), x, y-(ham_pos[1] + HAMTHREE.get_height())))
        WIN.blit(hamSurf, hamSurf.get_rect(top=scroll_y))
        WIN.set_clip(None)

    pygame.quit()

# Draw the main window
def drawWindow(windowNum):
    x, y = WIN.get_size()
    WIN.fill(MAIN_COLOUR)
    hamSurf.fill(MAIN_COLOUR)
    WIN.blit(SETTINGS, (x-50, 10))
    WIN.blit(HAMTHREE, (20, 10))
    WIN.blit(CALCIMAGE, (x-375, y-500))
    clear = TITLEFONT2.render("Clear", 1, (0, 0, 0))
    WIN.blit(clear, (x-274, y-414))
    if (windowNum == 1):
        print("Display Area of Parallelogram Equation")
    pygame.display.update()

# Draw the settings window
def drawSettings(x, y):
    hamSurf.set_alpha(0)
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

# Changes the global variables to the new desired size
def resize(size, windowNum = 0):
    global WIDTH, HEIGHT, WIN, hamSurf
    WIDTH, HEIGHT = size
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    hamSurf = pygame.Surface((option_rect[2]+20, option_rect[3]*len(opts) + HEIGHT/2))
    drawWindow(windowNum)
    drawSettings(WIDTH, HEIGHT)

# Handles calculations
def calculator(string_input):
    symbs = ["+", "-", "/", "*"]
    if string_input == "" or string_input[-1] == "!":
        return 0
    i = 1
    while i < len(string_input) - 1:
        if string_input[i] == "(" and string_input[i-1] not in symbs:
            string_input = string_input[0:i] + "*" + string_input[i:]
        if string_input[i] == ")" and string_input[i+1] not in symbs:
            string_input = string_input[0:i+1] + "*" + string_input[i+1:]
        i += 1
    try:
        answer = eval(string_input)
    except SyntaxError:
        return "Syntax Error!"
    except ZeroDivisionError:
        return "Error!"
    if len(str(answer).replace(".", "")) > 4:
        length = min(len(str(answer))-1, 7)
        answer = format(answer, ".%sE" % length)
        ans = list(answer)
        e = ans.index("E")
        # answer = int(str(answer)[0:-2])
        if ans[e+2] == "0":
            ans.pop(e+2)
            e = ans.index("E")
        for i in range(e-1, 2, -1):
            if ans[i] != "0":
                break
            ans.pop(i)
        answer = "".join(ans)
    return answer

# Draws and handles calculator text
def handleCalcText(num, surf):
    text = CALCFONT.render(str(num), 1, (0, 0, 0))
    surf.fill(CALC_SCREEN)
    surf.blit(text, (0, 0, 0, 0))


# For Windows operating system, make a unique appid in order to show icon in taskbar
if sys.platform.startswith("win32"):
    appid = u'IBStudents.CAS.Project.EquationCalculator' # Unique string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

if __name__ == '__main__':
    main()
