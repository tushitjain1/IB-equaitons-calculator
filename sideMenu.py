import pygame

class SideMenu():

    def __init__(self, menu_colour, option_colour, option_size, font, main, main_pos, options):
        self.menu_colour = menu_colour
        self.option_colour = option_colour
        self.rect = pygame.Rect(option_size)
        self.font = font
        self.main = main
        self.main_pos = main_pos
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.right = -option_size[2]

    def draw(self, surface):
        # pygame.draw.rect(surface, self.menu_colour[self.menu_active], self.rect, 0)
        # surface.blit(self.main, self.main.get_rect(topleft=self.main_pos))
        if self.draw_menu:
            if self.right < self.rect.x:
                self.right += 5
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i) * self.rect.height
                rect.x = self.right
                pygame.draw.rect(surface, self.option_colour[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surface.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list, scroll_y):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.main.get_rect(topleft=self.main_pos).collidepoint(mpos)
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += ((i) * self.rect.height) + scroll_y
            if rect.collidepoint(mpos):
                self.active_option = i
                break
        if not self.menu_active and self.active_option == -1 and self.draw_menu:
            self.draw_menu = False
            pygame.event.post(pygame.event.Event(REDRAW_WINDOW))
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                    self.right = -self.rect.w
                    pygame.event.post(pygame.event.Event(REDRAW_WINDOW))
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    pygame.event.post(pygame.event.Event(REDRAW_WINDOW))
                    return self.active_option
        return -1

REDRAW_WINDOW = pygame.USEREVENT + 1


if __name__ == "__main__":
    def drawWindow():
        screen.fill((255, 255, 255))
        menuSurf.fill((255, 255, 255))
        screen.blit(HAMTHREE, HAMTHREE.get_rect(topleft=(20, 10)))

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480))
    x, y = screen.get_size()

    HAMTHREE = pygame.image.load('./icons/hamthree.svg')
    HAMTHREE = pygame.transform.smoothscale(HAMTHREE, (50, 50))

    COLOR_INACTIVE = (100, 80, 255)
    COLOR_ACTIVE = (100, 200, 255)
    COLOR_LIST_INACTIVE = (255, 100, 100)
    COLOR_LIST_ACTIVE = (255, 150, 150)

    option_rect = (0, 10, 200, 90)
    main_pos = (20, 10)
    opts = ["Equation %i" %i for i in range(15)]

    list1 = SideMenu(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        option_rect,
        pygame.font.SysFont(None, 30),
        HAMTHREE, main_pos, opts)

    menuSurf = pygame.Surface((option_rect[2]+20, option_rect[3]*len(opts) + y/2))

    scroll_y = HAMTHREE.get_height()

    drawWindow()
    run = True
    while run:
        clock.tick(120)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and list1.draw_menu: scroll_y = min(scroll_y + 15, 50)
                if event.button == 5 and list1.draw_menu: scroll_y = max(scroll_y - 15, -(option_rect[3]*len(opts)) + (y-(main_pos[1] + HAMTHREE.get_height())))
            if event.type == REDRAW_WINDOW:
                drawWindow()

        selected_option = list1.update(event_list, scroll_y)
        if selected_option >= 0:
            opt = list1.options[selected_option]
            print(opt)

        list1.draw(menuSurf)
        screen.set_clip((0, main_pos[1] + HAMTHREE.get_height(), x, y-(main_pos[1] + HAMTHREE.get_height())))
        screen.blit(menuSurf, menuSurf.get_rect(top=scroll_y))
        screen.set_clip(None)
        pygame.display.flip()

    pygame.quit()
    exit()
