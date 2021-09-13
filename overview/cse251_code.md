![](../site/banner.png)

# Course Functions and Objects

The file `cse251.py` contains common course functions and objects that will be used during the course.  The file is found in the `code` directory in GtiHub.  [Common Code File](../code/cse251.py)


# Functions

`print_dict(dict, title='')`

This function is used while debugging your programs where it will print a dictionary in a readable format.


# Log Class

A class called Log has be created for the course.  It will allow you to create log files while running your programs.  Some of these log files will be required for your assignments.  It has built in timing methods to help will timing your functions and code.  

The file is called cse251.py and is imported in your programs by using the following code.  Refer to the file on [directory structure](directory_structure.md)

```python
# Include CSE 251 common Python files
import os, sys
sys.path.append('../../code')
from cse251 import *
```

Example of creating and using the Log class.

```python
log = Log(show_terminal=True)
log.write('Hello World')
```

When a Log() object is created without a filename, the Log() object will create a file using the current date and time. For example: `1121-120631.log`.  The file format is `MMDD-HHMMSS.log`.  This log file is created in the same directory of your program.

Open the `cse251.py` file to see the classes methods.

# Plots Class

This class, `Plots`, is used to create simple Matplotlib plots.

Currently, is contains the methods `line_plot` and `bar_plot`.