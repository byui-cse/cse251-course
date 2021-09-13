"""
Course: CSE 251
Lesson Week: 10
File: create_data_file.py
Author: Brother Comeau

Purpose: Create the data file to be used in the team activity.
"""

import random
import string

def main():
    
    words = []
    for _ in range(1000):
        word = ''
        for _ in range(10):
            word += random.choice(string.ascii_lowercase)
        words.append(word)

    with open('letter_a.txt', 'w') as f:
        for i in range(1000000):
            if i % 25000 == 0:
                print('.', end='', flush=True)

            for _ in range(8):
                f.write(random.choice(words))

            f.write('\n')
        print()


if __name__ == '__main__':
    main()
