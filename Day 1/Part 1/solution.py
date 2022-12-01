import os


if __name__ == "__main__":
    with open(os.path.join("Day 1", "Part 1", "puzzle_input.txt"), "r") as f:
        puzzle_input = f.read().splitlines()

    elves = []
    current_elf = 0
    for item in puzzle_input:
        if item:
            current_elf += int(item)
        else:
            elves.append(current_elf)
            current_elf = 0

    print(max(elves))
