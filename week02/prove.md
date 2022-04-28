![](../site/banner.png)

# 02 Prove: Star Wars

## Overview

The python server in this assignment contains details of all of the Star Wars films.  You can access this information by making GET requests.  You will be retrieving the details of the 6th Star Wars film.

## Instructions

1. In your "week02/assignment" folder, download the [assignment.py](assignment/assignment.py) file from GitHub.
1. Your goal is to retrieve the information from the website as fast as you can.

**Coding Instructions**

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used in this assignment.
- Run the server.py program from a terminal/console program.  Simply type `python server.py`.  Note that you also need to download the file `data.txt` in order for the server to work. 
- The only **fixed** or hard coded URL that you can use is TOP_API_URL.  Use this URL to retrieve other URLs that you can use to retrieve information from the server.
- You need to match the output outlined in the decription of the assignment. Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for this assignment.  This object will make the API calls to the server. You can define your class within this Python file (ie., no need to have a seperate file for the class)
- Do not add any global variables except for the ones included in this program.
- The main goal of the program is to create as many threads objects (In different parts of your program) as you can, then start them all, then wait for all of them to finish.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.


## Sample Output (Log file)

The following is the **required** output of your assignment.  Notice that the names of characters, planets, etc... are **sorted**.  Don't worry about the blank lines or the extra "," you might get while printing the names. Also, the exact number of calls do not need to match 94 that is in this example (but it should be very close to it).

```text
16:57:24| Starting to retrieve data from the server
16:57:35| -----------------------------------------
16:57:35| Title   : Revenge of the Sith
16:57:35| Director: George Lucas
16:57:35| Producer: Rick McCallum
16:57:35| Released: 2005-05-19
16:57:35|
16:57:35| Characters: 34
16:57:35| Adi Gallia, Anakin Skywalker, Ayla Secura, Bail Prestor Organa, Beru Whitesun lars, C-3PO, Chewbacca, Darth Vader, Dooku, Eeth Koth, Grievous, Ki-Adi-Mundi, Kit Fisto, Leia Organa, Luke Skywalker, Luminara Unduli, Mace Windu, Nute Gunray, Obi-Wan Kenobi, Owen Lars, Padmé Amidala, Palpatine, Plo Koon, Poggle the Lesser, R2-D2, R4-P17, Raymus Antilles, Saesee Tiin, Shaak Ti, Sly Moore, Tarfful, Tion Medon, Wilhuff Tarkin, Yoda,
16:57:35|
16:57:35| Planets: 13
16:57:35| Alderaan, Cato Neimoidia, Coruscant, Dagobah, Felucia, Kashyyyk, Mustafar, Mygeeto, Naboo, Polis Massa, Saleucami, Tatooine, Utapau,
16:57:35|
16:57:35| Starships: 12
16:57:35| Banking clan frigte, Belbullab-22 starfighter, CR90 corvette, Droid control ship, Jedi Interceptor, Jedi starfighter, Naboo star skiff, Republic attack cruiser, Theta-class T-2c shuttle, Trade Federation cruiser, V-wing, arc-170,
16:57:35| 
16:57:35| Vehicles: 13
16:57:35| AT-RT, AT-TE, Clone turbo tank, Corporate Alliance tank droid, Droid gunship, Droid tri-fighter, Emergency Firespeeder, LAAT/i, Neimoidian shuttle, Oevvaor jet catamaran, Raddaugh Gnasp fluttercraft, Tsmeu-6 personal wheel bike, Vulture Droid,
16:57:35|
16:57:35| Species: 20
16:57:35| Cerean, Chagrian, Clawdite, Droid, Geonosian, Human, Iktotchi, Kaleesh, Kel Dor, Mirialan, Muun, Pau'an, Quermian, Skakoan, Tholothian, Togruta, Toong, Twi'lek, Wookie, Yoda's species,
16:57:35|
16:57:35| Total Time To complete = 10.76325120
16:57:35| There were 94 calls to the server

```

## How to use the requests package

There are a number of Python packages that can help you make URL calls.  We will be using the package `requests`.

### Install Package

This package needs to be installed.  Read the details on how to install packages in the `resources/software` section of the course.  Using pip, the command is `pip install requests`.  Using Python, it's `python -m pip install requests`.  (Mac users might need to use pip3)

### How to make an URL call to the server

```python
import requests
import json

# Const Values
TOP_API_URL = r'http://127.0.0.1:8790'

if __name__ == '__main__':

    response = requests.get(TOP_API_URL)
    
    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        data = response.json()
        print(data)

		# Example to get person 1 url
        print('\nHere is the URL for person id = 1:', f'{data["people"]}1')
    else:
        print('Error in requesting ID')
```

Output:

```
{
    'people': 'http://127.0.0.1:8790/people/', 
    'planets': 'http://127.0.0.1:8790/planets/', 
    'films': 'http://127.0.0.1:8790/films/', 
    'species': 'http://127.0.0.1:8790/species/', 
    'vehicles': 'http://127.0.0.1:8790/vehicles/', 
    'starships': 'http://127.0.0.1:8790/starships/'
}

Here is the URL for person id = 1: http://127.0.0.1:8790/people/1
```

## Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be  plagiarised will be graded according to the `ACADEMIC HONESTY` section in the syllabus. The Assignment will be graded in broad categories as outlined in the syllabus:

## Submission

When finished, upload your Python file to Canvas.
