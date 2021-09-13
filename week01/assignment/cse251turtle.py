"""
Course: CSE 251
File: cse251Turtle.py
Author: Brother Comeau

Purpose: Turtle Class for CSE 251

************************************************************************
*                  This file can not be changed!!!!                    *
************************************************************************

"""

import turtle
import time


class CSE251Turtle:

    # Consts values
    COMMAND_UP = 1
    COMMAND_GOTO = 2
    COMMAND_DOWN = 3
    COMMAND_FORWARD = 4
    COMMAND_LEFT = 5
    COMMAND_RIGHT = 6
    COMMAND_BACKWARD = 7
    COMMAND_COLOR = 8
    COMMAND_SETHEADING = 9
    COMMAND_PENSIZE = 10

    SLEEP = 0.00001

    def __init__(self):
        self.commands = []


    def pensize(self, size):
        self.commands.append((self.COMMAND_PENSIZE, size))


    def move(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()


    def up(self):
        self.commands.append((self.COMMAND_UP, ))


    def goto(self, x, y):
        self.commands.append((self.COMMAND_GOTO, x, y))


    def down(self):
        self.commands.append((self.COMMAND_DOWN, ))


    def forward(self, amount):
        time.sleep(self.SLEEP)
        self.commands.append((self.COMMAND_FORWARD, amount))


    def backward(self, amount):
        time.sleep(self.SLEEP)
        self.commands.append((self.COMMAND_BACKWARD, amount))


    def left(self, amount):
        self.commands.append((self.COMMAND_LEFT, amount))


    def right(self, amount):
        self.commands.append((self.COMMAND_RIGHT, amount))


    def color(self, color):
        self.commands.append((self.COMMAND_COLOR, color))


    def setheading(self, amount):
        self.commands.append((self.COMMAND_SETHEADING, amount))


    def clear(self):
        self.commands = []


    def print_commands(self):
        # print(self.commands)
        print(f'There are {len(self.commands)} commands created')


    def get_command_count(self):
        return len(self.commands)


    def play_commands(self, tur):
        for action in self.commands:
            code = action[0]
            if code == self.COMMAND_UP:
                tur.up()
            elif code == self.COMMAND_GOTO:
                tur.goto(action[1], action[2])
            elif code == self.COMMAND_DOWN:
                tur.down()
            elif code == self.COMMAND_FORWARD:
                tur.forward(action[1])
            elif code == self.COMMAND_LEFT:
                tur.left(action[1])
            elif code == self.COMMAND_RIGHT:
                tur.right(action[1])
            elif code == self.COMMAND_BACKWARD:
                tur.backward(action[1])
            elif code == self.COMMAND_COLOR:
                tur.color(action[1])
            elif code == self.COMMAND_SETHEADING:
                tur.setheading(action[1])
            elif code == self.COMMAND_PENSIZE:
                tur.pensize(action[1])
            else:
                print(f'Invalid action found: {action}')

