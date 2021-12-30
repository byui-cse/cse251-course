"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team_get_deck_id.py
Author: Brother Comeau

Purpose: Playing Card deck ID

Instructions:

- Run this once to get a ID to be used in the team.py program.

"""

import requests
import json

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

if __name__ == '__main__':

    response = requests.get(r'https://deckofcardsapi.com/api/deck/new/')

    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        data = response.json()

        # Function is from the cse251 common code 
        print_dict(data)

        if 'success' in data:
            if data['success'] == True:
                print(data['deck_id'])
            else:
                print('Error in requesting ID')
        else:
            print('Error in requesting ID')
    else:
        print('Error in requesting ID')

