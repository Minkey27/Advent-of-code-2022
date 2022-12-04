import os


if __name__ == "__main__":
    f = open(os.path.join("Day 3", "Part 1", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()


    priority = 0
    for puzzle_item in puzzle_input:
        middle_index = int(len(puzzle_item) / 2)

        compartment_a = list(puzzle_item[middle_index:])
        compartment_b = list(puzzle_item[:middle_index])

        misplaced_item = None
        for item in compartment_a:
            if item in compartment_b:
                misplaced_item = item

        if misplaced_item.isupper():
            priority += ord(misplaced_item) - 38
        else:
            priority += ord(misplaced_item) - 96

    print(priority)