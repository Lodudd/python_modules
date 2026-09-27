#!/usr/bin/env python3

import sys


def make_player_happy(scores: list[int]) -> None:

    print("Scores processed: " + str(scores))
    print("Total players: " + str(len(scores)))
    print(f"Average score: {sum((scores)) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main(args: list[str]) -> None:
    print("=== Player Score Analytics ===")
    nb_args = len(args)
    scores = []
    if nb_args == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    for i in range(1, nb_args):
        try:
            scores.append(int(args[i]))
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")

    if not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        make_player_happy(scores)


if __name__ == "__main__":
    main(sys.argv)
