import os
import re


# There are 9 stacks
STACKS = 9

if __name__ == "__main__":
    f = open(os.path.join("Day 5", "Part 1", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    cargo_hold = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    # Parse cargo hold.
    cargo_puzzle_input = puzzle_input[:8]
    cargo_puzzle_input.reverse()

    for cargo_puzzle_input_layer in cargo_puzzle_input:
        for x in range(9):
            start_pos = x * 4

            item = cargo_puzzle_input_layer[start_pos: start_pos + 3]

            if not item.isspace() and item:
                cargo_hold[x].append(item)

    for command in puzzle_input[10:]:
        matches = re.findall(r"[0-9]+", command)

        move_amount = int(matches[0])
        source_stack = int(matches[1]) - 1
        destination_stack = int(matches[2]) - 1
        last_item_in_stack = len(cargo_hold[source_stack])

        crane = cargo_hold[source_stack][last_item_in_stack - move_amount:]

        # Picked up by crane.
        del cargo_hold[source_stack][last_item_in_stack - move_amount:]
        cargo_hold[destination_stack].extend(crane)

    answer = ""
    for x in cargo_hold:
        answer += x[-1][1]

    print(answer)
