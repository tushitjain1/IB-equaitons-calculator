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
        # surface.blit(self.main, self.main.get_rect(topleft=self.main_pos))
        if self.draw_menu:
            self.drawRects(surface)
            # print(surface.unmap_rgb(surface.get_at_mapped((0, 0))))
            # for i, text in enumerate(self.options):
            #     rect = self.rect.copy()
            #     rect.y += (i+1) * self.rect.height
                # pygame.draw.rect(surface, self.option_colour[1 if i == self.active_option else 0], rect, 0)
                # msg = self.font.render(text, 1, (0, 0, 0))
                # surface.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.main.get_rect(topleft=self.main_pos).collidepoint(mpos)
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i) * self.rect.height
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

    def drawRects(self, surface):
        for i, text in enumerate(self.options):
            rect = self.rect.copy()
            rect.y += (i) * self.rect.height
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

menuSurf = pygame.Surface((200, 900))
i_a = menuSurf.get_rect()
x1 = i_a[0]
x2 = x1 + i_a[2]
a, b = (255, 0, 0), (60, 255, 120)
y1 = i_a[1]
y2 = y1 + i_a[3]
h = y2-y1
rate = (float((b[0]-a[0])/h),
         (float(b[1]-a[1])/h),
         (float(b[2]-a[2])/h)
         )
# for line in range(y1,y2):
#      color = (min(max(a[0]+(rate[0]*line),0),255),
#               min(max(a[1]+(rate[1]*line),0),255),
#               min(max(a[2]+(rate[2]*line),0),255)
#               )
#      pygame.draw.line(menuSurf, color, (x1, line),(x2, line))

y = 20

scroll_y = 60

def drawWindow():
    screen.fill((255, 255, 255))
    menuSurf.fill((255, 255, 255))
    screen.blit(HAMTHREE, HAMTHREE.get_rect(topleft=(20, 10)))

drawWindow()
run = True
while run:
    clock.tick(60)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and list1.draw_menu: scroll_y = min(scroll_y + 15, 60)
            if event.button == 5 and list1.draw_menu: scroll_y = max(scroll_y - 15, -300)

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        opt = list1.options[selected_option]
        print(opt)

    # list1.draw(screen)
    drawWindow()
    list1.draw(menuSurf)
    screen.set_clip((0, 60, 640, 420))
    screen.blit(menuSurf, menuSurf.get_rect(top=scroll_y))
    screen.set_clip(None)
    pygame.display.flip()

pygame.quit()
exit()
