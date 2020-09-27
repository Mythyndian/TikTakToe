import pygame
import os

pygame.init()


class Player:
    def __init__(self):
        self.character = ''
        self.moves = []
        self.won = False
        self._draw = False
        self.character = ''
        self.image = ''
        self.matrix = None
        self.victory_list = []
        self.turn = True

    def draw(self, surface, rect):
        surface.blit(surface, rect)

    def set_character(self, character):
        self.character = character
        self.image = pygame.image.load(os.path.join('png', character + '.png'))

    def rect_to_matrix(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        for move in self.moves:
            if move.x == 250 and move.y == 150:
                matrix[0][0] = 1
            if move.x == 350 and move.y == 150:
                matrix[0][1] = 1
            if move.x == 450 and move.y == 150:
                matrix[0][2] = 1
            if move.x == 250 and move.y == 250:
                matrix[1][0] = 1
            if move.x == 350 and move.y == 250:
                matrix[1][1] = 1
            if move.x == 450 and move.y == 250:
                matrix[1][2] = 1
            if move.x == 250 and move.y == 350:
                matrix[2][0] = 1
            if move.x == 350 and move.y == 350:
                matrix[2][1] = 1
            if move.x == 450 and move.y == 350:
                matrix[2][2] = 1
        self.matrix = matrix

    def check_victory(self):
        if self.matrix[0][0] and self.matrix[0][1] and self.matrix[0][2]:
            self.won = True
            self.victory_list = [(250, 150 + 50), (550, 150 + 50)]

        elif self.matrix[1][0] and self.matrix[1][1] and self.matrix[1][2]:
            self.won = True
            self.victory_list = [(250, 200 + 50), (550, 200 + 50)]

        elif self.matrix[2][0] and self.matrix[2][1] and self.matrix[2][2]:
            self.won = True
            self.victory_list = [(250, 350 + 50), (550, 350 + 50)]

        elif self.matrix[0][0] and self.matrix[1][0] and self.matrix[2][0]:
            self.won = True
            self.victory_list = [(300, 150), (300, 450)]

        elif self.matrix[0][1] and self.matrix[1][1] and self.matrix[2][1]:
            self.won = True
            self.victory_list = [(400, 150), (400, 450)]

        elif self.matrix[0][2] and self.matrix[1][2] and self.matrix[2][2]:
            self.won = True
            self.victory_list = [(500, 150), (500, 450)]

        elif self.matrix[0][0] and self.matrix[1][1] and self.matrix[2][2]:
            self.won = True
            self.victory_list = [(250, 150), (550, 450)]

        elif self.matrix[2][0] and self.matrix[1][1] and self.matrix[0][2]:
            self.won = True
            self.victory_list = [(550, 150), (250, 450)]
        else:
            self._draw = False


class AI:
    def __init__(self):
        self.move_list = []
        self.moves = []

    def obtain_player_moves(self, move_list):
        self.move_list = move_list
