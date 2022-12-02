from enum import Enum

class RPS(Enum):
    R="R"
    P="P"
    S="S"

class Result(Enum):
    Win = "Z"
    Draw = "Y"
    Lose = "X"

map_theirs = {
    "A": RPS.R,
    "B": RPS.P,
    "C": RPS.S
}

map_yours = {
    "X": RPS.R,
    "Y": RPS.P,
    "Z": RPS.S
}

usage_score = {
    RPS.R: 1,
    RPS.P: 2,
    RPS.S: 3
}

beats = {
    RPS.R: RPS.S,
    RPS.S: RPS.P,
    RPS.P: RPS.R
}

loses = {
    RPS.R: RPS.P,
    RPS.S: RPS.R,
    RPS.P: RPS.S
}

def rps_result(yours:RPS, theirs:RPS):
    win = 6
    draw = 3
    loss = 0

    if yours == theirs:
        return(draw)

    if yours == RPS.R:
        if theirs == RPS.S:
            return(win)
        return(loss)

    if yours == RPS.P:
        if theirs == RPS.R:
            return(win)
        return(loss)

    if yours == RPS.S:
        if theirs == RPS.P:
            return(win)
        return(loss)

def get_required_shape(theirs, result):
    if result == Result.Draw:
        return(theirs)

    if result == Result.Win:
        return(loses[theirs])

    return(beats[theirs])

def load_file():
    pth = "day2/input.txt"
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by double newline"""
    splt = d.split("\n")
    return(splt)


def score(yours, theirs):
    u_score = usage_score[yours]
    w_score = rps_result(yours, theirs)
    return(u_score + w_score)

def wrap_score_1(line):
    split = line.split(" ")
    yours = map_yours[split[1]]
    theirs = map_theirs[split[0]]
    return(score(yours, theirs))

def wrap_score_2(line):
    split = line.split(" ")
    theirs = map_theirs[split[0]]
    result = Result(split[1])
    yours = get_required_shape(theirs, result)
    return(score(yours, theirs))

def part1():
    data = load_file()
    line_split = split_by_newline(data)
    round_scores = [wrap_score_1(line) for line in line_split if line != ""]
    return sum(round_scores)

def part2():
    data = load_file()
    line_split = split_by_newline(data)
    round_scores = [wrap_score_2(line) for line in line_split if line != ""]
    return sum(round_scores)

if __name__ == "__main__":
    print(f"Total score is {part2()}")
