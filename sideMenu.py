import pygame
from time import sleep
from main import *

class SideMenu():

    def __init__(self, menu_colour, option_colour, x, y, w, h, font, main, main_pos, options):
        self.menu_colour = menu_colour
        self.option_colour = option_colour
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.main_pos = main_pos
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surface):
        # pygame.draw.rect(surface, self.menu_colour[self.menu_active], self.rect, 0)
        surface.blit(self.main, self.main.get_rect(topleft=self.main_pos))
        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                # pygame.draw.rect(surface, self.option_colour[1 if i == self.active_option else 0], rect, 0)
                # msg = self.font.render(text, 1, (0, 0, 0))
                # surface.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.main.get_rect(topleft=self.main_pos).collidepoint(mpos)
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break
        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

    def handleRects(rect, opt_colour, selected_opt_colour):
        for i, text in enumerate(self.options):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            pygame.draw.rect(surface, self.option_colour[1 if i == self.active_option else 0], rect, 0)
            msg = self.font.render(text, 1, (0, 0, 0))
            surface.blit(msg, msg.get_rect(center = rect.center))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

list1 = SideMenu(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    20, 10, 200, 50,
    pygame.font.SysFont(None, 30),
    HAMTHREE, (20, 10), ["Equation %i" %i for i in range(10)])

run = True
while run:
    clock.tick(60)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        opt = list1.options[selected_option]
        print(opt)

    screen.fill((255, 255, 255))
    list1.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()
