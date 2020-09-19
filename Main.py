import sys
import pygame
from Menu import Menu, SinglePlayerButton, MultiPlayerButton, OnlineButton, QuitButton, XSelectionButton, OSelectionButton, GridButton
from SinglePlayer import Player
pygame.init()
# helpfull functions
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def draw_grid(surface):
    pygame.draw.line(surface, BLACK, (350, 150), (350, 450), 5)
    pygame.draw.line(surface, BLACK, (450, 150), (450, 450), 5)
    pygame.draw.line(surface, BLACK, (250, 250), (550, 250), 5)
    pygame.draw.line(surface, BLACK, (250, 350), (550, 350), 5)
    '''# X
    pygame.draw.line(surface, (255, 0, 0), (350,150), (250, 250), 5)
    pygame.draw.line(surface, (255, 0, 0), (250, 150), (350, 250), 5)
    # O
    pygame.draw.circle(surface, (0, 0, 255), (400, 200), 48, 5)
    '''
# screen configuration
screen_size = width, height = 800, 600
pygame.display.set_caption('Tik Tak Toe')
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
# start screen menu
singleplayer = SinglePlayerButton('Single Player', 250, 100, 350, 60)
multiplayer = MultiPlayerButton('Multiplayer', 250, 200, 350, 60)
online = OnlineButton('Online', 250, 300, 350, 60)
leave = QuitButton('Quit', 250, 400, 350, 60)
menu = Menu(singleplayer, multiplayer, online, leave)
# singleplayer menu
x = XSelectionButton('X', 250, 200, 100, 100)
o = OSelectionButton('O', 450, 200, 100, 100)
character_menu = Menu(x, o)
# grid menu
grid_0_0 = GridButton('', 250, 150, 100, 100)
grid_0_1 = GridButton('', 350, 150, 100, 100)
grid_0_2 = GridButton('', 450, 150, 100, 100)
grid_1_0 = GridButton('', 250, 250, 100, 100)
grid_1_1 = GridButton('', 350, 250, 100, 100)
grid_1_2 = GridButton('', 450, 250, 100, 100)
grid_2_0 = GridButton('', 250, 350, 100, 100)
grid_2_1 = GridButton('', 350, 350, 100, 100)
grid_2_2 = GridButton('', 450, 350, 100, 100)
grid_menu = Menu(grid_0_0, grid_0_1, grid_0_2, grid_1_0, grid_1_1, grid_1_2, grid_2_0, grid_2_1, grid_2_2)
#

# game loop
run = True
while run:
    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not singleplayer.clicked:
            menu.update(event)
            menu.draw(screen)
        else:
            character_menu.update(event)
            screen.fill(WHITE)
            character_menu.draw(screen)
            if x.clicked:
                player = Player('X')
                screen.fill(WHITE)
                # Draw the board
                grid_menu.update(event)
                grid_menu.draw(screen, player)

                draw_grid(screen)

            if o.clicked:
                player = Player('O')
                screen.fill((0, 0, 0))
                grid_menu.draw(screen, player)

    pygame.display.update()
    CLOCK.tick()
pygame.quit()
