# Implement a stack structure to pull off and put onto another

def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt[:-1])

class Stack:
    def __init__(self, contents = []) -> None:
        self.contents = contents

    def add(self, item):
        self.contents.extend(item)

    def remove_top_n(self, n):
        """Removes and returns top n items in order"""
        top_n = self.contents[-n:]
        self.contents = self.contents[:-n]
        return(top_n)

    def pop(self):
        if(len(self.contents)==0):
            raise Exception("Stack is empty")
        return(self.contents.pop())

    def peek(self):
        return(self.contents[-1])

class StackContainer:
    def __init__(self):
        self.stacks = {}

    def add_stack(self, stack, stack_name):
        s = Stack(stack)
        self.stacks[stack_name] = s

    def move_one_between_stack(self, src_stack_name, dest_stack_name):
        """Moves between two stacks a single item"""
        src_stack = self.stacks[src_stack_name]
        dest_stack = self.stacks[dest_stack_name]
        dest_stack.add(src_stack.pop())

    def move_multiple_between_stack(self, src_stack_name, dest_stack_name, n):
        """Moves between two stacks a number of items"""
        src_stack = self.stacks[src_stack_name]
        dest_stack = self.stacks[dest_stack_name]
        sub_stk = src_stack.remove_top_n(n)
        dest_stack.add(sub_stk)

    def move_n_between_stack(self, src_stack_name, dest_stack_name, n):
        for n in range(1, n+1):
            self.move_one_between_stack(src_stack_name, dest_stack_name)

def main():
    instruction_data = load_file("day5/instructions_input.txt")
    split_instruction_data = split_by_newline(instruction_data)
    split_by_space = [
        line.split() for line in split_instruction_data
    ]

    container = StackContainer()
    container.add_stack(["Z","P","M","H","R"],1)
    container.add_stack(["P","C","J","B"], 2)
    container.add_stack(["S","N","H","G","L","C","D"], 3)
    container.add_stack(["F","T","M","D","Q","S","R","L"], 4)
    container.add_stack(["F","S","P","Q","B","T","Z","M"], 5)
    container.add_stack(["T","F","S","Z","B","G"], 6)
    container.add_stack(["N","R","V"],7)
    container.add_stack(["P","G","L","T","D","V","C","M"], 8)
    container.add_stack(["W","Q","N","J","F","M","L"], 9)

    # Run
    for line in split_by_space:
        n = int(line[1])
        src = int(line[3])
        dst = int(line[5])

        container.move_multiple_between_stack(src, dst, n)

    for stack in container.stacks.values():
        print(stack.peek())


if __name__ == "__main__":
    main()
