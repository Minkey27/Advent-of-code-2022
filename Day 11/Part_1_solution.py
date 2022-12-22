import os
from math import floor
from pprint import pprint


def run(puzzle_input):
    data = {}

    current_monkey = None
    for line in puzzle_input:
        if "Monkey" in line:
            current_monkey = line.split(" ")[1][:1]
            data[current_monkey] = {"seen_items": 0}
        elif "Starting items" in line:
            data[current_monkey]["starting_items"] = [int(x) for x in line.split(": ")[1].split(", ")]
        elif "Operation" in line:
            data[current_monkey]["operation"] = line.split(": ")[1].replace("new = ", "")
        elif "Test" in line:
            data[current_monkey]["test"] = int(line.replace("Test: divisible by ", ""))
        elif "If true" in line:
            data[current_monkey]["if_true"] = int(line.replace("If true: throw to monkey ", ""))
        elif "If false" in line:
            data[current_monkey]["if_false"] = int(line.replace("If false: throw to monkey ", ""))

    for x in range(20):
        for monkey, monkey_data in data.items():
            for starting_item in monkey_data["starting_items"]:
                monkey_data["seen_items"] += 1
                new = None
                old = starting_item  # noqa
                new = eval(monkey_data["operation"])

                # Inspected, but monkey didn't break item.
                new = floor(new / 3)

                if new % monkey_data["test"] == 0:
                    target_monkey = monkey_data["if_true"]
                else:
                    target_monkey = monkey_data["if_false"]
                data[str(target_monkey)]["starting_items"].append(new)

            data[monkey]["starting_items"] = []

    print("Results:")
    seen_items = [x["seen_items"] for i, x in data.items()]
    print(seen_items)
    highest_numbers = sorted(seen_items)[-2:]
    print(highest_numbers)
    print(highest_numbers[0] * highest_numbers[1])


if __name__ == "__main__":
    f = open(os.path.join("Day 11", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()
    run(puzzle_input)
