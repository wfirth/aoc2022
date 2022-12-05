# Read each line
# Split into seperate rucksacks on half point
# Put each rucksack into a set to get uniqueness
# Merge and put into a set together
# Iterate over one half to see which of the items is no longer in it
# Assign a priority
# Sum

import string
LETTERS = string.ascii_lowercase + string.ascii_uppercase
NUMBERS = range(1,53)
SCORE_MAP = dict(zip(LETTERS, NUMBERS))

from typing import List

def load_file():
    pth = "day3/input.txt"
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt)

def split_half(d: list):
    """Splits a list into it's components"""
    split_point = int(len(d)/2)
    first_half = d[:split_point]
    second_half = d[split_point:]
    if(len(first_half)!= len(second_half)):
        raise Exception("Not same length")

    return([first_half, second_half])

def find_duplicate(set_1, set_2):
    """Finds duplicate balues between sets"""
    for c in set_1:
        if c in set_2:
            return(c)

def find_triplicate(set_1, set_2, set_3):
    """Finds duplicate balues between 3 sets"""
    for c in set_1:
        if c in set_2 and c in set_3:
            return(c)

def solve_1(rucksack):
    splits = split_half(rucksack)
    set_1 = set(splits[0])
    set_2 = set(splits[1])
    missing = find_duplicate(set_1, set_2)
    score = SCORE_MAP[missing]
    return(score)

def solve_2(three_rucksacks):
    if(len(three_rucksacks)<3):
        return(0)
    set_1 = set(three_rucksacks[0])
    set_2 = set(three_rucksacks[1])
    set_3 = set(three_rucksacks[2])
    triplicate = find_triplicate(set_1, set_2, set_3)
    score = SCORE_MAP[triplicate]
    return(score)


def main():
    input_data = load_file()
    split_data = split_by_newline(input_data)
    scores = [solve_1(line) for line in split_data if line != ""]
    return(sum(scores))

def main_2():
    input_data = load_file()
    split_data = split_by_newline(input_data)
    groupings = range(0,len(split_data),3)

    scores = [solve_2(split_data[grp:grp+3]) for grp in groupings]
    return(sum(scores))


if __name__ == "__main__":
    print(f"Value of misplaced items is {main_2()}")
