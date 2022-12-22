import os


def run(puzzle_input):
    """
    Runs the program specified in `puzzle_input` and outputs the resulting image to the console.

    Args:
    - puzzle_input: list of str, where each element represents a command in the program. Each command is of the form
        'noop' or 'addx V', where V is an integer.

    Returns:
    None. Outputs the resulting image to the console.
    """
    cycle = 0  # counter for the current cycle
    register_x = 1  # current value of the register X
    screen_line = ""  # current row of the screen being drawn
    for command in puzzle_input:
        command = command.split(" ")

        # Calculate the number of cycles the current command will take and the resulting value of register X
        pending_cycles = 0
        pending_register_x = 0
        if command[0] == "noop":
            pending_cycles += 1
        else:
            pending_cycles += 2
            pending_register_x = int(command[1])

        # For each pending cycle, add a '#' or '.' to the current screen line depending on whether the sprite is
        # visible or not at the current position
        for pending_cycle in range(pending_cycles):
            cycle += 1
            if abs((len(screen_line)) - register_x) <= 1:
                screen_line += "#"
            else:
                screen_line += "."

            # When a complete row has been drawn, output it to the console and reset the screen line
            if cycle % 40 == 0:
                print(screen_line)
                screen_line = ""

        # Update the value of register X after all pending cycles have been processed
        register_x += pending_register_x


if __name__ == "__main__":
    f = open(os.path.join("Day 10", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()
    run(puzzle_input)
