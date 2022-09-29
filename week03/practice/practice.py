import os
import time
import multiprocessing as mp


def add_two_numbers(values):
    # The sleep is here to slow down the program
    time.sleep(0.5)
    number1 = values[0]
    number2 = values[1]

    print(f'PID = {os.getpid()}: {number1} + {number2} = {number1 + number2}')

if __name__ == '__main__':
    # create argument list for the pool
    numbers = [(1, 2), (11, 52), (12, 62), (13, 72), (1312, 2272), (1332, 732), (13434, -23272)]

    print(f'Numbers list: {numbers}')

    # Create a pool of 2 processes
    print(os.cpu_count())
    with mp.Pool(os.cpu_count()) as p:
        p.map(add_two_numbers, numbers)
