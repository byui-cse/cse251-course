![](../site/banner.png)

# 14 Prove: Family Search

## Overview

You will be implementing both a [depth-first algorithm](https://www.youtube.com/watch?v=9RHO6jU--GU) (aka. DFS) and [breadth-first algorithm](https://www.youtube.com/watch?v=86g8jAQug04) (aka. BFS).  Please refer to those two video links for more information on these alogrithms.  You will be retrieving family tree information from a server.  This server can handle multiple concurrent requests.  Each request takes the server 0.25 seconds to reply.

The assignment is divided into two parts.  The first part will retrieve the family tree information using DFS.  The second part will use BFS.

There are a number of classes in `assignment.py` that you can use:

**Person**

This class will decode and hold person details sent from the server.

**Family**

This class holds the family information from the server.

**Tree**

The tree class allows you to build a family tree from the families and individuals that you retrieve from the server.

**Request_thread**

The only method of requesting information from the server.  Do not change it.

## Assignment

### FS Server

There is a server program that you will need to run in it's own terminal window on your computer.  The program is `server.py`.  

1. Open a command or terminal window on your computer.
1. Go to the directory of the assignment.
1. Type `python server.py` to start the server.

While running, the server will display requests and replies from your assignment.  It also displays the current number of active threads making requests and the maximum number of threads.

The project file is `assignment.py` in the `week14/assignment` folder in GitHub.

The file `assignment.py` contains two functions: `part1()` and `part2()`.

### Part 1

- The function `part1()` currently retrieves the pedigree information one family and person at a time.  Each call to the server takes 0.25 seconds.
- Your task is to use threads to make this function faster.  There is no limit on the number of threads you can use.
- You must build the pedigree tree starting with the starting family id.  You must write your program to handle different family information from the server (ie., number of families, number of children, etc.).
- The given code in `part1()` uses Depth First Search to retrieve information. You can change it to use threads to go up the husband's line and wife's line concurrently.
- You must retrieve all individuals in a family (ie., husband, wife and children)

**Your goal is to execute part 1 in under 10 seconds**

### Part 2

- In this part, you will be retrieving the family information using a breadth-first algorithm.  Refer to [this link](https://www.youtube.com/watch?v=86g8jAQug04) for more information.
- Use threads to speed up requesting families and individuals from the server.
- Your goal is to make this function as fast as possible by using threads.
- You must retrieve all individuals in a family (ie., husband, wife and children)
- Do not use recursion for this algorithm.

**Your goal is to execute part 2 in under 10 seconds**

### 10% Bonus

- A 10% bonus if you can limit the number of threads to 5 while retrieving the family information in part 2.  The server must not have more than 5 active threads at a time. (watch the output from the server to see number of activity threads)
- There is no time requirement for this extra feature.
- Implement the function bonus().

### Misc

- The server will create a log file called `server.log`
- You assignment program will create a log file named `assignment.log`
- Do not change these log files.

## Rubric

**Describing your code**

In the header of the file ``assignment.py` is a place where you can give meaningful descriptions of part 1 and part 2.  If this is missing or incomplete, 10 points will be taken off your grade for this assignment.

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.
The Assignment will be graded in broad categories according to the following:

| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted or no meaningful attempt made |
| 50% | Meaningful attempt made or doesn't compile |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% - 100% | Meets requirements |

## Submission

- Add comments in the Python file in the header section describing how you sped up the program.
- You must clearly show in your code that you are using DFS and BFS alogrithms.
- Upload your Python file to I-Learn.

