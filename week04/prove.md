![](../site/banner.png)

# 04 Prove: Factory and Dealership

## Overview

You will be using queue(s) and thread semaphore(s) to synchronize two threads in the production and selling of cars.

## Project Description

This assignment will contain two threaded classes.  A `Factory` will create cars and a `Dealership` will retrieve them to be sold.  There is a limit on the number of cars that a dealership can handle at a time.  This is the `MAX_QUEUE_SIZE` variable.  Therefore, if the dealership is full of cars, the Factory must wait to produce cars until some cars are sold.

## Assignment

1. Download the [assignment.py](assignment/assignment.py) file.
2. Review the instructions found in the Python file as well as the global constants.
3. The Python file contains three classes:
   - **Car**: This is the car that the factory will create.  When a car is created, it randomly selects a make, model and year.
   - **Factor**: This threaded class creates the cars for the dealerships.  After a car is created, the factory uses a short delay between creating another one.
   - **Dealer**: This is the dealership retrieves cars created by the factory to be sold. After a car is received, the dealership uses a short delay to seel the car.  The dealership only has room for 10 cars, therefore, if the dealership is full, the factory must until a car is sold before creating another car.
4. Your goal is to create `CARS_TO_PRODUCE` many cars.

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
