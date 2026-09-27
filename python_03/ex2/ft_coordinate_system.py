#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input("Enter new coordinates as"
                            " floats in format"
                            " 'x,y,z': ").replace(" ", "").split(",")
        new_coordinates = []
        try:
            if len(coordinates) != 3:
                raise NameError("Syntax Error")
            for item in coordinates:
                new_coordinates.append(float(item))

        except ValueError as e:
            print(f"Error on parameter'{item}': {e}")

        except NameError as e:
            print(e)

        counter = 0
        if len(coordinates) == 3:
            for i in range(len(coordinates)):
                if isinstance(new_coordinates[i], str):
                    break
                counter += 1
        if counter == len(coordinates):
            return (new_coordinates[0],
                    new_coordinates[1],
                    new_coordinates[2])


def calculate_distance(player1: tuple[float, float, float],
                       player2: tuple[float, float, float]) -> float:
    distance = math.sqrt((player2[0]-player1[0])**2 +
                         (player2[1]-player1[1])**2 +
                         (player2[2]-player1[2])**2)
    return distance


def main() -> None:
    cordinates = get_player_pos()
    print(f"Got a first tuple: {cordinates}")
    print(f"It includes: X={cordinates[0]},"
          f" Y={cordinates[1]}, Z={cordinates[2]}")
    print(f"Distance to center: "
          f"{calculate_distance(cordinates, (0.0, 0.0, 0.0)):.3f}")
    cordinates2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates:: "
          f"{round(calculate_distance(cordinates2, cordinates), 3)}")


if __name__ == "__main__":
    main()
