import numpy as np

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
        instructions.append(0)
        if l != "noop":
            d, n = l.split(" ")
            instructions.append(int(n))
    return(instructions)

def main():
    data = split_by_newline(load_file("day10/input.txt"))
    instructions = np.array(unpack_instructions(data))
    register = np.cumsum(instructions) + 1
    #register_positions = [20, 60, 100, 140, 180, 220]
    # total_strength = 0
    # for r in register_positions:
    #     reg_val = register[r-2]
    #     strength = reg_val * r
    #     total_strength += strength
    #register_positions = [40,80,120,160,200,240]
    line = ""
    count = 0
    register = np.insert(register, 0, 1)
    for i in register:
        sprite = [i, i+1, i+2]
        if count == 40:
            print(line)
            line = ""
            count = 0

        if count+1 in sprite:
            line += "#"
        else:
            line += " "

        count += 1



    #return(total_strength)


if __name__ == "__main__":
    print(main())
