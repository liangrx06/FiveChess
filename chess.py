import pygame
import pygame.gfxdraw
from pygame.sprite import Sprite

from settings import *

class Chess(Sprite):
    def __init__(self, ai_game, side, point):
        super().__init__()
        self.screen = ai_game.screen

        self.set_side(side)
        self.set_point(point)

    def set_side(self, side):
        self.side = side
        self.color = BLACK_COLOR if self.side == 1 else WHITE_COLOR

    def set_point(self, point):
        self.i, self.j = point

    def update(self):
        pass

    def draw(self):
        if self.side == 0:
            return

        self.draw_filled_circle(START_X + WIDTH * self.i, START_Y + WIDTH * self.j, RADIUS, self.color)

    def draw_filled_circle(self, x, y, r, color):
        pygame.gfxdraw.aacircle(self.screen, x, y, r, color)
        pygame.gfxdraw.filled_circle(self.screen, x, y, r, color)