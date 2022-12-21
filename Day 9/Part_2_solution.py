import os
from collections import namedtuple


Point = namedtuple("Point", "x y")

UP = Point(1, 0)
RIGHT = Point(0, 1)
DOWN = Point(-1, 0)
LEFT = Point(0, -1)

DIRECTIONS = {"U": UP, "R": RIGHT, "D": DOWN, "L": LEFT}


def move_point(point_a, point_b):
    return Point(point_a.x + point_b.x, point_a.y + point_b.y)


def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0


if __name__ == "__main__":
    f = open(os.path.join("Day 9", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    rope = [Point(0, 0)] * 10
    visited = set(rope)
    for command in puzzle_input:
        direction, steps = command.split(" ")

        for step in range(int(steps)):
            rope[0] = move_point(rope[0], DIRECTIONS[direction])

            for i in range(1, 10):
                delta = Point(rope[i - 1].x - rope[i].x, rope[i - 1].y - rope[i].y)
                if abs(delta.x) > 1 or abs(delta.y) > 1:
                    rope[i] = Point(rope[i].x + sign(delta.x), rope[i].y + sign(delta.y))

                visited.add(rope[-1])

    print(len(visited))
