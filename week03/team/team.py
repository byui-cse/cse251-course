"""
Course: CSE 251
Lesson Week: 03
File: team.py
Author: Brother Comeau

Purpose: Team Activity: 

Instructions:

- Review instructions in I-Learn

"""

import random
from datetime import datetime, timedelta
import threading
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import string
import copy
import time

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

words = ['BOOKMARK', 'SURNAME', 'RETHINKING', 'HEAVY', 'IRONCLAD', 'HAPPY', 
        'JOURNAL', 'APPARATUS', 'GENERATOR', 'WEASEL', 'OLIVE', 
        'LINING', 'BAGGAGE', 'SHIRT', 'CASTLE', 'PANEL', 
        'OVERCLOCKING', 'PRODUCER', 'DIFFUSE', 'SHORE', 
        'CELL', 'INDUSTRY', 'DIRT', 
        'TEACHING', 'HIGHWAY', 'DATA', 'COMPUTER', 
        'TOOTH', 'COLLEGE', 'MAGAZINE', 'ASSUMPTION', 'COOKIE', 
        'EMPLOYEE', 'DATABASE', 'POET', 'COMPUTER', 'SAMPLE']

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Board():

    directions = (
        (1, 0),   # E
        (1, 1),   # SE
        (0, 1),   # S
        (-1, 1),  # SW
        (-1, 0),  # W
        (-1, -1), # NW
        (0, -1),   # N
        (1, -1)   # NE
    )

    def __init__(self, size):
        """ Create the instance and the board arrays """
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)] 
        self.highlighting = [[False for _ in range(size)] for _ in range(size)] 

    def _word_fits(self, word, row, col, direction):
        """ Helper function: Fit a word in the board """
        dir_x, dir_y = self.directions[direction]
        board_copy = copy.deepcopy(self.board)
        for letter in word:
            board_letter = self.get_letter(row, col)
            if board_letter == '.' or board_letter == letter:
                self.board[row][col] = letter
                row += dir_x
                col += dir_y
            else:
                self.board = copy.deepcopy(board_copy)
                return False
        return True

    def place_words(self, words):
        """ Place all of the words into the board """
        for word in words:
            print(f'Placing {word}...')
            word_fitted = False
            while not word_fitted:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                direction = random.randint(0, 7)
                word_fitted = self._word_fits(word, row, col, direction)

    def fill_in_dots(self):
        """ Replace '.' in the board to random letters """
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '.':
                    self.board[row][col] = random.choice(string.ascii_uppercase)

    def highlight(self, row, col, on=True):
        """ Turn on/off highlighting for a letter """
        self.highlighting[row][col] = on

    def get_size(self):
        """ Return the size of the board """
        return self.size

    def get_letter(self, x, y):
        """ Return the letter found at (x, y) """
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return ''
        return self.board[x][y]

    def display(self):
        """ Display the board with highlighting """
        print()
        for row in range(self.size):
            for col in range(self.size):
                if self.highlighting[row][col]:
                    print(f'{bcolors.WARNING}{bcolors.BOLD}{self.board[row][col]}{bcolors.ENDC} ', end='')
                else:
                    print(f'{self.board[row][col]} ', end='')
            print()

    def _word_at_this_location(self, row, col, direction, word):
        """ Helper function: is the word found on the board at (x, y) in a direction """
        dir_x, dir_y = self.directions[direction]
        highlight_copy = copy.deepcopy(self.highlighting)
        for letter in word:
            board_letter = self.get_letter(row, col)
            if board_letter == letter:
                self.highlight(row, col)
                row += dir_x
                col += dir_y
            else:
                self.highlighting = copy.deepcopy(highlight_copy)
                return False
        return True

    def find_word(self, word):
        """ Find a word in the board """
        print(f'Finding {word}...')
        for row in range(self.size):
            for col in range(self.size):
                for d in range(0, 8):
                    if self._word_at_this_location(row, col, d, word):
                        return True
        return False


def main():
    board = Board(25)
    board.place_words(words)
    print('Board with placed words')
    board.display()
    board.fill_in_dots()
    board.display()

    start = time.perf_counter()
    for word in words:
        if not board.find_word(word):
            print(f'Error: Could not find "{word}"')
    total_time = time.perf_counter() - start

    board.display()
    print(f'Time to find words = {total_time}')


if __name__ == '__main__':
    main()
