import numpy as np
from itertools import compress
import random

class Grid:
    def __init__(self, grid, start, dest) -> None:
        self.grid = grid
        self.start = start
        self.dest = dest
        self.visited = np.zeros(self.grid.shape) + 999

    def run_walks(self):
        finds_ones = np.where(self.grid == 1)
        walk_starts = list(zip(finds_ones[0], finds_ones[1]))
        current_lowest = 1000
        for s in walk_starts:
            self.visited = np.zeros(self.grid.shape) + 999
            self.start = s
            dist = self.walk()
            current_lowest =  dist if dist < current_lowest else current_lowest

        return(current_lowest)

    def pt2(self):
        finds_ones = np.where(self.grid == 1)
        walk_a = list(zip(finds_ones[0], finds_ones[1]))
        dist = [self.visited[i] for i in walk_a]
        smallest = min(dist)
        return(smallest)


    def walk(self):
        stack = []
        stack.append(self.start)
        self.visited[self.start[0], self.start[1]] = 0

        while(len(stack) > 0):
            current_loc = stack.pop(0)
            c_x = current_loc[0]
            c_y = current_loc[1]
            current_visited = self.get_current_shortest(c_x, c_y)
            neighbours = self.get_accessible_neighbours(current_loc)

            # Update curent visited is shorter, then reset
            for n in neighbours:
                n_shortest = self.get_current_shortest(n[0], n[1])
                if n_shortest == 999:
                    stack.append(n)

                if(n_shortest > current_visited + 1):
                    self.visited[n[0], n[1]] = current_visited + 1

    def pt1(self):
        return(self.visited[self.dest[0], self.dest[1]])

    def get_accessible_neighbours(self, current_loc):
        c_x = current_loc[0]
        c_y = current_loc[1]
        current_val = self.get_loc_value(c_x, c_y)

        dirs = [
                (c_x+1, c_y), # right
                (c_x-1, c_y), #left
                (c_x, c_y+1), # up
                (c_x, c_y-1) # down
            ]

        neighbours = [xy for xy in dirs if self.can_move_2(xy[0], xy[1], current_val)]
        return(neighbours)

    def get_current_shortest(self, x, y):
        return(
            self.visited[x, y]
        )

    def should_move(self, x, y):
        """Should only move there if haven't been there before"""
        try:
            return(self.visited[x,y] == -999)
        except IndexError:
            return(False)

    def can_move(self, x, y, current_val):
        """Can only move there if <= +1"""
        if(x == -1 or y == -1):
            return(False)

        try:
            can_move = self.get_loc_value(x, y) <= current_val + 1
        except IndexError:
            can_move = False

        return(can_move)

    def can_move_2(self, x, y, current_val):
        """Can only move there if <= +1"""
        if(x == -1 or y == -1):
            return(False)

        try:
            check_value = self.get_loc_value(x, y)
            can_move = check_value >= current_val - 1
        except IndexError:
            can_move = False

        return(can_move)

    def get_loc_value(self, x, y):
        constant = -1
        if(x == -1 or y == -1):
            return(constant)

        try:
            val = self.grid[x, y]
        except IndexError:
            val = constant
        return(val)





def get_remap():
    import string
    letters = list(string.ascii_lowercase)
    numbers = list(range(1,27))
    score_map = dict(zip(letters, numbers))
    score_map["S"] = 1
    score_map["E"] = 26
    return(score_map)

def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt[:-1])

def main():
    lines = split_by_newline(load_file("day12/input.txt"))
    remap = get_remap()
    data = [
        [i for i in list(line)] for line in lines
    ]
    data = np.array(data)
    start = (np.where(data == "S")[0][0], np.where(data == "S")[1][0])
    dest = (np.where(data == "E")[0][0], np.where(data == "E")[1][0])
    # Lazy
    data = [
        [remap[i] for i in list(line)] for line in lines
    ]
    data = np.array(data)

    # Part 1
    # grid = Grid(data, start, dest)
    # grid.walk()
    # moves = grid.pt1()
    # print(moves)
    # Part 2
    grid = Grid(data, dest, dest)
    grid.walk()
    moves = grid.pt2()
    return(moves)



if __name__ == "__main__":
    print(main())
