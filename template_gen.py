import os
import re


if __name__ == "__main__":
    # Generate directories and files.

    # Figure out next day.
    dir_names = [name for name in os.listdir(".") if os.path.isdir(name) and name.startswith("Day")]
    last_day = max([int(re.search(r"(\d+)(?!.*\d)", dir_name).group(0)) for dir_name in dir_names])
    new_day = f"Day {last_day + 1}"

    # Create files.
    os.mkdir(new_day)

    for x in range(1, 3):
        part = f"Part {x}"
        os.mkdir(os.path.join(new_day, part))
        open(os.path.join(new_day, part, "puzzle_input.txt"), "x")
        open(os.path.join(new_day, part, "solution.py"), "x")
        with open(os.path.join(new_day, part, "solution.py"), "w") as f:
            f.write(
                f"""import os


if __name__ == "__main__":
    f = open(os.path.join("{new_day}", "{part}", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()
"""
            )
