import sys
import pygame
import os
from Menu import Menu, SinglePlayerButton, MultiPlayerButton, OnlineButton, QuitButton, XSelectionButton, OSelectionButton, GridButton, GridMenu
from SinglePlayer import Player
pygame.init()
# helpfull functions
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
def draw_grid(surface):
    pygame.draw.line(surface, BLACK, (350, 150), (350, 450), 5)
    pygame.draw.line(surface, BLACK, (450, 150), (450, 450), 5)
    pygame.draw.line(surface, BLACK, (250, 250), (550, 250), 5)
    pygame.draw.line(surface, BLACK, (250, 350), (550, 350), 5)

def draw_win_line(surface, color, start_point, end_point, tickness=1):
    pygame.draw.line(surface,color, start_point, end_point, tickness)

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
menu_group = pygame.sprite.Group(singleplayer, multiplayer, online, leave)
menu = Menu(singleplayer, multiplayer, online, leave)
# singleplayer menu
x = XSelectionButton('X', 250, 50, 100, 100)
o = OSelectionButton('O', 450, 50, 100, 100)
x_o_group = pygame.sprite.Group(x, o)
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
grid_menu = GridMenu(grid_0_0, grid_0_1, grid_0_2, grid_1_0, grid_1_1, grid_1_2, grid_2_0, grid_2_1, grid_2_2)
#
player = Player()
# game loop
run = True
while run:
    # Getting events
    for event in pygame.event.get():
        screen.fill(WHITE)
        if event.type == pygame.QUIT:
            run = False
        if not singleplayer.clicked:
            menu.update(event)
            menu.draw(screen)
        else:
            for sprite in menu_group:
                sprite.kill()
            if not x.clicked or not x.clicked:
                character_menu.update(event)
                screen.fill(WHITE)
                character_menu.draw(screen)
            if x.clicked:
                for sprite in x_o_group:
                    sprite.kill()
                screen.fill(WHITE)
                player.set_character('X')

                if  not player.won:
                    player.rect_to_matrix()
                    if player.turn:
                        grid_menu.update(event, player, screen)
                        player.turn = False
                    else:
                        # AI making move
                        player.turn = True
                    grid_menu.draw(screen, player)
                    player.check_victory()
                    draw_grid(screen)
                    print(player.won)
                elif player._draw:
                    pass

                else:
                    grid_menu.draw(screen, player)
                    draw_grid(screen)
                    draw_win_line(screen, RED, player.victory_list[0], player.victory_list[1], 5)

                # AI making move

               #while not player.won:
            elif o.clicked:
                for sprite in x_o_group:
                    sprite.kill()
                screen.fill(WHITE)
                player.character = 'O'
                grid_menu.update(event, player, screen)
                grid_menu.draw(screen, player)
                draw_grid(screen)

    pygame.display.update()
    CLOCK.tick(10)
pygame.quit()
