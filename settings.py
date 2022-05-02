import pygame

BACKGROUND_COLOR = (0XE3, 0X92, 0X65)  # 棋盘颜色
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (200, 30, 30)
BLUE_COLOR = (30, 30, 200)

WIDTH = 30  # 棋盘每个点之间的间隔
LINE_POINTS = 19  # 棋盘每行/每列点数
OUTER_WIDTH = 20  # 棋盘外宽度
BORDER_WIDTH = 4  # 边框宽度
INSIDE_WIDTH = 4  # 边框跟实际的棋盘之间的间隔

BORDER_LENGTH = WIDTH * (LINE_POINTS - 1) + INSIDE_WIDTH * 2 + BORDER_WIDTH  # 边框线的长度
START_Y = OUTER_WIDTH + int(BORDER_WIDTH / 2) + INSIDE_WIDTH  # 网格线起点（左上角）坐标
START_X = START_Y
SCREEN_HEIGHT = WIDTH * (LINE_POINTS - 1) + OUTER_WIDTH * 2 + BORDER_WIDTH + INSIDE_WIDTH * 2  # 游戏屏幕的高
SCREEN_WIDTH = SCREEN_HEIGHT + 150  # 游戏屏幕的宽

RADIUS = WIDTH // 2 - 3  # 棋子半径
RADIUS2 = WIDTH // 2 + 3

RIGHT_INFO_POS_X = SCREEN_HEIGHT + RADIUS2 * 2 + 10

pygame.init()
FONT1 = pygame.font.SysFont('SimHei', 32)
FONT2 = pygame.font.SysFont('SimHei', 72)

OFFSET = [[0, 1], [1, 0], [1, 1], [1, -1]]