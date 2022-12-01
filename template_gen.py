import os
import re


if __name__ == "__main__":
    # Generate directories and files.

    # Figure out next day.
    dir_names = [name for name in os.listdir(".") if os.path.isdir(name) and name.startswith('Day')]
    last_day = max([int(re.search(r"(\d+)(?!.*\d)", dir_name).group(0)) for dir_name in dir_names])
    new_day = f"Day {last_day + 1}"

    # Create files.
    os.mkdir(new_day)
    os.mkdir(os.path.join(new_day, "Part 1"))
    open(os.path.join(new_day, "Part 1", "puzzle_input.txt"), "x")
    open(os.path.join(new_day, "Part 1", "solution.py"), "x")
    os.mkdir(os.path.join(new_day, "Part 2"))
    open(os.path.join(new_day, "Part 2", "puzzle_input.txt"), "x")
    open(os.path.join(new_day, "Part 2", "solution.py"), "x")
