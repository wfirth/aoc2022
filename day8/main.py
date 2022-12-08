import numpy as np

class GridPosition:
    def __init__(self, val, up, down, left, right) -> None:
        self.val = val
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.visible = False
        self.scenic_score = 0

    def is_edge(self) -> bool:
        return(
            len(self.up) == 0
            or len(self.down) == 0
            or len(self.left) == 0
            or len(self.right) == 0
        )

    def greatest(self, dir) -> bool:
        """Returns true if the greatest value in a direction"""
        return(
            all([self.val > i for i in dir])
        )

    def set_is_visible(self) -> None:
        self.visible = self.is_visible()

    def is_visible(self) -> bool:
        if self.is_edge():
            return(True)

        dirs = [self.up, self.down, self.left, self.right]
        for d in dirs:
            if self.greatest(d):
                return(True)

    def calc_scenic_score(self):
        """Get the scenic score"""
        # Need to flip the lefts and ups to be relative to position.
        right_scenicness = self.direction_scenicness(self.right)
        down_scenicness = self.direction_scenicness(self.down)
        left_scenicness = self.direction_scenicness(self.left[::-1])
        up_scenicness = self.direction_scenicness(self.up[::-1])
        score = right_scenicness * down_scenicness * left_scenicness * up_scenicness
        self.scenic_score = score

    def direction_scenicness(self, dir):
        i = 0
        for d in dir:
            i += 1
            if d >= self.val:
                return(i)
        return(i)



def load_file_to_matrix(pth):
    return(
        np.loadtxt(pth)
    )

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
    lines = split_by_newline(load_file("day8/input.txt"))
    data = [
        [int(i) for i in list(line)] for line in lines
    ]
    data = np.array(data)
    nrow, ncol = data.shape

    # sum = 0
    # for i in range(nrow):
    #     for j in range(ncol):
    #         v = data[i,j]
    #         up = data[:i,j]
    #         down = data[i+1:,j]
    #         left = data[i,:j]
    #         right = data[i,j+1:]

    #         grid = GridPosition(v, up, down, left, right)
    #         grid.set_is_visible()
    #         if grid.visible:
    #             sum += 1
    # return(sum)

    highest_score = 0
    for i in range(nrow):
        for j in range(ncol):
            v = data[i,j]
            up = data[:i,j]
            down = data[i+1:,j]
            left = data[i,:j]
            right = data[i,j+1:]

            grid = GridPosition(v, up, down, left, right)
            grid.calc_scenic_score()
            score = grid.scenic_score
            if score > highest_score:
                highest_score = score

    return(highest_score)


if __name__ == "__main__":
    print(main())
