import pygame

from settings import *


class ChessData:
    def __init__(self, game):
        self.game = game
        self.stats = game.stats

        self.reset_stats()

    def reset_stats(self):
        self.mat = [[0] * LINE_POINTS for _ in range(LINE_POINTS)]
        pass

    def get_side(self, point):
        return self.mat[point[0]][point[1]]

    def set_side(self, side, point):
        self.mat[point[0]][point[1]] = side

    def can_drop(self, point):
        return self.get_side(point) == 0

    def drop(self, side, point):
        self.set_side(side, point)
        side_str = "黑方" if side == 1 else "白方"
        print(side_str + ":", tuple(point))
        self.stats.winner = self.check_win(point)

    def check_win(self, point):
        cur_side = self.get_side(point)
        if cur_side == 0:
            return 0
        for k in OFFSET:
            count = 1
            for m in range(1, 5):
                p = [point[0] + k[0] * m, point[1] + k[1] * m]
                if not check_point_legal(p) or self.get_side(p) != cur_side:
                    break
                count += 1
            for m in range(1, 5):
                p = [point[0] - k[0] * m, point[1] - k[1] * m]
                if not check_point_legal(p) or self.get_side(p) != cur_side:
                    break
                count += 1
            if count >= 5:
                return cur_side
        return 0

def check_point_legal(point):
    i, j = point
    return 0 <= i < LINE_POINTS and 0 <= j < LINE_POINTS
