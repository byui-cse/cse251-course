![](../site/banner.png)

# Course Functions and Objects

Run in the console.  Make sure that you use the same Python version that Visual Code is using when you are running your programs.

```
Mac:
python3 -m pip install git+https://github.com/byui-cse/cse251-course-files.git

Windows:
python -m pip install git+https://github.com/byui-cse/cse251-course-files.git
```

# Functions

`print_dict(dict, title='')`

This function is used while debugging your programs where it will print a dictionary in a readable format.


# Log Class

A class called Log has be created for the course.  It will allow you to create log files while running your programs.  Some of these log files will be required for your assignments.  It has built in timing methods to help will timing your functions and code.  

The file is called cse251.py and is imported in your programs by using the following code.  Refer to the file on [directory structure](directory_structure.md)


```python
# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)
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