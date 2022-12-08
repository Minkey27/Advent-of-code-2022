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
    open(os.path.join(new_day, "puzzle_input.txt"), "x")

    for x in range(1, 3):
        part = f"Part_{x}"
        open(os.path.join(new_day, f"{part}_solution.py"), "x")
        with open(os.path.join(new_day, f"{part}_solution.py"), "w") as f:
            f.write(
                f"""import os


if __name__ == "__main__":
    f = open(os.path.join("{new_day}", "{part}", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()
"""
            )
