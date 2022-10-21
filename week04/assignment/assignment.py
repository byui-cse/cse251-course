"""
Course: CSE 251
Lesson Week: 04
File: assignment.py
Author: Gabriel Ikpaetuk

Purpose: Assignment 04 - Factory and Dealership

Instructions:
--- Download the assignment.py file.
--- Implement your code where the TODO comments are found.
--- No global variables, all data must be passed to the objects.
--- Only the included/imported packages are allowed.
--- Thread pools are not allowed.
    You are not allowed to use the normal Python Queue class.
    You must use Queue251. This shared queue holds the Car objects
    and can not be greater than MAX_QUEUE_SIZE while your program is running.
--- Your goal is to create CARS_TO_PRODUCE many cars. The Dealer thread must not know how many cars will be produced by the factory.
    You will need two semaphores to properly implement this assignment.
    Don't use a BoundedSemaphore. Do not use any arguments for the
    method acquire() when using semaphores. Also, when using semaphores,
    do not use the _value attribute.


- See I-Learn
I successfully implemented the core requirements for the assignment. I made use of semaphores and the provided
queue. I believe my submission Meets the requirements for the assignment.
"""

import time
import threading
import random

# Include cse 251 common Python files
from cse251 import *

# Global Consts - Do not change
CARS_TO_PRODUCE = 500
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

END_OF_FACTORY_CAR_PROD_SIGNAL = "NO MORE CARS"
# NO GLOBAL VARIABLES!

class Car():
    """ This is the Car class that will be created by the factories """

    # Class Variables
    car_makes = ('Ford', 'Chevrolet', 'Dodge', 'Fiat', 'Volvo', 'Infiniti', 'Jeep', 'Subaru',
                 'Buick', 'Volkswagen', 'Chrysler', 'Smart', 'Nissan', 'Toyota', 'Lexus',
                 'Mitsubishi', 'Mazda', 'Hyundai', 'Kia', 'Acura', 'Honda')

    car_models = ('A1', 'M1', 'XOX', 'XL', 'XLS', 'XLE', 'Super', 'Tall', 'Flat', 'Middle', 'Round',
                  'A2', 'M1X', 'SE', 'SXE', 'MM', 'Charger', 'Grand', 'Viper', 'F150', 'Town', 'Ranger',
                  'G35', 'Titan', 'M5', 'GX', 'Sport', 'RX')

    car_years = [i for i in range(1990, datetime.now().year)]

    def __init__(self):
        # Make a random car
        self.model = random.choice(Car.car_models)
        self.make = random.choice(Car.car_makes)
        self.year = random.choice(Car.car_years)

        # Sleep a little.  Last statement in this for loop - don't change
        time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))

        # Display the car that has just be created in the terminal
        self.display()

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)


class Factory(threading.Thread):
    """ This is a factory.  It will create cars and place them on the car queue """

    def __init__(self, car_queue, num_queue_empty_slots_sem, num_queue_avail_cars_sem, queue_stats):
        # TODO, you need to add arguments that will pass all of data that 1 factory needs
        # to create cars and to place them in a queue.
        super().__init__()
        self.car_queue = car_queue
        self.num_queue_empty_slots_sem = num_queue_empty_slots_sem
        self.num_queue_avail_cars_sem = num_queue_avail_cars_sem
        self.queue_stats = queue_stats

    def run(self):
        for i in range(CARS_TO_PRODUCE):
            # TODO Add you code here
            """
            create a car
            place the car on the queue
            signal the dealer that there is a car on the queue
           """
            self.num_queue_empty_slots_sem.acquire()
            new_car = Car()
            self.car_queue.put(new_car)
            self.num_queue_avail_cars_sem.release()

        # signal the dealer that there are not more cars
        self.num_queue_empty_slots_sem.acquire()
        self.car_queue.put(END_OF_FACTORY_CAR_PROD_SIGNAL)
        self.num_queue_avail_cars_sem.release()

class Dealer(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self, car_queue, num_queue_empty_slots_sem, num_queue_avail_cars_sem, queue_stats):
        # TODO, you need to add arguments that pass all of data that 1 Dealer needs
        # to sell a car
        super().__init__()
        self.car_queue = car_queue
        self.num_queue_empty_slots_sem = num_queue_empty_slots_sem
        self.num_queue_avail_cars_sem = num_queue_avail_cars_sem
        self.queue_stats = queue_stats

    def run(self):
        while True:
            # TODO Add your code here
            """
            take the car from the queue
            signal the factory that there is an empty slot in the queue
            """
            self.num_queue_avail_cars_sem.acquire()
            supposed_car = self.car_queue.get()
            if supposed_car == END_OF_FACTORY_CAR_PROD_SIGNAL:
                break
            self.queue_stats[self.car_queue.size()] += 1
            supposed_car.display()
            self.num_queue_empty_slots_sem.release()
            # Sleep a little after selling a car
            # Last statement in this for loop - don't change
            time.sleep(random.random() / SLEEP_REDUCE_FACTOR)


def main():
    log = Log(show_terminal=True)

    # TODO Create semaphore(s)
    num_queue_empty_slots_sem = threading.Semaphore(MAX_QUEUE_SIZE)
    num_queue_avail_cars_sem = threading.Semaphore(0)
    # TODO Create queue251
    car_queue = Queue251()
    # TODO Create lock(s) ?

    # This tracks the length of the car queue during receiving cars by the dealership
    # i.e., update this list each time the dealer receives a car
    queue_stats = [0] * MAX_QUEUE_SIZE

    # TODO create your one factory
    factory = Factory(car_queue, num_queue_empty_slots_sem, num_queue_avail_cars_sem, queue_stats)

    # TODO create your one dealership
    dealer = Dealer(car_queue, num_queue_empty_slots_sem, num_queue_avail_cars_sem, queue_stats)

    log.start_timer()

    # TODO Start factory and dealership
    factory.start()
    dealer.start()

    # TODO Wait for factory and dealership to complete
    factory.join()
    dealer.join()

    log.stop_timer(f'All {sum(queue_stats)} have been created')

    xaxis = [i for i in range(1, MAX_QUEUE_SIZE + 1)]
    plot = Plots()
    plot.bar(xaxis, queue_stats, title=f'{sum(queue_stats)} Produced: Count VS Queue Size', x_label='Queue Size',
             y_label='Count')


if __name__ == '__main__':
    main()
