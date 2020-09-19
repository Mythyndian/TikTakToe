import pygame
import os

pygame.init()


class Player:
    def __init__(self, character):
        self.character = character
        self.placements = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.won = False
        self.image = pygame.image.load(os.path.join('png', self.character + '.png'))

    @staticmethod
    def draw(surface, rect):
        surface.blit(surface, rect)
