class Runner:
    def __init__(self) -> None:
        self.head: Head = None
        self.tails = []
        self.tail_positions = []

    def initialize(self, start_x, start_y, n_tails):
        self.head= Head(start_x, start_y)
        p_head = self.head

        for t in range(0, n_tails):
            tail = Tail(start_x, start_y, p_head)
            self.tails.append(tail)
            p_head = tail

    def update_tail_positions(self):
        self.tail_positions.append((self.tails[-1].x, self.tails[-1].y))

    def run_instruction(self, instruction):
        self.head.move(instruction)
        for t in self.tails:
            t.move()

    def run_instructions(self, instructions):
        for instr in instructions:
            self.run_instruction(instr)
            self.update_tail_positions()

    def get_total_locations(self):
        return(
            len(set(self.tail_positions))
        )


class Head:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    @property
    def position(self):
        return(
            (self.x, self.y)
        )


    def move(self, d):
        if d == "D":
            self.y = self.y -1
        elif d == "U":
            self.y = self.y + 1
        elif d == "L":
            self.x = self.x -1
        elif d == "R":
            self.x = self.x + 1

class Tail:
    def __init__(self, x:int, y:int, head: Head) -> None:
        self.x = x
        self.y = y
        self.head = head

    @property
    def position(self):
        return(
            (self.x, self.y)
        )

    def move(self):
        """Always move towards the head"""
        # If the head and tail are adjacent at all (including on top of each other), don't move.
        diff_x = self.head.x - self.x
        diff_y = self.head.y - self.y

        diff_sq = (diff_x ** 2 + diff_y ** 2)
        # If the difference in position is less than sqrt(2) then don't move
        if diff_sq <= 2:
            return()

        x_move = self.get_move(diff_x)
        y_move = self.get_move(diff_y)

        self.x += x_move
        self.y += y_move


    @staticmethod
    def get_move(move):
        sign = 1 if(move > 0)  else -1
        abs_move = min(1, abs(move))
        final_move = sign * abs_move
        return(final_move)


def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt[:-1])

def unpack_instructions(lines):
    instructions = []
    for l in lines:
        d, n = l.split(" ")
        instructions.extend([d] * int(n))
    return(instructions)

def main():
    lines = split_by_newline(load_file("day9/input.txt"))
    instructions = unpack_instructions(lines)
    runner = Runner()
    runner.initialize(0, 0, 9)
    runner.run_instructions(instructions)
    n_hit = runner.get_total_locations()
    return(n_hit)


if __name__ == "__main__":
    print(main())
