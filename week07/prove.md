![](../site/banner.png)

# 07 Prove: Processing Task Files

## Overview

This program will process a directory full of task files.  Each file will contain details on the task to be preformed.

## Assignment

1. The assignment files is [found here](assignment/assignment.py) and the [create_tasks.py file](assignment/create_tasks.py).  You also need to download the file [words.txt](assignment/words.txt)
1. Follow the instructions found in the `assignment.py`
1. When you submit your assignment code file, describe the size of each process pool for each task type how to determined they the best values.

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

When you submit your assignment code file, describe the size of each process pool for each task type how to determined they the best values.


| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted |
| 50% | Some attempt made |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% - 100%| Meets requirements and/or Showed creativity and extend your assignments beyond the minimum standard that is specifically required |
