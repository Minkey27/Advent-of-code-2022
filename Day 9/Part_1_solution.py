import os
import re


def print_playing_field(playing_field):
    """
    Util function to prettily print the playing field for ease of debugging.
    """
    for x in playing_field:
        print(x)


def calculate_and_move_head_position(playing_field, direction, steps, current_head_x, current_head_y):
    end_x = current_head_x
    end_y = current_head_y

    for step in range(steps):
        if direction == "U":
            end_x -= 1
        elif direction == "R":
            end_y += 1
        elif direction == "D":
            end_x += 1
        elif direction == "L":
            end_y -= 1

        playing_field[end_x][end_y] = "H"

    print_playing_field(playing_field)
    return end_x, end_y


if __name__ == "__main__":
    f = open(os.path.join("Day 9", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    # Generate playing field to visualize steps and ease of debugging.
    playing_field = []
    for x in range(0, 25):
        playing_field.append(["." for x in range(0, 25)])

    # Set starting point.
    current_head_x = 20
    current_head_y = 15
    playing_field[current_head_x][current_head_y] = "H"

    print_playing_field(playing_field)

    for move_command in puzzle_input[:50]:
        move_command = re.search(r"(.) (\d*)", move_command)

        direction = move_command[1]
        steps = int(move_command[2])

        import pdb; pdb.set_trace()
        print(direction, steps)
        print(current_head_x, current_head_y)
        current_head_x, current_head_y = calculate_and_move_head_position(
            playing_field,
            direction,
            steps,
            current_head_x,
            current_head_y,
        )
