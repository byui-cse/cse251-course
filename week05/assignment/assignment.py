"""
Course: CSE 251
Lesson Week: 04
File: assignment.py
Author: Brother Comeau

Purpose: Assignment 05 - Factories and Stores

Instructions:

- Read the comments in the following code.  
- Implement your code where the TODO comments are found.
- No global variables, all data must be passed to the objects.
- Only the included/imported packages are allowed.  
- Thread/process pools are not allowed
- the shared queue between the threads that are used to hold the Car objects
  can not be greater than MAX_QUEUE_SIZE
- 

"""

from datetime import datetime, timedelta
import time
import queue
import threading
import random

# Include cse 251 common Python files
import os, sys
sys.path.append('../../code')
from cse251 import *

# Global Consts
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50
CARS_TO_CREATE_PER_FACTORY = 200

# NO GLOBAL VARIABLES!

class Car():
    """ This is the Car class that will be created by the factories """

    # Class Variables
    car_makes = ('Ford', 'Chevrolet', 'Dodge', 'Fiat', 'Volvo', 'Infiniti', 'Jeep', 'Subaru', 
                'Buick', 'Volkswagen', 'Chrysler', 'Smart', 'Nissan', 'Toyota', 'Lexus', 
                'Mitsubishi', 'Mazda', 'Hyundai', 'Kia', 'Acura', 'Honda')

    car_models = ('A1', 'M1', 'XOX', 'XL', 'XLS', 'XLE' ,'Super' ,'Tall' ,'Flat', 'Middle', 'Round',
                'A2', 'M1X', 'SE', 'SXE', 'MM', 'Charger', 'Grand', 'Viper', 'F150', 'Town', 'Ranger',
                'G35', 'Titan', 'M5', 'GX', 'Sport', 'RX')

    car_years = [i for i in range(1990, datetime.now().year)]

    def __init__(self):
        # Make a random car
        self.model = random.choice(Car.car_models)
        self.make = random.choice(Car.car_makes)
        self.year = random.choice(Car.car_years)
           
    def display(self):
        print(f'{self.make} {self.model}, {self.year}')



class Factory(threading.Thread):
    """ This is a factory.  It will create cars and place them on the car queue """

    def __init__(self):
        pass

    def run(self):
        # TODO produce the cars

        # TODO wait until all of the factories are finished producing cars

        # TODO "Wake up/signal" the dealerships one more time.  Select one factory to do this
        pass



class Dealer(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self):
        pass

    def run(self):
        while True:
            # TODO handle a car

            # Sleep a little - don't change
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR + 0))



def run_production(factory_count, dealer_count):
    """ This function will do a production run with the number of
        factories and dealerships passed in as arguments.
    """

    # TODO Create semaphore(s)
    # TODO Create queue(s)
    # TODO Create lock(s)
    # TODO Create barrier(s)

    # This is used to track the number of cars receives by each dealer
    dealer_stats = list([0] * dealer_count)

    # This tracks the length of the car queue during receiving cars by the dealerships
    # It is passed to each dealership to fill out
    queue_stats = list([0] * MAX_QUEUE_SIZE)

    # TODO create your factories, each factory will create CARS_TO_CREATE_PER_FACTORY

    # TODO create your dealerships

    log.start_timer()

    # TODO Start factories and dealerships

    # TODO Wait for factories and dealerships to complete

    run_time = log.stop_timer(f'{sum(queue_stats)} cars have been created')

    # This function must return the following - Don't change!
    return (run_time, sum(queue_stats))


def main(log):
    """ Main function - DO NOT CHANGE! """

    xaxis = []
    times = []
    for i in [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]:
        run_time, cars_produced = run_production(i, i)

        assert cars_produced == (CARS_TO_CREATE_PER_FACTORY * i)
        
        xaxis.append(i)
        times.append(run_time)

    plot = Plots()
    plot.bar(xaxis, times, title=f'Production Time VS Threads', x_label='Thread Count', y_label='Time')


if __name__ == '__main__':

    log = Log(show_terminal=True)
    main(log)


