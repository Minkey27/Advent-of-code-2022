import os


if __name__ == "__main__":
    f = open(os.path.join("Day 2", "Part 1", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    WIN_CONDITIONS = {
        "X": "C",
        "Y": "A",
        "Z": "B",
    }

    DRAW_CONDITONS = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    REACTION_SCORES = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    total_score = 0
    for item in puzzle_input:
        opponent, reaction = item.split(" ")

        match_score = 0
        # First figure out if we win, draw or lose.
        if WIN_CONDITIONS[reaction] == opponent:
            match_score += 6
        elif DRAW_CONDITONS[reaction] == opponent:
            match_score += 3

        # Add the score of the reaction.
        match_score += REACTION_SCORES[reaction]

        total_score += match_score

    print(total_score)
