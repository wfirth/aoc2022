# Load into string, split by newlines into nested, sum over, bang
from typing import List

def load_file():
    pth = "day1/1/input.txt"
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by double newline"""
    splt = d.split("\n\n")
    return(splt)

def split_into_sublists(d: List[str]):
    return(
        [dind.split("\n") for dind in d]
    )

def convert_numeric(d: List[str]):
    return(
        [int(i) for i in d if i != ""]
    )

def sum_up_elements(d: List[List]):
    return(
        [sum(convert_numeric(i)) for i in d]
    )


def main():
    d = load_file()
    splt = split_by_newline(d)
    subs = split_into_sublists(splt)
    sums = sum_up_elements(subs)
    sums.sort(reverse=True)
    return(sum(sums[:3]))
    #maxVal = max(sums)
    #return(maxVal)


if __name__ == "__main__":
    #print(f"The elf with the most calories is holding {main()} calories")
    print(f"The top 3 elves are carrying a total of {main()} calories")
