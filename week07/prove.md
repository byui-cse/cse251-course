![](../site/banner.png)

# 07 Prove: Processing Task Files

## Overview

Your assignment will process a directory full of task files.  Each file will contain details on the task to be preformed.

## Assignment

1. The assignment files is [found here](assignment/assignment.py) and the [create_tasks.py file](assignment/create_tasks.py).  You also need to download the file [words.txt](assignment/words.txt)
1. Follow the instructions found in the `assignment.py`
1. When you submit your assignment code file, describe the size of each process pool for each task type and you determined the best size of that pool.
1. run the Python program **create_tasks.py** to create the task files.
1. There are 5 different tasks that need to be processed.  Each task needs to  have it's own process pool.  The number of processes in each pool is up to you.  However, your goal is to process all of the tasks as quicky as possible using these pools.  You will need to try out different pool sizes.
1. The program will load a task one at a time and add it to the pool that is used to process that task type.  You can't load all of the tasks into memory/list and then pass them to a pool.
1. You are required to use the function apply_async() for these 5 pools. You can't use map(), or any other pool function.  You must use callback functions with the apply_async() statement.
1. Each pool will collect that results of their tasks into a global list. (ie. result_primes, result_words, result_upper, result_sums, result_names)
1. the task_* functions contain general logic of what needs to happen

### create_tasks.py program

This program will create the task files that your assignment will process.  There are two features for creating the task files.  When you run to the program, you get this prompt:

```
Do you want all task files (y), or just a few for testing (n): 
```

If you select 'y' to create all of the task files (434 of them).  You are required to process of these files for your assignment.  However, while you are developing your program, you can select the 'n' option to only create 5 task files.  Each of these task files represents one of the 5 different tasks your assignment must handle.

Sample Output while using these test tasks files.

```
{'task': 'prime', 'value': 617185517107683}
{'task': 'sum', 'start': 677, 'end': 1494917}
{'task': 'word', 'word': 'vessel'}
{'task': 'upper', 'text': 'vessel'}
{'task': 'name', 'url': 'http://swapi.dev/api/people/2/'}
12:19:00| --------------------------------------------------------------------------------
12:19:00| Primes: 1
12:19:00| 617,185,517,107,683 is not prime
12:19:00|  
12:19:00| --------------------------------------------------------------------------------
12:19:00| Words: 1
12:19:00| vessel Found
12:19:00|
12:19:00| --------------------------------------------------------------------------------
12:19:00| Uppercase: 1
12:19:00| vessel ==> VESSEL
12:19:00|
12:19:00| --------------------------------------------------------------------------------
12:19:00| Sums: 1
12:19:00| sum of 677 to 1,494,917 = 1,117,387,442,160
12:19:00|
12:19:00| --------------------------------------------------------------------------------
12:19:00| Names: 1
12:19:00| http://swapi.dev/api/people/2/ has name C-3PO
12:19:00|
12:19:00| Primes: 1
12:19:00| Words: 1
12:19:00| Uppercase: 1
12:19:00| Sums: 1
12:19:00| Names: 1
12:19:00| Finished processes 5 tasks = 4.26428800
```

## Submission

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit. The Assignment will be graded in broad categories according to the following:

When you submit your assignment code file, describe the size of each process pool for each task type how to determined them the best values.


| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted or no meaningful attempt made |
| 50% | Meaningful attempt made or doesn't compile |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% - 100%| Meets requirements |
