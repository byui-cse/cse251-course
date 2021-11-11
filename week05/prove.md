![](../site/banner.png)

# 05 Prove: Factories and Dealerships

## Overview

You will be using queue(s) and thread semaphore(s) to synchronize many threads in the production and selling of cars.

## Project Description

This is a continuation of assignment 04.  Instead of one factory and one dealership, will have multiple of each.  The restriction of only producing `MAX_QUEUE_SIZE` is still in place for all of the dealerships.

## Assignment

1. Download the [assignment.py](assignment/assignment.py) file.
2. Review the instructions found in the Python file as well as the global constants.
4. The function `run_production()` will be passed different number of factories and dealerships that are to be created for a production run.
1. You must not use the Python queue object for this assignment.  Use the class Queue251().

Here is a sample run of the completed assignment.  The number of cars each factory produces is random:

```
15:33:42| 296 cars have been created = 4.60179630
15:33:42| Factories      : 1     
15:33:42| Dealerships    : 1     
15:33:42| Run Time       : 4.6018
15:33:42| Max queue size : 1     
15:33:42| Factor Stats   : [296] 
15:33:42| Dealer Stats   : [296] 
15:33:42| 
15:33:46| 211 cars have been created = 3.32463510
15:33:46| Factories      : 1
15:33:46| Dealerships    : 2
15:33:46| Run Time       : 3.3246    
15:33:46| Max queue size : 2
15:33:46| Factor Stats   : [211]     
15:33:46| Dealer Stats   : [107, 104]
15:33:46| 
15:33:55| 566 cars have been created = 8.92919360
15:33:55| Factories      : 2
15:33:55| Dealerships    : 1
15:33:55| Run Time       : 8.9292    
15:33:55| Max queue size : 10        
15:33:55| Factor Stats   : [271, 295]
15:33:55| Dealer Stats   : [566]     
15:33:55| 
15:33:59| 484 cars have been created = 4.00742010
15:33:59| Factories      : 2
15:33:59| Dealerships    : 2
15:33:59| Run Time       : 4.0074    
15:33:59| Max queue size : 2
15:33:59| Factor Stats   : [230, 254]
15:33:59| Dealer Stats   : [241, 243]
15:33:59| 
15:34:03| 489 cars have been created = 4.09568640
15:34:03| Factories      : 2
15:34:03| Dealerships    : 5
15:34:03| Run Time       : 4.0957
15:34:03| Max queue size : 5
15:34:03| Factor Stats   : [229, 260]
15:34:03| Dealer Stats   : [89, 92, 108, 106, 94]
15:34:03| 
15:34:12| 1147 cars have been created = 8.97750810
15:34:12| Factories      : 5
15:34:12| Dealerships    : 2
15:34:12| Run Time       : 8.9775
15:34:12| Max queue size : 10
15:34:12| Factor Stats   : [239, 211, 204, 228, 265]
15:34:12| Dealer Stats   : [574, 573]
15:34:12| 
15:34:16| 2536 cars have been created = 4.71039130
15:34:16| Factories      : 10
15:34:16| Dealerships    : 10
15:34:16| Run Time       : 4.7104
15:34:16| Max queue size : 10
15:34:16| Factor Stats   : [269, 249, 297, 267, 228, 253, 253, 200, 299, 221]
15:34:16| Dealer Stats   : [258, 253, 257, 247, 257, 254, 255, 254, 256, 245]
```


## Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.
The Assignment will be graded in broad categories according to the following:

| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted or no meaningful attempt made |
| 50% | Meaningful attempt made or doesn't compile |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% to 100% | Meets requirements |

## Submission

When finished, upload your Python file to Canvas.