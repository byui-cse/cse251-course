"""
Course: CSE 251
File: cse251.py
Author: Brother Comeau

Purpose: Common classes for the CSE 251 course
"""

import os
import time
import logging
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import json

# ===============================================================================================
def print_dict(dict, title=''):
    """ Display a dictionary in a structured format """
    if title != '':
        print(f'Dictionary: {title}')
    print(json.dumps(dict, indent=3))


# ===============================================================================================
def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename) as json_file: 
            data = json.load(json_file)
        return data
    else:
        return {}


# ===============================================================================================
class Log():
    """ Logger Class for CSE 251 """

    def __init__(self, filename_log='',
                 linefmt='',
                 show_levels=False,
                 show_terminal=False,
                 include_time=True):
        self._start_time = time.perf_counter()
        self._show_terminal = show_terminal

        if filename_log == '':
            d = datetime.now()
            localtime = d.strftime("%m%d-%H%M%S")
            filename_log = f'{localtime}.log'

        self._filename = filename_log

        if linefmt == '':
          linefmt = '%(message)s'

        if show_levels:
            linefmt = '%(levelname)s - ' + linefmt

        if include_time:
            date_format = '%H:%M:%S'
            linefmt = '%(asctime)s| ' + linefmt
        else:
            date_format = ''

        # Create and configure logger
        logging.basicConfig(filename=self._filename,
                            # format='%(asctime)s %(levelname)s %(message)s',
                            format=linefmt,
                            datefmt=date_format,
                            filemode='w')

        self.logger = logging.getLogger()

        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.INFO)

        if show_terminal:
            formatter = logging.Formatter(linefmt, datefmt=date_format)
            terminal_handler = logging.StreamHandler()
            terminal_handler.setFormatter(formatter)
            self.logger.addHandler(terminal_handler)


    def start_timer(self, message=''):
        """Start a new timer"""
        if message != '':
            self.write(message)
            
        self._start_time = time.perf_counter()

    def step_timer(self, message=''):
        """Current timer value"""
        t = time.perf_counter() - self._start_time
        if message == '':
            self.write(f'{t:0.8f}')
        else:
            self.write(f'{message} = {t:0.8f}')
        return t

    def stop_timer(self, message=''):
        """Stop the timer, and report the elapsed time"""
        t = time.perf_counter() - self._start_time
        if message == '':
            self.write(f'{t:0.8f}')
        else:
            self.write(f'{message} = {t:0.8f}')
        return t

    def get_time(self):
        return time.perf_counter()

    def write_blank_line(self):
        """Write info message to log file"""
        self.logger.info(' ')
        # if self._show_terminal:
        #   print(f'LOG: {message}')

    def write(self, message=''):
        """Write info message to log file"""
        self.logger.info(message)
        # if self._show_terminal:
        #   print(f'LOG: {message}')

    def write_warning(self, message=''):
        """Write warning message to log file"""
        self.logger.warning('WARNING: ' + message)
        # if self._show_terminal:
        #   print(f'LOG: {message}')

    def write_error(self, message=''):
        """Write error message to log file"""
        self.logger.error('ERROR: ' + message)
        # if self._show_terminal:
        #   print(f'LOG: {message}')

# ===============================================================================================
class Plots:
    """ Create plots for reports """
    def __init__(self, title=''):
        self._title = title

    def line(self, xdata, ydata,
                  desc='', title='', x_label='', y_label='', show_plot=True, filename=''):
        # fig, ax = plt.subplots()
        plt.plot(xdata, ydata)

        if title == '':
            title = self._title

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid()

        # fig.savefig("test.png")
        if filename != '':
            plt.savefig(filename)

        if show_plot:
            plt.show()

    def bar(self, xdata, ydata,
                 desc='', title='', x_label='', y_label='', show_plot=True, filename=''):

        plt.bar(xdata, ydata)

        if title == '':
            title = self._title

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid()

        # fig.savefig("test.png")
        if filename != '':
            plt.savefig(filename)

        if show_plot:
            plt.show()
