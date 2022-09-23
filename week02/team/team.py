"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team.py
Author: Brother Comeau

Purpose: Playing Card API calls

Instructions:

- Review instructions in I-Learn.

"""

from datetime import datetime, timedelta
import threading
import requests
import json

# Include cse 251 common Python files
from cse251 import *

# TODO Create a class based on (threading.Thread) that will
# make the API call to request data from the website

class Request_thread(threading.Thread):
    # TODO - Add code to make an API call and return the results
    # https://realpython.com/python-requests/
    # constructor
    def __init__(self, url):
        # calling parent class constructor
        super().__init__()
        self.url = url
        self.response = {}

    # This is the method that is run when start() is called
    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
        else:
            print(f"Error code: {response.status_code}", flush=True)



class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.BASE_URL = f'https://deckofcardsapi.com/api/deck/{self.id}/'
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        # TODO - add call to reshuffle
        reshuffle_url = f'{self.BASE_URL}shuffle'
        req_thread = Request_thread(reshuffle_url)
        req_thread.start()
        req_thread.join()

    def draw_card(self):
        # TODO add call to get a card
        draw_url = f'{self.BASE_URL}draw/?count=1'
        req_thread = Request_thread(draw_url)
        req_thread.start()
        req_thread.join()

        if req_thread.response:
            self.remaining -= 1
            return req_thread.response["cards"][0]["code"]

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = 'yge0v95mfkoo'

    # Testing Code >>>>>
    deck = Deck(deck_id)
    for i in range(52):
        card = deck.draw_endless()
        print(f'{i + 1}. {card}', flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

