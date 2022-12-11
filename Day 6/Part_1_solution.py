import os


if __name__ == "__main__":
    f = open(os.path.join("Day 6", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()[0]

    for x in range(len(puzzle_input)):
        marker = puzzle_input[x: x + 14]
        if len(set(marker)) == 14:
            print(x + 14)
            print(marker)
            break
