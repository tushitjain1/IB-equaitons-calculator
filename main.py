import pygame
from pygame.locals import *

class Calc:
    def __init__(self):
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 640)
        Calc.screen = pygame.display.set_mode(self.rect.size, self.flags)
        Calc.running = True

    def run(self):
        while Calc.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Calc.running = False
        pygame.quit()


if __name__ == '__main__':
    Calc().run()
