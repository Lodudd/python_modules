#!/usr/bin/env python3

import random


def main() -> None:
    origin_list = ['Alice', 'bob', 'Charlie', 'dylan',
                   'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {origin_list}")

    new_list = [element.capitalize() for element in origin_list]
    print(f"New list with all names capitalized: {new_list}")

    capital_list = [element for element in origin_list if element.istitle()]
    print(f"New list of capitalized names only: {capital_list}")

    score_dict = {element: random.randrange(1000) for element in new_list}
    print(score_dict)

    x = (sum(score_dict.values())/len(score_dict))
    print(f"Score average is {x:.1f}")

    high_scores = {value: key for value, key in score_dict.items() if key > x}
    print(f"High Scores: {high_scores}")


if __name__ == "__main__":
    main()
