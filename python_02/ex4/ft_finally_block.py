#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Caught PlantError: Invalid plant name to water:"
                         f"'{plant_name}'")


def test_watering_system(*plants: str) -> None:
    print("Opening watering system")
    try:
        for i in range(len(plants)):
            water_plant(plants[i])
    except PlantError as e:
        print(f"{e}\n.. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system("Tomatto", "Lettuce", "Carrots")
    print("\nTesting invalid plants...")
    test_watering_system("Tomatto", "lettuce", "Carrots")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
