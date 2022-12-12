import os


MAX_ROW_COLUMNS = 99


def check_up_visible(grid, x, y, height):
    vision = 0
    for to_check_x in reversed(range(x)):
        vision += 1
        if grid[to_check_x][y] >= height:
            break
    return vision


def check_down_visible(grid, x, y, height):
    vision = 0
    for to_check_x in range(x + 1, MAX_ROW_COLUMNS):
        vision += 1
        if grid[to_check_x][y] >= height:
            break
    return vision


def check_left_visible(grid, x, y, height):
    vision = 0
    for to_check_y in reversed(range(y)):
        vision += 1
        if grid[x][to_check_y] >= height:
            break
    return vision


def check_right_visible(grid, x, y, height):
    vision = 0
    for to_check_y in range(y + 1, MAX_ROW_COLUMNS):
        vision += 1
        if grid[x][to_check_y] >= height:
            break
    return vision


if __name__ == "__main__":
    f = open(os.path.join("Day 8", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    grid = []

    for row in puzzle_input:
        grid.append(list(row))

    highest_tree_score = 0
    for x in range(MAX_ROW_COLUMNS):
        if x == 0 or x == MAX_ROW_COLUMNS - 1:
            # Skip the first & last column.
            continue
        for y in range(MAX_ROW_COLUMNS):
            if y == 0 or y == MAX_ROW_COLUMNS - 1:
                # Skip the first & last row.
                continue

            item = grid[x][y]
            vision_up = check_up_visible(grid, x, y, item)
            vision_down = check_down_visible(grid, x, y, item)
            vision_left = check_left_visible(grid, x, y, item)
            vision_right = check_right_visible(grid, x, y, item)

            vision_score = vision_up * vision_down * vision_left * vision_right
            if vision_score > highest_tree_score:
                highest_tree_score = vision_score

    print(highest_tree_score)
