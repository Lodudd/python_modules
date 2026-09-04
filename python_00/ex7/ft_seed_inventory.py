def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type.capitalize(), "seeds:", f"{quantity} packets avaible")
    elif unit == "grams":
        print(seed_type.capitalize(), "seeds:", f"{quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.title()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


if __name__ == "__main__":
    ft_seed_inventory("tomato", 3, "packets")
    ft_seed_inventory("CARROT", 3, "grams")
    ft_seed_inventory("Lettuce", 3, "area")
