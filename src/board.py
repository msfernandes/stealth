# -*- coding: utf-8 -*-
from configs import (BOARD_LINES, BOARD_COLUMNS, WALLS, WALL_SIZE,
                     BOARD_UNITY_CENTER_X, BOARD_UNITY_CENTER_Y,
                     BOARD_UNITY_HEIGHT, BOARD_UNITY_WIDTH,
                     SCREEN_HEIGHT)
from cocos.layer import Layer
from sprites import WallSprite
import random


class Board(Layer):
    EMPTY = ' '
    WALL = 'W'

    HORIZONTAL = 3
    VERTICAL = 4

    def __init__(self):
        super(Board, self).__init__()
        self.board = []
        self.lines = BOARD_LINES
        self.columns = BOARD_COLUMNS
        self.walls = []
        self.__initialize_map()
        self.__create_limits()
        self.__create_walls()
        self.__create_sprites()
        self.__add_walls()

    def __initialize_map(self):
        for line in range(self.lines):
            line = []
            for column in range(self.columns):
                line.append(self.EMPTY)
            self.board.append(line)

    def __create_sprites(self):
        for i, line in enumerate(self.board):
            pos_y = SCREEN_HEIGHT - BOARD_UNITY_CENTER_Y - \
                (i * BOARD_UNITY_HEIGHT) + 178
            for j, column in enumerate(line):
                pos_x = BOARD_UNITY_CENTER_X + (j * BOARD_UNITY_WIDTH) + 195

                if self.board[i][j] == self.WALL:
                    wall = WallSprite(pos_x, pos_y)
                    self.walls.append(wall)

    def __add_walls(self):
        for wall in self.walls:
            self.add(wall)

    def __create_limits(self):
        for line_count, line in enumerate(self.board):
            for column_count, column in enumerate(line):
                if line_count == 0 or line_count == self.lines - 1:
                    self.board[line_count][column_count] = self.WALL

                if column_count == 0 or column_count == self.columns - 1:
                    self.board[line_count][column_count] = self.WALL

    def __create_walls(self):
        for wall in range(WALLS):
            orientation = random.choice([self.HORIZONTAL, self.VERTICAL])
            line = random.randint(2, self.lines - 1)
            column = random.randint(2, self.columns - 1)
            self.__create_wall(WALL_SIZE, orientation, line, column)

    def __create_wall(self, size, orientation, line, column):
        for i in range(size):
            self.board[line][column] = self.WALL
            if orientation is self.HORIZONTAL:
                column = column - 1
            else:
                line = line - 1

    def __str__(self):
        print_map = ''
        for line in self.board:
            print_line = ''
            for column in line:
                print_line += ' ' + str(column) + ' '

            print_line += '\n'
            print_map += print_line
        return print_map

if __name__ == '__main__':
    b = Board()
    print b
