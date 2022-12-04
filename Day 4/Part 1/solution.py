import os


if __name__ == "__main__":
    f = open(os.path.join("Day 4", "Part 1", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    overlap = 0
    for pairs in puzzle_input:
        a, b = pairs.split(",")

        a_start, a_end = a.split("-")
        a_sections = range(int(a_start), int(a_end) + 1)

        b_start, b_end = b.split("-")
        b_sections = range(int(b_start), int(b_end) + 1)

        if (int(a_start) in b_sections and int(a_end) in b_sections) or (
            int(b_start) in a_sections and int(b_end) in a_sections
        ):
            overlap += 1

    print(overlap)
