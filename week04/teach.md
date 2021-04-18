![](../site/banner.png)

# 04 Teach: Using Queues and Semaphores

## Overview

Today's team activity will be using queue(s) and thread's semaphore(s). 

## Assignment

The file `data.txt` contains a list of URLs from the website `swapi.dev`.  (For example: `https://swapi.dev/api/people/1/`).  You will be creating a thread that will read this data file line by line and placing the URLs into a queue.  The other thread(s) will take URLs from the queue and request information using that URL.  Use the `request` module for Internet requests.

## Instructions

- NO global variables!!!
- Don't use thread/process pools for this program.
- Use only the provided packages that are imported.
- Review all of the give code so you understand it before adding your code.
- I would suggest setting RETRIEVE_THREADS to 1 and get that to work. Then increase it.


## Requirements

1. Download [team.py](team/team.py) and [data.txt](team/data.txt) from Github and place them in one directory.  Make sure that you open that directory in VSCode.
2. Start with `RETRIEVE_THREADS = 1` while implementing the threads.  Implement your program in steps - building on code that works.
3. You final goal is to set `RETRIEVE_THREADS = 4` where you will create 4 `retrieve_thread()` threads.
4. Once you have the program working with multiple threads, run the program using different `RETRIEVE_THREADS` values.  Does your program complete faster with more threads?  Is there a point where adding more threads to this program doesn't improve completion time?

## Sample Solution

We will go over a solution in next class time.

## Submission

When complete, please report your progress in the associated I-Learn quiz.

