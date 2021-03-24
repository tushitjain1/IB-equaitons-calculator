import pygame
from pygame.locals import *
import sys
import ctypes

class Calc:
    def __init__(self):
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 900, 650)
        Calc.screen = pygame.display.set_mode(self.rect.size, self.flags)
        pygame.display.flip()
        pygame.display.set_caption("IB equations calculator")
        icon = pygame.image.load("./icons/calc.png")
        pygame.display.set_icon(icon)


        Calc.running = True

    def run(self):
        while Calc.running:
            Calc.screen.fill(Color(214,240,234))
            menu = pygame.image.load("icons/hamtwo.png")
            menu = pygame.transform.smoothscale(menu, (40,40))
            x,y = Calc.screen.get_size()
            Calc.screen.blit(menu, (x - 50,10))
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == QUIT:
                    Calc.running = False
                if event.type == VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), self.flags)
        pygame.quit()


if __name__ == '__main__':
    appid = 'IBStudents.EquationCalculator.CASProject' # Unique string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    Calc().run()
