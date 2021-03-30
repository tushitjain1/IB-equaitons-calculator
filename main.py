import pygame
from pygame.locals import *
import sys
import ctypes

class Calc:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.BASICFONT = pygame.font.SysFont('notosans', 30)
        self.TITLEFONT = pygame.font.SysFont('notosans', 50)
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 900, 650)
        Calc.screen = pygame.display.set_mode(self.rect.size, self.flags)
        pygame.display.flip()
        pygame.display.set_caption("IB equations calculator")
        icon = pygame.image.load("./icons/calc.png")
        pygame.display.set_icon(icon)
        Calc.screen.fill(Color(214, 240, 234))

        Calc.running = True

    def run(self):
        settings = pygame.Surface((0, 0))
        while Calc.running:
            # Calc.screen.fill(Color(214, 240, 234))
            x, y = Calc.screen.get_size()
            area = pygame.Rect(x - 51, 12, 40, 40)
            menu = pygame.image.load("icons/settings.png")
            menu = pygame.transform.smoothscale(menu, (40, 40))
            Calc.screen.blit(menu, (x - 50, 10))
            area_two = pygame.Rect(25, 12, 43, 43)
            opts = pygame.image.load("icons/hamthree.svg")
            opts = pygame.transform.smoothscale(opts, (50, 50))
            Calc.screen.blit(opts, (20, 10))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    Calc.running = False
                if event.type == VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), self.flags)
                    Calc.screen.fill(Color(214, 240, 234))
                mousex, mousey = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                    clickx, clicky = event.pos
                    if area.collidepoint(event.pos):
                        settings = self.settings()
                        # print(Calc.screen.get_size())
                    elif (pygame.Rect(0, 0, x, y).collidepoint(event.pos)) and (not settings.get_rect().collidepoint((clickx-70, clicky-85))):
                        Calc.screen.fill(Color(214, 240, 234))
                    if area_two.collidepoint(event.pos):
                        pass

    def settings(self):
        w, h = pygame.display.get_surface().get_size()
        settings = pygame.Surface((w-140, h-170))
        settings.fill(Color(20, 201, 199))
        # Calc.screen.blit(settings, (70, 85))
        top = 70
        left = 85
        textSurf = self.TITLEFONT.render("Size", 1, Color('black'))
        textRect = textSurf.get_rect()
        textRect.top = top
        textRect.left = left
        top += pygame.font.Font.get_linesize(self.TITLEFONT)+15
        settings.blit(textSurf, textRect)
        options = ['Small', 'Medium', 'Large']
        for i in range(len(options)):
            textSurf = self.BASICFONT.render(options[i], 1, Color('black'))
            textRect = textSurf.get_rect()
            textRect.top = top
            textRect.left = left
            top += pygame.font.Font.get_linesize(self.TITLEFONT)-10
            settings.blit(textSurf, textRect)
        popupRect = settings.get_rect()
        popupRect.centerx = w/2
        popupRect.centery = h/2
        Calc.screen.blit(settings, popupRect)
        pygame.display.update()
        return settings


if __name__ == '__main__':
    if sys.platform.startswith("win32"):
        appid = 'IBStudents.EquationCalculator.CASProject' # Unique string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    Calc().run()
