from typing import List
from copy import deepcopy

def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n\n")
    return(splt)


def main_pt1():
    file = load_file("day13/input.txt")
    packet_pairs = split_by_newline(file)

    count = 0
    totalling_sum = 0
    for pair in packet_pairs:
        count += 1
        a, b = split_packet(pair)
        response = compare_packets(a, b)
        if response is None:
            raise Exception("Should not happen")

        if(response):
            totalling_sum += count

    return(totalling_sum)

def main_pt2():
    file = load_file("day13/input.txt")
    packet_pairs = split_by_newline(file)
    sort_lst = []
    for line in packet_pairs:
        sort_lst.extend(split_packet(line))
    sort_lst.append([[2]])
    sort_lst.append([[6]])

    all_fine = False
    while not all_fine:
        all_fine = True

        for i in range(len(sort_lst)-1):
            a = sort_lst[i]
            b = sort_lst[i+1]

            response = compare_packets(deepcopy(a), deepcopy(b))

            if response is None:
                raise Exception("Should not happen")

            if not response:
                # Swap
                all_fine = False
                sort_lst[i] = b
                sort_lst[i+1] = a

    start_idx = sort_lst.index([[2]]) + 1
    end_idx = sort_lst.index([[6]]) + 1

    return(start_idx * end_idx)


def split_packet(pair):
    splt = pair.split("\n")
    a = eval(splt[0])
    b = eval(splt[1])
    return(a, b)


def compare_packets(lhs, rhs):
    len_diff = len(lhs) - len(rhs)
    if(len_diff < 0):
        lhs.extend([None] * - len_diff)
    if(len_diff > 0):
        rhs.extend([None] * len_diff)

    for l, r in zip(lhs, rhs):
        if l is None:
            return(True)
        if r is None:
            return(False)

        if type(l)==int and type(r) == int:
            if l < r:
                return(True)
            elif l > r:
                return(False)

        if type(l) == list or type(r) == list:
            if type(l) != list:
                l = [l]
            if type(r) != list:
                r = [r]

            subcheck =compare_packets(l, r)
            if subcheck is not None:
                return(subcheck)



if __name__ == "__main__":
    print(main_pt2())
