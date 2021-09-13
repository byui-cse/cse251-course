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
        self.screen = screen
        self.filename = bitmap_file
        self.screen_w = width
        self.screen_h = height
        self.delay = delay

        # numpy array
        self.pixels = cv2.imread(bitmap_file, 0)

        self.width, self.height = self.pixels.shape

        self.start_pos = (0, 1)
        self.end_pos = (self.width - 1, self.height - 2)
        
        self.border_size = 50

        self.scale_w = (self.screen_w - self.border_size) / self.width
        self.scale_h = (self.screen_h - self.border_size) / self.height
        self.offset_x = self.border_size // 2
        self.offset_y = self.border_size // 2

        self.colors = [ [COLOR_BLACK for _ in range(self.height)] for _ in range(self.width)]
        # Set colors
        for row in range(self.height):
            for col in range(self.width):
                if self.pixels[row, col] == 255:
                    self.colors[row][col] = COLOR_WHITE

        self._draw()


    def move(self, row, col, color):
        """ Change a color of a square """
        state = self._state(row, col)
        if state != OPEN:
            print(f'ERROR: You are trying to move on a spot that is a wall or already visited: {row}, {col}, color = {self.colors[row][col]}')
            return

        self.colors[row][col] = color
        pos_x, pos_y = self._calc_screen_pos(row, col)
        self.screen.block(pos_x, pos_y, self.scale_w, self.scale_h, color=color)
        self.screen.update()
        if self.delay:
            time.sleep(0.00000001)

    def restore(self, row, col):
        """ Change the color to show that this square was visited """
        self.colors[row][col] = COLOR_VISITED
        pos_x, pos_y = self._calc_screen_pos(row, col)
        self.screen.block(pos_x, pos_y, self.scale_w, self.scale_h, color=COLOR_VISITED)
        self.screen.update()


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
        return self.start_pos


    def at_end(self, row, col):
        """ Did we reach the end of the maze """
        return self.end_pos == (row, col)


    # *************************************************************************
    # Local methods for this class - don't call directly

    def _draw(self):
        # Assume that the background on the screen is black
        for row in range(self.height):
            for col in range(self.width):
                if self._state(row, col) == OPEN:
                    pos_x, pos_y = self._calc_screen_pos(row, col)
                    self.screen.block(pos_x, pos_y, self.scale_w, self.scale_h, color=COLOR_WHITE)
                else:
                    pos_x, pos_y = self._calc_screen_pos(row, col)
                    self.screen.block(pos_x, pos_y, self.scale_w, self.scale_h, color=COLOR_BLACK)
        self.screen.update()

    def _state(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return WALL
        if self.colors[x][y] == COLOR_WHITE:
            return OPEN
        else:
            return WALL

    def _calc_screen_pos(self, x, y):
        pos_x = (self.scale_w * x) + self.offset_x
        pos_y = (self.scale_h * y) + self.offset_y
        return (pos_x, pos_y)

    def _pos_ok(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return False
        return True

