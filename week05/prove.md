![](../site/banner.png)

# 05 Prove: Factories and Dealerships

## Overview

You will be using queue(s) and thread semaphore(s) to synchronize many threads in the production and selling of cars.

## Project Description

This is a continuation of assignment 04.  Instead of one factory and one dealership, will have multiple of each.  The restriction of only producing `MAX_QUEUE_SIZE` is still in place for all of the dealerships.

## Assignment

1. Download the [assignment.py](assignment/assignment.py) file.
2. Review the instructions found in the Python file as well as the global constants.
3. Your goal is for each factory to produce `CARS_TO_CREATE_PER_FACTORY` many cars.
4. The function `run_production()` will be passed different number of factories and dealerships that are to be created for a production run.
5. The program will create a plot of the production time VS number of threads used.

## Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.
The Assignment will be graded in broad categories according to the following:

| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted |
| 50% | Some attempt made |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% | Meets requirements |
| 100% | Showed creativity and extend your assignments beyond the minimum standard that is specifically required |

## Submission

When finished, upload your Python file to Canvas.