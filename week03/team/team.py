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

    SIZE = 25

    directions = (
        (1, 0),   # E
        (1, 1),   # SE
        (0, 1),   # S
        (-1, 1),  # SW
        (-1, 0),  # W
        (-1, -1), # NW
        (0, -1),  # N
        (1, -1)   # NE
    )

    def __init__(self):
        """ Create the instance and the board arrays """
        # self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.size = self.SIZE 
        self.highlighting = [[False for _ in range(self.SIZE)] for _ in range(self.SIZE)] 

        self.board = [['L', 'S', 'O', 'D', 'A', 'E', 'O', 'M', 'A', 'A', 'I', 'I', 'A', 'S', 'S', 'A', 'M', 'G', 'R', 'C', 'O', 'D', 'A', 'I', 'R'], 
                      ['A', 'V', 'C', 'S', 'N', 'T', 'U', 'U', 'O', 'H', 'N', 'C', 'H', 'A', 'B', 'E', 'U', 'M', 'O', 'C', 'R', 'G', 'H', 'A', 'I'], 
                      ['E', 'T', 'H', 'A', 'A', 'S', 'M', 'S', 'S', 'C', 'A', 'O', 'A', 'T', 'N', 'T', 'S', 'N', 'H', 'T', 'A', 'E', 'P', 'D', 'H'], 
                      ['E', 'I', 'S', 'S', 'S', 'E', 'W', 'S', 'L', 'V', 'R', 'R', 'H', 'S', 'E', 'Q', 'S', 'B', 'S', 'M', 'E', 'R', 'V', 'K', 'A'], 
                      ['R', 'S', 'S', 'A', 'H', 'B', 'B', 'A', 'L', 'E', 'E', 'I', 'L', 'B', 'T', 'R', 'A', 'W', 'C', 'K', 'W', 'W', 'E', 'O', 'A'], 
                      ['U', 'U', 'G', 'N', 'I', 'K', 'N', 'I', 'H', 'T', 'E', 'R', 'A', 'V', 'L', 'L', 'D', 'N', 'L', 'H', 'Y', 'S', 'S', 'T', 'A'], 
                      ['M', 'O', 'C', 'D', 'M', 'B', 'N', 'D', 'U', 'Q', 'M', 'I', 'A', 'A', 'H', 'L', 'E', 'N', 'A', 'P', 'E', 'K', 'H', 'I', 'H'], 
                      ['L', 'C', 'O', 'O', 'K', 'I', 'E', 'P', 'U', 'A', 'O', 'E', 'N', 'T', 'D', 'Q', 'L', 'Q', 'C', 'N', 'T', 'J', 'I', 'D', 'A'], 
                      ['C', 'H', 'G', 'A', 'N', 'V', 'M', 'M', 'G', 'Y', 'S', 'R', 'E', 'G', 'E', 'L', 'L', 'O', 'C', 'O', 'F', 'Y', 'R', 'I', 'N'], 
                      ['A', 'E', 'A', 'G', 'T', 'O', 'J', 'A', 'O', 'U', 'U', 'W', 'A', 'D', 'E', 'O', 'V', 'P', 'O', 'A', 'O', 'N', 'T', 'U', 'A'], 
                      ['A', 'A', 'R', 'E', 'C', 'A', 'Z', 'W', 'F', 'O', 'H', 'A', 'P', 'C', 'Q', 'S', 'P', 'T', 'E', 'V', 'I', 'L', 'O', 'G', 'A'], 
                      ['B', 'V', 'J', 'E', 'M', 'I', 'D', 'F', 'J', 'T', 'I', 'E', 'P', 'A', 'C', 'S', 'H', 'Y', 'X', 'G', 'R', 'R', 'Z', 'D', 'E'], 
                      ['A', 'Y', 'T', 'L', 'N', 'A', 'I', 'D', 'K', 'G', 'G', 'E', 'A', 'M', 'N', 'I', 'R', 'O', 'N', 'C', 'L', 'A', 'D', 'D', 'A'], 
                      ['G', 'S', 'W', 'E', 'S', 'D', 'N', 'U', 'O', 'I', 'H', 'Y', 'R', 'G', 'L', 'L', 'M', 'I', 'Y', 'D', 'V', 'M', 'A', 'J', 'O'], 
                      ['G', 'A', 'E', 'A', 'A', 'Y', 'A', 'R', 'N', 'W', 'W', 'O', 'A', 'U', 'K', 'N', 'K', 'T', 'B', 'I', 'R', 'T', 'M', 'C', 'U'], 
                      ['A', 'M', 'A', 'S', 'R', 'C', 'O', 'A', 'U', 'R', 'A', 'L', 'T', 'O', 'Y', 'C', 'E', 'O', 'E', 'E', 'A', 'F', 'P', 'P', 'Y'], 
                      ['G', 'P', 'S', 'S', 'O', 'I', 'H', 'V', 'D', 'S', 'Y', 'P', 'U', 'B', 'O', 'R', 'O', 'Z', 'T', 'B', 'P', 'D', 'M', 'P', 'M'], 
                      ['E', 'L', 'E', 'U', 'T', 'J', 'F', 'I', 'E', 'D', 'S', 'M', 'S', 'L', 'O', 'K', 'T', 'U', 'A', 'R', 'D', 'O', 'P', 'K', 'H'], 
                      ['U', 'E', 'L', 'M', 'A', 'N', 'R', 'C', 'N', 'R', 'Q', 'E', 'C', 'R', 'M', 'Y', 'P', 'S', 'O', 'Z', 'C', 'A', 'O', 'S', 'D'], 
                      ['C', 'D', 'G', 'P', 'R', 'T', 'E', 'X', 'Y', 'G', 'C', 'R', 'D', 'A', 'T', 'M', 'E', 'D', 'U', 'D', 'H', 'O', 'C', 'A', 'S'], 
                      ['A', 'T', 'N', 'T', 'E', 'M', 'O', 'X', 'E', 'S', 'E', 'L', 'R', 'I', 'O', 'H', 'U', 'J', 'Q', 'D', 'B', 'D', 'I', 'F', 'F'], 
                      ['C', 'D', 'D', 'I', 'N', 'A', 'K', 'Q', 'N', 'V', 'K', 'K', 'O', 'C', 'N', 'C', 'Q', 'L', 'O', 'I', 'N', 'D', 'L', 'U', 'C'], 
                      ['A', 'I', 'S', 'O', 'E', 'G', 'P', 'G', 'O', 'M', 'Y', 'O', 'Z', 'C', 'E', 'D', 'R', 'D', 'T', 'U', 'N', 'I', 'A', 'S', 'S'], 
                      ['F', 'R', 'O', 'N', 'G', 'A', 'A', 'A', 'A', 'C', 'C', 'P', 'V', 'R', 'K', 'D', 'U', 'A', 'I', 'A', 'R', 'D', 'Z', 'E', 'D'], 
                      ['D', 'C', 'D', 'V', 'A', 'Z', 'N', 'G', 'S', 'O', 'L', 'D', 'I', 'E', 'I', 'I', 'D', 'S', 'S', 'F', 'C', 'N', 'U', 'A', 'I']]


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
    board = Board()
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
