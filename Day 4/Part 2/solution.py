import os


if __name__ == "__main__":
    f = open(os.path.join("Day 4", "Part 2", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    overlap = 0
    for pairs in puzzle_input:
        a, b = pairs.split(",")

        a_start, a_end = a.split("-")
        a_sections = range(int(a_start), int(a_end) + 1)

        b_start, b_end = b.split("-")
        b_sections = range(int(b_start), int(b_end) + 1)

        if list(set(a_sections) & set(b_sections)):
            overlap += 1

    print(overlap)
