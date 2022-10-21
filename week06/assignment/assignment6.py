"""
Course: CSE 251
Lesson Week: 06
File: assignment.py
Author: <Your name here>
Purpose: Processing Plant
Instructions:
- Implement the classes to allow gifts to be created.
"""

import random
import multiprocessing as mp
import os.path
import time
import datetime

# Include cse 251 common Python files - Don't change
from multiprocessing.connection import Connection

from cse251 import *

CONTROL_FILENAME = 'settings.txt'
BOXES_FILENAME = 'boxes.txt'

# Settings consts
MARBLE_COUNT = 'marble-count'
CREATOR_DELAY = 'creator-delay'
BAG_COUNT = 'bag-count'
BAGGER_DELAY = 'bagger-delay'
ASSEMBLER_DELAY = 'assembler-delay'
WRAPPER_DELAY = 'wrapper-delay'

# Global constants
MARBLE_CREATOR_END_MESSAGE = "CREATOR: SENT ALL REQUIRED MARBLES"
BAGGER_END_MESSAGE = "BAGGER: SENT ALL REQUIRED BAGS"
ASSEMBLER_END_MESSAGE = "ASSEMBLER: SENT ALL REQUIRED GIFTS"


# No Global variables

class Bag():
    """ bag of marbles - Don't change """

    def __init__(self):
        self.items = []

    def add(self, marble):
        self.items.append(marble)

    def get_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Gift():
    """ Gift of a large marble and a bag of marbles - Don't change """

    def __init__(self, large_marble, marbles):
        self.large_marble = large_marble
        self.marbles = marbles

    def __str__(self):
        marbles = str(self.marbles)
        marbles = marbles.replace("'", "")
        return f'Large marble: {self.large_marble}, marbles: {marbles[1:-1]}'


