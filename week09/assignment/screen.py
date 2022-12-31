"""
Course: CSE 251
File: cse251Turtle.py
Author: Brother Comeau
Purpose: Drawing Class for CSE 251

*******************************************************************************
*                                Do Not Change                                *
*******************************************************************************

"""

import turtle
import time

import cv2
import numpy as np

class Screen:

    # Consts values
    COMMAND_MOVE = 1
    COMMAND_COLOR = 2
    COMMAND_UPDATE = 3
    COMMAND_BLOCK = 4
    COMMAND_LINE = 5

    def __init__(self, width, height):
        self.commands = []
        self.width = width
        self.height = height

        self.board = np.zeros((width, height, 3), dtype=np.uint8)

    def __del__(self):
        cv2.destroyAllWindows()

    def background(self, color):
        pt1 = (0, 0)
        pt2 = (self.width, self.height)
        cv2.rectangle(self.board, pt1, pt2, color, -1)

    def move(self, x, y):
        self.commands.append((self.COMMAND_MOVE, int(x), int(y)))

    def color(self, color):
        self.commands.append((self.COMMAND_COLOR, color))

    def clear(self):
        self.commands = []

    def print_commands(self):
        # print(self.commands)
        print(f'There are {len(self.commands)} commands created')

    def get_command_count(self):
        return len(self.commands)

    def line(self, x1, y1, x2, y2, color='black'):
        self.commands.append((self.COMMAND_LINE, int(x1), int(y1), int(x2), int(y2), color))

    def update(self):
        self.commands.append((self.COMMAND_UPDATE, ))

    def block(self, x, y, width, height, color='black'):
        self.commands.append((self.COMMAND_BLOCK, int(x), int(y), int(width), int(height), color))

    def play_commands(self, speed=0):
        pos_x = 0
        pos_y = 0
        color = (0, 0, 0)
        sleep_time = speed
        finish = False

        title = 'Maze: Press "q" to quit, "f" to finish drawing, "1" slow drawing, "2" faster drawing, "p" to play again'

        cv2.namedWindow(title)

        for action in self.commands:
            # print(action)
            code = action[0]
            if   code == self.COMMAND_MOVE:
                pos_x = action[1]
                pos_y = action[2]

            elif code == self.COMMAND_COLOR:            
                color = action[1]

            elif code == self.COMMAND_UPDATE:
                cv2.imshow(title, self.board)
                if not finish:
                    if sleep_time > 0:
                        key = cv2.waitKey(sleep_time)
                    else:
                        key = cv2.waitKey(1)

                    if key == 27 or key == ord('q') or key == ord('Q'):
                        return False

                    if key == ord('f') or key == ord('F'):
                        finish = True

            elif code == self.COMMAND_LINE:
                cv2.line(self.board, (action[1], action[2]), (action[3], action[4]), action[5], 1)

            elif code == self.COMMAND_BLOCK:
                cv2.rectangle(self.board, (action[1], action[2]), (action[1] + action[3], action[2] + action[4]), action[5], -1)

            else:
                print(f'Invalid action found: {action}')

        cv2.imshow(title, self.board)
        return True
