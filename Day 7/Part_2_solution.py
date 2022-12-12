import os
import re
from collections import OrderedDict, defaultdict


if __name__ == "__main__":
    f = open(os.path.join("Day 7", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    c_dir = []
    dir_sizes = defaultdict(lambda: 0)

    for command_or_output in puzzle_input:
        if command_or_output.startswith('$'):
            cd_command = re.findall(r"cd (.*)$", command_or_output)
            if cd_command:
                if cd_command[0] == '..':
                    c_dir.pop()
                else:
                    c_dir.append(cd_command[0])
        else:  # output
            file_size = re.findall(r"(\d+) (.*)$", command_or_output)
            temp_dir = []
            if file_size:
                for sub_dir in c_dir:
                    temp_dir.append(sub_dir)
                    dir_sizes[os.path.join(*temp_dir)] += int(file_size[0][0])

    needed = 30000000 - (70000000 - dir_sizes["/"])
    sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda kv: kv[1])

    for directory in sorted_dir_sizes:
        if directory[1] >= needed:
            print(directory[1])
            break
