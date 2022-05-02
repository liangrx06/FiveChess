import sys
from time import sleep

import pygame

from settings import *
from game_stats import GameStats
from chess_board import ChessBoard, Chess
from chess_data import ChessData, check_point_legal
from ai import AI


class FiveChessGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("五子棋")

        self.stats = GameStats(self)

        self.line_points = LINE_POINTS
        self.chess_data = ChessData(self)

        self.chess_board = ChessBoard(self)

        self.chesses = pygame.sprite.Group()
        self.prep_chess = Chess(self, 0, [0, 0])

        self.ai = AI(self)

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                # self.chess_board.update()
                self.chesses.update()
                self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif self.stats.cur_side == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._check_mousebuttondown_events(pygame.mouse.get_pos())
                # elif event.type == pygame.MOUSEMOTION:
                #     self._check_mousemotton_events(pygame.mouse.get_pos())
            else:
                point = self.ai.AI_drop()
                cur_side = self.stats.cur_side
                chess = Chess(self, cur_side, point)
                self.chesses.add(chess)
                self.stats.change_side()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RETURN and not self.stats.game_active:
            self.stats.reset_stats()
            self.chess_data.reset_stats()
            for chess in self.chesses.copy():
                self.chesses.remove(chess)

    def _check_keyup_events(self, event):
        pass

    def _check_mousebuttondown_events(self, pos):
        point = self._get_point(pos)
        # print(point)
        if point is not None and self.chess_data.can_drop(point):
            cur_side = self.stats.cur_side
            self.chess_data.drop(cur_side, point)
            chess = Chess(self, cur_side, point)
            self.chesses.add(chess)
            self.stats.change_side()

    def _check_mousemotton_events(self, pos):
        point = self._get_point(pos)
        # print(point)
        if point is not None and self.chess_data.can_drop(point):
            self.prep_chess.set_side(self.stats.cur_side)
            self.prep_chess.set_point(point)
        else:
            self.prep_chess.set_side(0)

    def _get_point(self, pos):
        x = pos[0] - START_X
        y = pos[1] - START_Y
        width = WIDTH
        radius = RADIUS
        line_points = LINE_POINTS
        i = x // width
        j = y // width
        point = None
        for k1 in range(2):
            for k2 in range(2):
                ii = i + k1
                jj = j + k2
                if check_point_legal((ii, jj)):
                    iw = ii * width
                    jw = jj * width
                    if (iw - x) * (iw - x) + (jw - y) * (jw - y) <= radius * radius:
                        point = [i + k1, j + k2]
        return point

    def _update_screen(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.chess_board.draw_chess_board()
        for chess in self.chesses:
            chess.draw()
        self.prep_chess.draw()

        if self.stats.winner != 0:
            # print('Win:', self.stats.winner)
            self.stats.scores[self.stats.winner - 1] += 1
            # print(self.stats.scores)
            self.chess_board.print_win_msg()
            self.stats.game_active = False
        self.chess_board.draw_left_info()

        pygame.display.flip()


if __name__ == "__main__":
    game = FiveChessGame()
    game.run_game()
