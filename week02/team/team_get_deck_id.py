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

if __name__ == '__main__':

    response = requests.get(r'https://deckofcardsapi.com/api/deck/new/')
    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        data = response.json()
        if data['success'] == True:
            print(data['deck_id'])
        else:
            print('Error in requesting ID')
    else:
        print('Error in requesting ID')

