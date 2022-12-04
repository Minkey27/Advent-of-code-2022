import os


if __name__ == "__main__":
    f = open(os.path.join("Day 3", "Part 2", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    priority = 0
    for i in range(0, len(puzzle_input), 3):
        group = puzzle_input[i: i + 3]
        unique_items = set("".join(group))

        badge = None
        for item in unique_items:
            if item in group[0] and item in group[1] and item in group[2]:
                badge = item

        if badge.isupper():
            priority += ord(badge) - 38
        else:
            priority += ord(badge) - 96

    print(priority)