#!/usr/bin/env python3
import random
from typing import Generator


def get_event() -> Generator[tuple[str, str], None, None]:
    names = ["Alice", "Bob", "Dylan", "Charlie"]
    actions = ["Run", "Eat", "Sleap", "Move"]
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(lista: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while len(lista):
        element = random.choice(lista)
        lista.remove(element)
        yield element


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = get_event()
    for i in range(10):
        next_event = next(gen)
        print(f"Event {i}: Player {next_event[0]} did action {next_event[1]}")

    new_list = []
    for i in range(10):
        new_list.append(next(gen))
    print(f"Built list of 10 events: {new_list}")

    for event in consume_event(new_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {new_list}")


if __name__ == "__main__":
    main()
