#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    achivments = ['Crafting Genius', 'Strategist', 'World Savior',
                  'Speed Runner', 'Survivor',
                  'Master Explorer', 'Treasure Hunter', 'Unstoppable',
                  'First Steps',
                  'Collector Supreme', 'Untouchable',
                  'Sharp Mind', 'Boss Slayer']
    nb_achivments = random.randrange(1, 13)
    player = random.sample(achivments, nb_achivments)
    nplayer = set(player)
    return nplayer


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    player1 = gen_player_achievements()
    player2 = gen_player_achievements()
    player3 = gen_player_achievements()
    player4 = gen_player_achievements()

    print(f"Player Alice: {player1}")
    print(f"Player Bob: {player2}")
    print(f"Player Charlie: {player3}")
    print(f"Player Dylan: {player4}")

    print(f"\nAll distinct achievements: "
          f"{player1 | player2 | player3 | player4}")

    print(f"\nCommon achievements: {player1 & player2 & player3 & player4}")

    print(f"\nOnly Alice has: {player1 - player2 - player3 - player4}")
    print(f"Only Bob has: {player2 - player1 - player3 - player4}")
    print(f"Only Charlie has: {player3 - player2 - player1 - player4}")
    print(f"Only Dylan has: {player4 - player2 - player3 - player1}")

    print(f"\nAlice is missing: {(player2 | player3 | player4) - player1}")
    print(f"Bob is missing: {(player1 | player3 | player4) - player2}")
    print(f"Charlie is missing: {(player2 | player1 | player4) - player3}")
    print(f"Dylan is missing: {(player2 | player3 | player1) - player4}")


if __name__ == "__main__":
    main()
