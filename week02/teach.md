![](../site/banner.png)

# 02 Teach : Playing Cards

## Overview

The website **http://deckofcardsapi.com** allows us to make Internet requests for a deck of cards.  

## Assignment

You will be using this website to implement some Python classes to retrieve playing card information.

## Instructions:

- Don't include any other packages/modules.
- Use the website http://deckofcardsapi.com to implement then methods below.  Go to this website to get documentation on the API calls allowed.

### Core Requirements

1. Install all of the files for this team activity and run `team_get_deck_id.py` to get an ID for a deck of playing cards.  You will be using this ID in your `team.py` code.  You only need to run this program once.
2. Implement the `Request_thread` class where it can be created with a URL and it will return the results. (See example in the reading requirements for this week's lesson)
3. Implement the `Deck` class methods.  Make sure that the code in `main()` can run and display card values.


### Stretch Challenge

1. Talk with your team if a `Card` class needs to be created for your game.  What are the pros and cons?
2. Question: Would the class `Deck` be faster if you retrieved all of the cards for the deck when you reshuffle instead of making an API call for draw every card?  If you have the time, implement this feature.
3. Question: Why do you think that it's important to have the `Request_thread` class?  Why not just make the API calls in `Deck` directly?

## Sample Solution

When your program is finished, please view the sample solution for this program to compare it to your approach.

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution (Core requirements): [Solution](team/team_solution.py)

## Submission

When complete, please report your progress in the associated I-Learn quiz.