class Marble_Creator(mp.Process):
    """ This class "creates" marbles and sends them to the bagger """

    colors = ('Gold', 'Orange Peel', 'Purple Plum', 'Blue', 'Neon Silver',
              'Tuscan Brown', 'La Salle Green', 'Spanish Orange', 'Pale Goldenrod', 'Orange Soda',
              'Maximum Purple', 'Neon Pink', 'Light Orchid', 'Russian Violet', 'Sheen Green',
              'Isabelline', 'Ruby', 'Emerald', 'Middle Red Purple', 'Royal Orange', 'Big Dip O’ruby',
              'Dark Fuchsia', 'Slate Blue', 'Neon Dark Green', 'Sage', 'Pale Taupe', 'Silver Pink',
              'Stop Red', 'Eerie Black', 'Indigo', 'Ivory', 'Granny Smith Apple',
              'Maximum Blue', 'Pale Cerulean', 'Vegas Gold', 'Mulberry', 'Mango Tango',
              'Fiery Rose', 'Mode Beige', 'Platinum', 'Lilac Luster', 'Duke Blue', 'Candy Pink',
              'Maximum Violet', 'Spanish Carmine', 'Antique Brass', 'Pale Plum', 'Dark Moss Green',
              'Mint Cream', 'Shandy', 'Cotton Candy', 'Beaver', 'Rose Quartz', 'Purple',
              'Almond', 'Zomp', 'Middle Green Yellow', 'Auburn', 'Chinese Red', 'Cobalt Blue',
              'Lumber', 'Honeydew', 'Icterine', 'Golden Yellow', 'Silver Chalice', 'Lavender Blue',
              'Outrageous Orange', 'Spanish Pink', 'Liver Chestnut', 'Mimi Pink', 'Royal Red', 'Arylide Yellow',
              'Rose Dust', 'Terra Cotta', 'Lemon Lime', 'Bistre Brown', 'Venetian Red', 'Brink Pink',
              'Russian Green', 'Blue Bell', 'Green', 'Black Coral', 'Thulian Pink',
              'Safety Yellow', 'White Smoke', 'Pastel Gray', 'Orange Soda', 'Lavender Purple',
              'Brown', 'Gold', 'Blue-Green', 'Antique Bronze', 'Mint Green', 'Royal Blue',
              'Light Orange', 'Pastel Blue', 'Middle Green')

    def __init__(self, send_marble_conn, marble_count, creator_delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.send_marble_conn = send_marble_conn
        self.marble_count = marble_count
        self.creator_delay = creator_delay


    def run(self):
        """
        for each marble:
            send the marble (one at a time) to the bagger
              - A marble is a random name from the colors list above
            sleep the required amount
        Let the bagger know there are no more marbles
        """
        for i in range(self.marble_count):
            color_index = random.randrange(0, len(self.colors))
            color = self.colors[color_index]
            self.send_marble_conn.send(color)
            # Delay after sending the marble
            time.sleep(self.creator_delay)

        self.send_marble_conn.send(MARBLE_CREATOR_END_MESSAGE)
        self.send_marble_conn.close()


class Bagger(mp.Process):
    """ Receives marbles from the marble creator, then there are enough
        marbles, the bag of marbles is sent to the assembler """

    def __init__(self, receive_marble_conn, send_bag_conn, marbles_per_bag, bagger_delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.receive_marble_conn = receive_marble_conn
        self.send_bag_conn = send_bag_conn
        self.marbles_per_bag = marbles_per_bag
        self.bagger_delay = bagger_delay

    def run(self):
        """
        while there are marbles to process
            collect enough marbles for a bag
            send the bag to the assembler
            sleep the required amount
        tell the assembler that there are no more bags
        """
        bag = Bag()

        while True:
            marble = self.receive_marble_conn.recv()
            if marble == MARBLE_CREATOR_END_MESSAGE:
                # The marbles left should not be up to marbles count per bag
                # So the break here works!
                break
            bag.add(marble)
            if bag.get_size() == self.marbles_per_bag:
                self.send_bag_conn.send(bag)
                # Delay after sending bag
                time.sleep(self.bagger_delay)
                bag = Bag()

        self.send_bag_conn.send(BAGGER_END_MESSAGE)
        self.send_bag_conn.close()



class Assembler(mp.Process):
    """ Take the set of marbles and create a gift from them.
        Sends the completed gift to the wrapper """
    marble_names = ('Lucky', 'Spinner', 'Sure Shot', 'The Boss', 'Winner', '5-Star', 'Hercules', 'Apollo', 'Zeus')

    def __init__(self, receive_bag_conn, send_gift_conn, assembler_delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.receive_bag_conn = receive_bag_conn
        self.send_gift_conn = send_gift_conn
        self.assembler_delay = assembler_delay

    def run(self):
        """
        while there are bags to process
            create a gift with a large marble (random from the name list) and the bag of marbles
            sends the gift to the wrapper
            sleep the required amount
        tell the wrapper that there are no more gifts
        """
        while True:
            bag = self.receive_bag_conn.recv()
            if bag == BAGGER_END_MESSAGE:
                break
            mable_index = random.randrange(0, len(self.marble_names))
            large_mable = self.marble_names[mable_index]
            gift = Gift(large_mable, bag.items)
            self.send_gift_conn.send(gift)
            # Delay after sending the gift
            time.sleep(self.assembler_delay)

        self.send_gift_conn.send(ASSEMBLER_END_MESSAGE)
        self.send_gift_conn.close()


class Wrapper(mp.Process):
    """ Takes created gifts and wraps them by placing them in the boxes file """

    def __init__(self, receive_gift_conn, wrapper_delay, filename):
        mp.Process.__init__(self, )
        # TODO Add any arguments and variables here
        self.receive_gift_conn = receive_gift_conn
        self.wrapper_delay = wrapper_delay
        self.filename = filename


    def run(self):
        """
        open file for writing
        while there are gifts to process
            save gift to the file with the current time
            sleep the required amount
        """

        # FIXME ---> (1st approach) This seems to be a second faster than the second approach
        # start = time.time()
        # with open(self.filename, "w") as file_to_write_to:
        #     while True:
        #         gift = self.receive_gift_conn.recv()
        #         if gift == ASSEMBLER_END_MESSAGE:
        #             break
        #         text_to_write = f"Created - {datetime.now().time()}: {str(gift)} \n"
        #         file_to_write_to.write(text_to_write)

        # FIXME ---> (2nd approach) This seems to be a second faster than the second approach
        while True:
            gift = self.receive_gift_conn.recv()
            if gift == ASSEMBLER_END_MESSAGE:
                break
            text_to_write = f"Created - {datetime.now().time()}: {str(gift)} \n"
            with open(self.filename, "a") as file_to_write_to:
                file_to_write_to.write(text_to_write)

        # print("********************")
        # end = time.time()
        # print(f"Total time to write to file: {end - start} seconds")
        # print("********************")


def display_final_boxes(filename, log):
    """ Display the final boxes file to the log file -  Don't change """
    if os.path.exists(filename):
        log.write(f'Contents of {filename}')
        with open(filename) as boxes_file:
            for line in boxes_file:
                log.write(line.strip())
    else:
        log.write_error(f'The file {filename} doesn\'t exist.  No boxes were created.')


def main():
    """ Main function """

    log = Log(show_terminal=True)

    log.start_timer()

    # Load settings file
    settings = load_json_file(CONTROL_FILENAME)
    if settings == {}:
        log.write_error(f'Problem reading in settings file: {CONTROL_FILENAME}')
        return

    log.write(f'Marble count                = {settings[MARBLE_COUNT]}')
    log.write(f'settings["creator-delay"]   = {settings[CREATOR_DELAY]}')
    log.write(f'settings["bag-count"]       = {settings[BAG_COUNT]}')
    log.write(f'settings["bagger-delay"]    = {settings[BAGGER_DELAY]}')
    log.write(f'settings["assembler-delay"] = {settings[ASSEMBLER_DELAY]}')
    log.write(f'settings["wrapper-delay"]   = {settings[WRAPPER_DELAY]}')

    # TODO: create Pipes between creator -> bagger -> assembler -> wrapper

    # creator -> bagger
    creator_send_conn, bagger_receive_conn = mp.Pipe()

    # bagger -> assembler
    bagger_send_conn, assembler_receive_conn = mp.Pipe()

    # assembler -> wrapper
    assembler_send_conn, wrapper_receiver_conn = mp.Pipe()

    # TODO create variable to be used to count the number of gifts
    number_of_gifts = mp.Manager().list([0] * 1)

    # delete final boxes file
    if os.path.exists(BOXES_FILENAME):
        os.remove(BOXES_FILENAME)

    log.write('Create the processes')

    # TODO Create the processes (ie., classes above)
    creator = Marble_Creator(creator_send_conn, settings[MARBLE_COUNT], settings[CREATOR_DELAY])
    bagger = Bagger(bagger_receive_conn, bagger_send_conn, settings[BAG_COUNT], settings[BAGGER_DELAY])
    assembler = Assembler(assembler_receive_conn, assembler_send_conn, settings[ASSEMBLER_DELAY])
    wrapper = Wrapper(wrapper_receiver_conn, settings[ASSEMBLER_DELAY], BOXES_FILENAME)

    log.write('Starting the processes')
    # TODO add code here
    creator.start()
    bagger.start()
    assembler.start()
    wrapper.start()

    log.write('Waiting for processes to finish')
    # TODO add code here
    creator.join()
    bagger.join()
    assembler.join()
    wrapper.join()

    display_final_boxes(BOXES_FILENAME, log)

    # TODO Log the number of gifts created.


if __name__ == '__main__':
    main()
