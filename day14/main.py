import curses
import numpy as np
import time

mywindow = curses.initscr()

def getMarixString(m):
    dmap = {
        0:" ",
        4:".",
        9:"#"
    }
    x = ''
    for row in m:
        x += ' '.join(dmap[item] for item in row)
        x += "\n"
    return x


def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt)[:-1]


def main():
    lines = split_by_newline(load_file("day14/input.txt"))
    walls = [line.split("->") for line in lines]

    xs = []
    ys = []
    for i in range(len(walls)):
        walls[i] = [[int(section.split(",")[0]), int(section.split(",")[1])] for section in walls[i]]
        xs.extend([w[0] for w in walls[i]])
        ys.extend([w[1] for w in walls[i]])

    minX = min(xs)
    xOffset = minX
    maxX = max(xs)
    minY = min(ys)
    maxY = max(ys)

    arr = np.zeros((maxX-minX+1, maxY+1))
    # Build walls
    for wall in walls:
        for i in range(len(wall)-1):
            start = wall[i]
            end = wall[i+1]
            n_x = end[0] - start[0]
            n_y = end[1] - start[1]
            x_rng = range(n_x+1) if n_x >= 0 else [- x for x in range((n_x-1) * -1)]
            y_rng = range(n_y+1) if n_y >= 0 else [- y for y in range((n_y-1)* -1)]

            for x in x_rng:
                arr[start[0]-xOffset+x, start[1]] = 9
            for y in y_rng:
                arr[start[0]-xOffset, start[1]+y] = 9

    # Add arrays
    n_rows = np.shape(arr)[0]
    arr = np.c_[arr, np.zeros(n_rows), np.ones(n_rows) * 9]
    print()

    # Drop sand
    total_sand = 0
    in_abyss = False
    while not in_abyss:
        at_rest = False
        sand_origin = (500 - xOffset, 0)
        sand = [sand_origin[0], sand_origin[1]]
        while not at_rest:
            # If at far left and not at bottom, we should add another column
            if sand[0] == 0 and sand[1] < arr.shape[1] -1:
                xOffset -= 1
                sand[0] += 1
                addtnl_col = np.zeros(arr.shape[1])
                addtnl_col[-1] = 9
                arr = np.vstack([addtnl_col, arr])

            if sand[0] == arr.shape[0]-1 and sand[1] < arr.shape[1] -1:
                #xOffset -= 1
                #sand[0] -= 1
                addtnl_col = np.zeros(arr.shape[1])
                addtnl_col[-1] = 9
                arr = np.vstack([arr, addtnl_col])

            # Chek if in abyss
            arr[sand[0], sand[1]] = 0
            if(is_in_abyss(sand, arr)):
                in_abyss = True
                at_rest = True
                continue

            # Can move down
            if can_move_down(sand, arr):
                sand = [sand[0], sand[1]+1]
                arr[sand[0], sand[1]] = 4
            elif can_move_left(sand, arr):
                sand = [sand[0]-1, sand[1]+1]
                arr[sand[0], sand[1]] = 4
            elif can_move_right(sand, arr):
                sand = [sand[0]+1, sand[1]+1]
                arr[sand[0], sand[1]] = 4
            else:
                arr[sand[0], sand[1]] = 4
                at_rest = True
                total_sand += 1
                if sand[0] == sand_origin[0] and sand[1] == sand_origin[1]:
                    in_abyss = True
                continue

            # mywindow.addstr(0,0, getMarixString(arr.transpose()))
            # mywindow.refresh()
            # time.sleep(0.01)

            # if arr[sand[0], sand[1]+1] == 9:
            #     arr[sand[0], sand[1]] = 4
            #     at_rest = True
            #     total_sand += 1

    curses.endwin()

    txt = getMarixString(arr.transpose())
    textfile = open("example.txt", "w")
    a = textfile.write(txt)
    textfile.close()
    print(getMarixString(arr.transpose()))

    return(total_sand)

def xsand(sand):
    return(sand[0])

def ysand(sand):
    return(sand[1])

def is_in_abyss(sand, arr):
    if(ysand(sand) + 1 >= arr.shape[1]):
        return(True)
    return(False)

def can_move_down(sand, arr):
    return(
        arr[xsand(sand), ysand(sand)+1] not in [4, 9]
    )

def can_move_right(sand, arr):
    # if(xsand(sand)+1 >= arr.shape[0]):
    #     return(False)

    return(
        arr[xsand(sand)+1, ysand(sand)+1] not in [4, 9]
    )

def can_move_left(sand, arr):
    return(
        arr[xsand(sand) - 1, ysand(sand)+1] not in [4, 9] #and xsand(sand)-1 >= 0
    )

if __name__ == "__main__":
    print(main())
