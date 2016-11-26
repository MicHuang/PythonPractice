# -*- coding: utf-8 -*-
from random import randint
print "\nHello everyone, this is my first Python game, \
\nbelow is the Battle Field has one enemy ship hidding there. \
\nyou have 5 chances to guess where it is and destroy it. \
\nHave Fun!!"

field = []

for x in range(5):
    field.append(["O"] * 5)


def print_map(field):
    for row in range(len(field)):
        print "  ".join(field[row])


def random_row(field):
    return randint(1, len(field))


def random_col(field):
    return randint(1, len(field))


ship_row = random_row(field)
ship_col = random_col(field)


def show_ship():  # 作弊用的
    print ship_row
    print ship_col


count = 1
while count < 6:
    print "\nRound", count
    print_map(field)

    try:
        while True:
            guess_row = int(raw_input("\nGuess a row: "))
            if guess_row == 9999:  # 作弊用的
                show_ship()
                continue
            else:
                break
        guess_col = int(raw_input("Guess a col: "))
    except ValueError:
        print "Please enter a valid number!"
        continue
    if guess_row == ship_row and \
       guess_col == ship_col:
        print "\nYou Win!\n"
        break
    elif guess_row not in range(1, (len(field) + 1)) or \
         guess_col not in range(1, (len(field) + 1)):
        print "\nNot even in the sea!\n"
        count -= 1
    elif field[(guess_row) - 1][(guess_col) - 1] == "X":
        print "\nYou already guessed that place.\n"
        count -= 1
    else:
        print "\nSorry, you miss it..\n"
        field[(guess_row) - 1][(guess_col) - 1] = "X"

    count += 1
else:
    print "\nYou Lose!\n"
