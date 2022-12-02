import os


if __name__ == "__main__":
    f = open(os.path.join("Day 2", "Part 2", "puzzle_input.txt"), "r")
    puzzle_input = f.read().splitlines()

    OPPONENT_WIN_CONDITIONS = {
        "A": "C",  # A: Rock, C: Scissors
        "B": "A",  # B: Paper, A: Rock
        "C": "B",  # C: Sciccors, B: Paper
    }

    OPPONENT_LOSE_CONDITIONS = {
        "A": "B",  # A: Rock, B: Paper
        "B": "C",  # B: Paper, C: Sciccors
        "C": "A",  # C: Sciccors, A: Rock
    }

    REACTION_SCORES = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    total_score = 0
    for item in puzzle_input:
        opponent, outcome = item.split(" ")

        match_score = 0
        # First figure out if we should win, draw or lose.
        # X: Lose
        # Y: Draw
        # Z: Win
        match outcome:
            case "X":
                reaction = OPPONENT_WIN_CONDITIONS[opponent]
            case "Y":
                match_score += 3
                reaction = opponent
            case "Z":
                match_score += 6
                reaction = OPPONENT_LOSE_CONDITIONS[opponent]

        match_score += REACTION_SCORES[reaction]

        total_score += match_score

    print(total_score)
