"""
Course: CSE 251
Lesson Week: 08
File: maze.py
Author: Brother Comeau
Purpose: Maze class for assignment 08 and 09

*******************************************************************************
*                                Do Not Change                                *
*******************************************************************************

Instructions:

- You can only call the method that don't begin wih a '_' character

"""

import numpy as np
import random
import time
import os, sys

import cv2


COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_VISITED = (128, 128, 128)

OPEN = 1
WALL = 2
VISITED = 3

class Maze():

    def __init__(self, screen, width, height, bitmap_file, delay=False):
        super().__init__()
        self._screen = screen
        self._filename = bitmap_file
        self._screen_w = width
        self._screen_h = height
        self._delay = delay

        # numpy array
        if not os.path.exists(bitmap_file):
            print('\n' * 2, '*' * 50)
            print(f'Bitmap file {bitmap_file} not found.')
            print('1) Make sure you are only opening the folder with your \n   assignment files in VSCode')
            print('2) Make sure you have the 10 bitmap files in your directory')
            print('*' * 50, '\n' * 2)
            return

        self._pixels = cv2.imread(bitmap_file, 0)

        self._width, self._height = self._pixels.shape

        self._start_pos = (0, 1)
        self._end_pos = (self._width - 1, self._height - 2)
        
        self._border_size = 50

        self._scale_w = (self._screen_w - self._border_size) / self._width
        self._scale_h = (self._screen_h - self._border_size) / self._height
        self._offset_x = self._border_size // 2
        self._offset_y = self._border_size // 2

        self._colors = [ [COLOR_BLACK for _ in range(self._height)] for _ in range(self._width)]
        # Set colors
        for row in range(self._height):
            for col in range(self._width):
                if self._pixels[row, col] == 255:
                    self._colors[row][col] = COLOR_WHITE

        self._draw()


    def move(self, row, col, color):
        """ Change a color of a square """
        state = self._state(row, col)
        if state != OPEN:
            print(f'ERROR: You are trying to move on a spot that is a wall or already visited: {row}, {col}, color = {self._colors[row][col]}')
            return

        self._colors[row][col] = color
        pos_x, pos_y = self._calc_screen_pos(row, col)
        self._screen.block(pos_x, pos_y, self._scale_w, self._scale_h, color=color)
        self._screen.update()
        if self._delay:
            time.sleep(0.00000001)

    def restore(self, row, col):
        """ Change the color to show that this square was visited """
        self._colors[row][col] = COLOR_VISITED
        pos_x, pos_y = self._calc_screen_pos(row, col)
        self._screen.block(pos_x, pos_y, self._scale_w, self._scale_h, color=COLOR_VISITED)
        self._screen.update()


    def can_move_here(self, row, col):
        """ Is the square free to move to """
        return self._state(row, col) == OPEN


    def get_possible_moves(self, row, col):
        """ Given a square location, returns possible moves """
        if not self._pos_ok(row, col):
            return []

        possible = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        random.shuffle(possible)

        moves = []
        for x, y in possible:
            if self._state(x, y) == OPEN:
                moves.append((x, y))

        return moves


    def get_start_pos(self):
        """ Return the starting position of the maze """
        return self._start_pos


    def at_end(self, row, col):
        """ Did we reach the end of the maze """
        return self._end_pos == (row, col)


    # *************************************************************************
    # Local methods for this class - don't call directly

    def _draw(self):
        # Assume that the background on the screen is black
        for row in range(self._height):
            for col in range(self._width):
                if self._state(row, col) == OPEN:
                    pos_x, pos_y = self._calc_screen_pos(row, col)
                    self._screen.block(pos_x, pos_y, self._scale_w, self._scale_h, color=COLOR_WHITE)
                else:
                    pos_x, pos_y = self._calc_screen_pos(row, col)
                    self._screen.block(pos_x, pos_y, self._scale_w, self._scale_h, color=COLOR_BLACK)
        self._screen.update()

    def _state(self, x, y):
        if x < 0 or y < 0 or x >= self._height or y >= self._width:
            return WALL
        if self._colors[x][y] == COLOR_WHITE:
            return OPEN
        else:
            return WALL

    def _calc_screen_pos(self, x, y):
        pos_x = (self._scale_w * x) + self._offset_x
        pos_y = (self._scale_h * y) + self._offset_y
        return (pos_x, pos_y)

    def _pos_ok(self, x, y):
        if x < 0 or y < 0 or x >= self._height or y >= self._width:
            return False
        return True

