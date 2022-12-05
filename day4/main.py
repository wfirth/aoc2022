def load_file():
    pth = "day4/input.txt"
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt[:-1])

def split_by_comma(d):
    splt = d.split(",")
    return(splt)

def split_by_hyphen(d):
    splt = d.split("-")
    return(splt)

def check_fully_contained(x_upper, x_lower, y_upper, y_lower):
    """Checks that y is fully contained within x"""
    return(
        between_two_points(y_upper, x_upper, x_lower) and between_two_points(y_lower, x_upper, x_lower)
        )

def check_has_overlap(x_upper, x_lower, y_upper, y_lower):
    """Checks that y is fully contained within x"""
    return(
        between_two_points(y_upper, x_upper, x_lower) or between_two_points(y_lower, x_upper, x_lower)
        )

def between_two_points(check, upper, lower):
    return(
        check <= upper and check >= lower
    )

def solve_1(line):
    x_y = split_by_comma(line)
    x = split_by_hyphen(x_y[0])
    y = split_by_hyphen(x_y[1])

    fully_contained = check_fully_contained(
        int(x[1]), int(x[0]), int(y[1]), int(y[0])
    ) or check_fully_contained(
        int(y[1]), int(y[0]), int(x[1]), int(x[0])
    )
    if(fully_contained):
        return(1)
    return(0)

def solve_2(line):
    x_y = split_by_comma(line)
    x = split_by_hyphen(x_y[0])
    y = split_by_hyphen(x_y[1])

    fully_contained = check_has_overlap(
        int(x[1]), int(x[0]), int(y[1]), int(y[0])
    ) or check_has_overlap(
        int(y[1]), int(y[0]), int(x[1]), int(x[0])
    )
    if(fully_contained):
        return(1)
    return(0)

def main():
    input_data = load_file()
    split_data = split_by_newline(input_data)
    count = [solve_2(line) for line in split_data]
    return(sum(count))


if __name__ == "__main__":
    print(f"Number of overlaps {main()}")
