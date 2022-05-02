import random

from settings import *
from chess_data import check_point_legal

class AI:
    def __init__(self, game):
        self.game = game
        self.chess_data = game.chess_data
        self.mat = self.chess_data.mat
        self.side = 2
        self.opponent = 3 - self.side

    def AI_drop(self):
        point = None
        score = 0
        for i in range(LINE_POINTS):
            for j in range(LINE_POINTS):
                if self.chess_data.can_drop((i, j)):
                    _score = self._get_point_score((i, j))
                    if _score > score:
                        score = _score
                        point = (i, j)
                    elif _score == score and _score > 0:
                        r = random.randint(0, 100)
                        if r % 2 == 0:
                            point = (i, j)
        # print(point)
        self.chess_data.drop(self.side, point)
        return point

    def _get_point_score(self, point):
        score = 0
        for os in OFFSET:
            score += self._get_direction_score(point, os[0], os[1])
        return score

    def _get_direction_score(self, point, x_offset, y_offset):
        count = 0   # 落子处我方连续子数
        _count = 0  # 落子处对方连续子数
        space = None   # 我方连续子中有无空格
        _space = None  # 对方连续子中有无空格
        both = 0    # 我方连续子两端有无阻挡
        _both = 0   # 对方连续子两端有无阻挡

        # 如果是 1 表示是边上是我方子，2 表示敌方子
        flag = self._get_stone_color(point, x_offset, y_offset, True)
        if flag != 0:
            for direction in [-1, 1]:
                for step in range(1, 6):
                    x = point[0] + step * x_offset * direction
                    y = point[1] + step * y_offset * direction
                    if check_point_legal((x, y)):
                        if flag == 1:
                            if self.mat[x][y] == self.side:
                                count += 1
                                if space is False:
                                    space = True
                            elif self.mat[x][y] == self.opponent:
                                _both += 1
                                break
                            else:
                                if space is None:
                                    space = False
                                else:
                                    break   # 遇到第二个空格退出
                        elif flag == 2:
                            if self.mat[x][y] == self.side:
                                _both += 1
                                break
                            elif self.mat[x][y] == self.opponent:
                                _count += 1
                                if _space is False:
                                    _space = True
                            else:
                                if _space is None:
                                    _space = False
                                else:
                                    break
                    else:
                        # 遇到边也就是阻挡
                        if flag == 1:
                            both += 1
                        elif flag == 2:
                            _both += 1

        if space is False:
            space = None
        if _space is False:
            _space = None

        score = 0
        if count == 4:
            score = 10000
        elif _count == 4:
            score = 9000
        elif count == 3:
            if both == 0:
                score = 1000
            elif both == 1:
                score = 100
            else:
                score = 0
        elif _count == 3:
            if _both == 0:
                score = 900
            elif _both == 1:
                score = 90
            else:
                score = 0
        elif count == 2:
            if both == 0:
                score = 100
            elif both == 1:
                score = 10
            else:
                score = 0
        elif _count == 2:
            if _both == 0:
                score = 90
            elif _both == 1:
                score = 9
            else:
                score = 0
        elif count == 1:
            score = 10
        elif _count == 1:
            score = 9
        else:
            score = 0

        if space or _space:
            score /= 2

        return score

    # 判断指定位置处在指定方向上是我方子、对方子、空
    def _get_stone_color(self, point, x_offset, y_offset, next):
        x = point[0] + x_offset
        y = point[1] + y_offset
        if check_point_legal((x, y)):
            if self.mat[x][y] == self.side:
                return 1
            elif self.mat[x][y] == self.opponent:
                return 2
            else:
                if next:
                    return self._get_stone_color((x, y), x_offset, y_offset, False)
                else:
                    return 0
        else:
            return 0