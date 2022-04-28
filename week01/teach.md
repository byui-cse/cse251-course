![](../site/banner.png)

# 01 Teach: Finding Prime Numbers

## Overview

Programs can run with and without threads.  In the team activity today, you will be taking a program that counts the number of prime numbers in a range and converting it to use threads to find these prime numbers.

## Assignment

### Core Requirements

1. Install all of the [software required](../overview/cse251_code.md) for the course.  Create the folders for the course and copy the required files from GitHub to allow you to write programs in this course.  Each team member needs to complete this step.
   - Team activity files are found at [link](team/)
2. Open the folder "week01/team" and get the program file `team.py` to run.  It will create a log file and display that it found 4,306 primes.  
   - Note that each time you run the program, a new log file will be created.  You can delete any that you don't need.
   - Keep track on how long it takes for the program to run.
3. Make a copy of the `team.py` program (ie., the name of the new file could be `team-threads.py` for example) and convert that copy to use 1 thread to find the prime numbers.  You should get the same results.
   - Keep track on how long it takes for the program to run.  How does it compare to step 2 above?


### Stretch Challenge

1. Convert your program to use 10 threads to find these prime numbers.  You should get the same results as the original program.  Your program needs to display the primes that it finds.
   - Keep track on how long it takes for the program to run.
2. Question: compare the run times of the original non-threaded program with the 10 threaded version.  Talk with your team members to explain the difference.  Also, do we need a lock to protect the global variables `prime_count` and `numbers_processed`?
3. Remove (comment out) the `print` statements that display when a prime is found.  Test the non-threaded and threaded program and compare run times. 
    - Why is the program faster when you don't print out the found primes?
    - Why is there a greater time difference when you remove print statements from the threaded program when compared to the non-threaded version. (ie., run each program with and without the print statements and review the log files).  The following is my test results.  Do you get the same results?

```
threaded - with prints
11:23:59| Total time = 39.07553100

threaded - no prints
11:25:34| Total time = 33.99205550

no threads - with prints
11:27:27| Total time = 39.44827810

no threads - no prints
11:26:31| Total time = 35.67455270
```

## Sample Solution

When your program is finished, please view the sample solution for this program to compare it to your approach.

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution [team-solution.py](team/team-solution.py)

## Submission

When complete, please report your progress in the associated I-Learn quiz.

