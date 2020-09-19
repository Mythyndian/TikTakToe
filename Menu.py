import pygame

pygame.init()


class MenuButton:
    def __init__(self, text, pos_x, pos_y, width, height):
        self.name = text
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.color = (255, 0, 0)
        self.font = 'Font/pixelated.ttf'
        self.clicked = False

    def draw(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, outline,
                             (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4), 0)

        pygame.draw.rect(surface, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 0)

        if self.name != '':
            font = pygame.font.Font(self.font, 60)
            text = font.render(self.name, 1, (0, 0, 0))
            surface.blit(text, (
                self.rect.x + (self.rect.width / 2 - text.get_width() / 2),
                self.rect.y + (self.rect.height / 2 - text.get_height() / 2)))

    def is_over(self, position):
        if self.rect.x < position[0] < self.rect.x + self.rect.width:
            if self.rect.y < position[1] < self.rect.y + self.rect.height:
                return True

    def update(self, event):
        position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over(position):
                self.clicked = True
        if event.type == pygame.MOUSEMOTION:
            if self.is_over(position):
                self.color = (0, 0, 255)
            else:
                self.color = (255, 0, 0)


class Menu:
    def __init__(self, *args):
        self.buttons = args

    def draw(self, surface, player=None):
        for button in self.buttons:
            button.draw(surface)

    def update(self, event):
        for button in self.buttons:
            button.update(event)


class SinglePlayerButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)


class MultiPlayerButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)


class OnlineButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)


class QuitButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)


class XSelectionButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)

    def action(self, surface):
        # Start game as O
        pass


class OSelectionButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)


class GridButton(MenuButton):
    def __init__(self, text, pos_x, pos_y, width, height):
        super().__init__(text, pos_x, pos_y, width, height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.text = text

    def update(self, event):
        position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over(position):
                self.clicked = True

        if event.type == pygame.MOUSEMOTION:
            if self.is_over(position):
                self.color = (161, 161, 191)
            else:
                self.color = (255, 255, 255)

    def draw(self, surface, player=None, outline=None):
        if outline:
            pygame.draw.rect(surface, outline,
                             (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4), 0)

        pygame.draw.rect(surface, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 0)

        if player and self.clicked:
            surface.blit(player.image, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))



class GridMenu(Menu):
    def __init__(self, *args):
        super().__init__(self, *args)

    def draw(self, surface, player=None):
        for button in self.buttons:
            button.draw(surface, player)

    def update(self, event):
        for button in self.buttons:
            button.update(event)
