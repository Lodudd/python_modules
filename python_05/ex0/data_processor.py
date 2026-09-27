#!/usr/bin/env python3

from abc import ABC, abstractmethod

def DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


def main():
    pass


if __name__ == "__main__":
    main()
