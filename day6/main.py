def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)

def window_string(string: str, start: int, n: int):
    return(string[start:start+n])

def all_different(string: str):
    """Checks all values in a string are different"""
    return(len(string)==len(set(string)))

def main():
    data = load_file("day6/input.txt")
    window_size = 14
    found = False
    i = -1
    while not found:
        i += 1
        substr = window_string(data, i, window_size)
        if(all_different(substr)):
            found = True

    character_index = window_size + i
    return(character_index)


if __name__ == "__main__":
    print(main())
