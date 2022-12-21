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

    rope = [Point(0, 0)] * 2
    visited = set(rope)
    for command in puzzle_input:
        direction, steps = command.split(" ")

        for step in range(int(steps)):
            rope[1] = move_point(rope[1], DIRECTIONS[direction])

            delta = Point(rope[1].x - rope[0].x, rope[1].y - rope[0].y)
            if abs(delta.x) > 1 or abs(delta.y) > 1:
                rope[0] = Point(rope[0].x + sign(delta.x), rope[0].y + sign(delta.y))

            visited.add(rope[0])

    print(len(visited))
