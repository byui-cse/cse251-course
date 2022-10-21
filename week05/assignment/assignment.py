"""
Course: CSE 251
Lesson Week: 05
File: assignment.py
Author: Gabriel Ikpaetuk

Purpose: Assignment 05 - Factories and Dealers

Instructions:

- Read the comments in the following code.
- Implement your code where the TODO comments are found.
- No global variables, all data must be passed to the objects.
- Only the included/imported packages are allowed.
- Thread/process pools are not allowed
- You are not allowed to use the normal Python Queue object.  You must use Queue251.
- the shared queue between the threads that are used to hold the Car objects
  can not be greater than MAX_QUEUE_SIZE

"""

from datetime import datetime, timedelta
import time
import threading
import random

# Include cse 251 common Python files
from cse251 import *

# Global Consts
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

        # Display the car that has was just created in the terminal
        # self.display()

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []
        self.max_size = 0

    def get_max_size(self):
        return self.max_size

    def put(self, item):
        self.items.append(item)
        if len(self.items) > self.max_size:
            self.max_size = len(self.items)

    def get(self):
        return self.items.pop(0)


class Factory(threading.Thread):
    """ This is a factory.  It will create cars and place them on the car queue """

    def __init__(self, car_queue, num_queue_empty_slots_sem,
                 num_queue_avail_cars_sem,
                 factory_stats, barrier, fact_num, isSupervisorDetails,
                 ):
        super().__init__()
        self.cars_to_produce = random.randint(200, 300)  # Don't change
        self.car_queue = car_queue
        self.num_queue_empty_slots_sem = num_queue_empty_slots_sem
        self.num_queue_avail_cars_sem = num_queue_avail_cars_sem
        self.factory_stats = factory_stats
        self.barrier = barrier
        self.fact_num = fact_num
        self.isSupervisor, self.num_dealership = isSupervisorDetails
        # self.num_dealership = num_dealership

    def run(self):
        # TODO produce the cars, the send them to the dealerships
        for i in range(self.cars_to_produce):
            self.num_queue_empty_slots_sem.acquire()
            new_car = Car()
            self.car_queue.put(new_car)
            self.factory_stats[self.fact_num] += 1
            self.num_queue_avail_cars_sem.release()

        # TODO wait until all of the factories are finished producing cars
        # print("***********")
        self.barrier.wait()

        # TODO "Wake up/signal" the dealerships one more time.  Select one factory to do this
        if self.isSupervisor:
            for i in range(self.num_dealership):
                self.num_queue_empty_slots_sem.acquire()
                self.car_queue.put(END_OF_FACTORY_CAR_PROD_SIGNAL)
                self.num_queue_avail_cars_sem.release()


class Dealer(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self, car_queue,
                 num_queue_empty_slots_sem,
                 num_queue_avail_cars_sem, dealer_stats, deal_num):
        super().__init__()
        self.car_queue = car_queue
        self.num_queue_empty_slots_sem = num_queue_empty_slots_sem
        self.num_queue_avail_cars_sem = num_queue_avail_cars_sem
        self.dealer_stats = dealer_stats
        self.deal_num = deal_num

    def run(self):
        while True:
            # TODO handle a car
            self.num_queue_avail_cars_sem.acquire()
            supposed_car = self.car_queue.get()
            if supposed_car == END_OF_FACTORY_CAR_PROD_SIGNAL:
                break
            # self.queue_stats[self.car_queue.size()] += 1
            self.dealer_stats[self.deal_num] += 1
            # supposed_car.display()
            self.num_queue_empty_slots_sem.release()
            # Sleep a little - don't change.  This is the last line of the loop
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR + 0))


def run_production(factory_count, dealer_count):
    """ This function will do a production run with the number of
        factories and dealerships passed in as arguments.
    """

    # TODO Create semaphore(s)
    num_queue_empty_slots_sem = threading.Semaphore(MAX_QUEUE_SIZE)
    num_queue_avail_cars_sem = threading.Semaphore(0)

    # TODO Create queue
    car_queue = Queue251()
    # queue_stats = list([0] * MAX_QUEUE_SIZE)

    # TODO Create lock(s)
    lock = threading.Lock()

    # TODO Create barrier(s)
    barrier = threading.Barrier(factory_count)

    # This is used to track the number of cars receives by each dealer
    dealer_stats = list([0] * dealer_count)
    factory_stats = list([0] * factory_count)

    # TODO create your factories, each factory will create CARS_TO_CREATE_PER_FACTORY
    factories = [Factory(car_queue,
                         num_queue_empty_slots_sem,
                         num_queue_avail_cars_sem, factory_stats, barrier, fact_num, (False, dealer_count))
                 for fact_num in range(factory_count - 1)]

    factories.append(Factory(car_queue,
                             num_queue_empty_slots_sem,
                             num_queue_avail_cars_sem, factory_stats, barrier, factory_count - 1, (True, dealer_count)))

    # TODO create your dealerships
    dealerships = [Dealer(car_queue,
                          num_queue_empty_slots_sem,
                          num_queue_avail_cars_sem, dealer_stats, deal_num)
                   for deal_num in range(dealer_count)]

    log.start_timer()

    # TODO Start all dealerships
    [dealership.start() for dealership in dealerships]

    time.sleep(1)  # make sure all dealers have time to start

    # TODO Start all factories
    [factory.start() for factory in factories]

    # TODO Wait for factories and dealerships to complete
    [dealership.join() for dealership in dealerships]
    [factory.join() for factory in factories]

    run_time = log.stop_timer(f'{sum(dealer_stats)} cars have been created')

    # This function must return the following - Don't change!
    # factory_stats: is a list of the number of cars produced by each factory.
    #                collect this information after the factories are finished.
    return run_time, car_queue.get_max_size(), dealer_stats, factory_stats


def main(log):
    """ Main function - DO NOT CHANGE! """

    runs = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 5), (10, 10)]
    for factories, dealerships in runs:
        run_time, max_queue_size, dealer_stats, factory_stats = run_production(factories, dealerships)

        log.write(f'Factories      : {factories}')
        log.write(f'Dealerships    : {dealerships}')
        log.write(f'Run Time       : {run_time:.4f}')
        log.write(f'Max queue size : {max_queue_size}')
        log.write(f'Factor Stats   : {factory_stats}')
        log.write(f'Dealer Stats   : {dealer_stats}')
        log.write('')

        # The number of cars produces needs to match the cars sold
        assert sum(dealer_stats) == sum(factory_stats)


if __name__ == '__main__':
    log = Log(show_terminal=True)
    main(log)
