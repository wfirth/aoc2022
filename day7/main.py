class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.contents = {}

    def __repr__(self) -> str:
        return(f"Directory - {self.name}")

    @property
    def path(self):
        if self.parent is None:
            return("/")

        return(
            f"{self.parent.path}/{self.name}"
        )

    @property
    def size(self):
        size = sum([c.size for c in self.contents.values()])
        return(size)

    def add_contents(self, item, item_name):
        if item_name in self.contents:
            raise Exception("Check")
        self.contents[item_name] = item

    def get_sub_directory_sizes(self):
        dic = {}

        for d in self.contents.values():
            if type(d) == Directory:
                dic[d.path] = d.size
                sub_dic = d.get_sub_directory_sizes()
                dic.update(sub_dic)

        return(dic)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


    def __repr__(self) -> str:
        return(f"File - {self.name}, {self.size}")


def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt[:-1])

def is_command(line):
    return(line[0]=="$")

def is_chdir(line):
    return(line[2:4]=="cd")

def chdir_name(line):
    return(line[5:])

def is_ls(line):
    return(line[2:4]=="ls")

def is_dir(line):
    return(line[0:3]=="dir")

def get_dir_name(line):
    return(line.split(" ")[1])

def get_file_name_size(line):
    file = line.split(" ")
    return(file[0], file[1])


def main():
    c_dir = Directory(None, None)
    lines = split_by_newline(load_file("day7/input.txt"))
    n_lines = len(lines)
    n = -1
    while n < n_lines-1:
        n += 1
        line = lines[n]
        if line == "$ cd /":
            c_dir = Directory("/", None)
            og_dic = c_dir
            continue

        if not is_command(line):
            raise Exception("Should always be a command here")

        if is_ls(line):
            while(n+1 < n_lines and not(is_command(lines[n+1]))):
                n += 1
                line = lines[n]
                if(is_dir(line)):
                    d_name = get_dir_name(line)
                    directory = Directory(d_name, c_dir)
                    c_dir.add_contents(directory, d_name)
                else:
                    file_name_ize = get_file_name_size(line)
                    file = File(file_name_ize[1], file_name_ize[0])
                    c_dir.add_contents(file, file_name_ize[1])

        elif is_chdir(line):
            chdir = chdir_name(line)
            if(chdir==".."):
                c_dir = c_dir.parent
            else:
                c_dir = c_dir.contents[chdir]

    output = og_dic.get_sub_directory_sizes()
    val = sum([size for size in output.values() if size <= 100000])
    #val = sum([size for size in output if size <= 100000])
    total_space_used = og_dic.size
    space_required = 30000000
    total_space = 70000000
    deficiency = space_required - (total_space - total_space_used)

    current_biggest = total_space
    for drive, size in output.items():
        if size > deficiency:
            if size < current_biggest:
                current_biggest = size
                output_drive = drive


    return(output_drive)


if __name__ == "__main__":
    print(main())
