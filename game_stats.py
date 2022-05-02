import pygame

from settings import *


class GameStats:
    def __init__(self, game):
        self.scores = [0, 0]

        self.reset_stats()

    def reset_stats(self):
        self.game_active = True
        self.cur_side = 1
        self.winner = 0

    def change_side(self):
        self.cur_side = 3 - self.cur_side

