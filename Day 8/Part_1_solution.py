import os


MAX_ROW_COLUMNS = 99


def check_up_visible(grid, x, y, height):
    for to_check_x in reversed(range(x)):
        if grid[to_check_x][y] >= height:
            return True


def check_down_visible(grid, x, y, height):
    for to_check_x in range(x + 1, MAX_ROW_COLUMNS):
        if grid[to_check_x][y] >= height:
            return True


def check_left_visible(grid, x, y, height):
    for to_check_y in reversed(range(y)):
        if grid[x][to_check_y] >= height:
            return True


def check_right_visible(grid, x, y, height):
    for to_check_y in range(y + 1, MAX_ROW_COLUMNS):
        if grid[x][to_check_y] >= height:
            return True


if __name__ == "__main__":
    f = open(os.path.join("Day 8", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    grid = []
    for row in puzzle_input:
        grid.append(list(row))

    invisible_trees = 0 + 392
    for x in range(MAX_ROW_COLUMNS):
        if x == 0 or x == MAX_ROW_COLUMNS - 1:
            # Skip the first & last column.
            continue
        for y in range(MAX_ROW_COLUMNS):
            if y == 0 or y == MAX_ROW_COLUMNS - 1:
                # Skip the first & last row.
                continue

            item = grid[x][y]
            if (
                not check_up_visible(grid, x, y, item)
                or not check_down_visible(grid, x, y, item)
                or not check_left_visible(grid, x, y, item)
                or not check_right_visible(grid, x, y, item)
            ):
                invisible_trees += 1

    print(invisible_trees)
