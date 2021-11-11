![](../site/banner.png)

# 11 Prove: Party Room

## Overview

You will be implementing a hotel room where guests can throw a party and where the cleaning staff will clean.

## Assignment

The project file is `assignment.py` in the `week11/assignment` folder in GitHub.  Refer to this file for instructions.

### Description of the problem

In a hotel, there are a number of guests and cleaning staff.  There is a conference room where guests can enter to have a party.

**Rules of using the room**

1. The guests and cleaning staff will be processes in your assignment.
1. If someone from the cleaning staff is in the room cleaning, no guest can enter the room.  Only one person from the cleaning staff can be in the room at a time.  If guests are in the room, the cleaning staff will wait until the room is empty before entering.
2. If the room is empty or other guests are in the room, guests can enter the room.  You can have multiple guests in the room at the same time.
3. The first guest to enter the empty room, will turn on the lights.
4. The last guest to leave the room, will turn of the lights.  (This is not the first guest in most cases)
5. Guests can enter and leave the room at anytime as long as the room is empty or contains other guests. It is not uncommon for guests to enter the room, leave and then enter the room again while the party is happening.
6. Assign each cleaner and guest an unique number/ID.
7. Use constants CLEANING_STAFF and HOTEL_GUESTS to know how many processes to create.
8. Remember, multiple guests must be able to be in the room at the same time.
9. Run your program for 1 minute.  While your program is running, keep track of the number of times the room of cleaned and the number of parties held.  A party starts with the lighting being turned on and ends when the lights are turned off.
10. Make sure your assignment matches the format/text of the sample output below.
11. You are not allowed to use lists or queues to control access to the room.  The solution requires 2 locks.

### Sample output of the assignment

From the sample output below.  This is only the last part of the output of the running program.  Notice that guests sometimes enter-leave and then enter-leave again during the same party.

```
                     :
                     :
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 2
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 1
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Turning on the lights for the party vvvvvvvvvvvvvv
Guest 2
Guest 3
Guest 5
Guest 1
Guest 2
Guest 4
Guest 2
Guest 5
Guest 2
Guest 5
Guest 2
Guest 4
Guest 3
Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 2
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 1
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Turning on the lights for the party vvvvvvvvvvvvvv
Guest 4
Guest 1
Guest 5
Guest 3
Guest 2
Guest 5
Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 2
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner 1
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Turning on the lights for the party vvvvvvvvvvvvvv
Guest 4
Guest 2
Guest 3
Guest 1
Guest 5
Guest 5
Guest 1
Guest 2
Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^
Room was cleaned 32 times, there were 20 parties
```

## Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.  Assignments are individual and not to be worked on with others.

The Assignment will be graded in broad categories according to the following:

| Grade | Description |
|-------|-------------|
| 0% | Nothing submitted or no meaningful attempt made |
| 50% | Meaningful attempt made or doesn't compile |
| 75% | Developing (but significantly deficient) |
| 85% | Slightly deficient |
| 93% - 100% | Meets requirements |

## Submission

When finished

- upload your Python files to Canvas.

