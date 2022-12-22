import os


CHECK_CYCLES = [20, 60, 100, 140, 180, 220]


def run(puzzle_input):
    sum_registers = 0

    cycle = 0
    register_x = 1
    for command in puzzle_input:
        command = command.split(" ")

        pending_cycles = 0
        pending_register_x = 0
        if command[0] == "noop":
            pending_cycles += 1
        else:
            pending_cycles += 2
            pending_register_x += int(command[1])

        for pending_cycle in range(pending_cycles):
            cycle += 1
            if cycle in CHECK_CYCLES:
                print(cycle, register_x, cycle * register_x)
                sum_registers += cycle * register_x

        register_x += pending_register_x

    print(sum_registers)


if __name__ == "__main__":
    f = open(os.path.join("Day 10", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()
    run(puzzle_input)
