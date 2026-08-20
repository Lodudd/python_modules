def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print (seed_type.capitalize(), "seeds:", f"{quantity} packets avaible")
    elif unit == "grams":
        print (seed_type.capitalize(), "seeds:", f"{quantity} grams total")
    elif unit == "area":
        print (seed_type.capitalize(), "seeds:", f"covers {quantity} square meters")
    else:
        print ("Unknown unit type")


if __name__ == "__main__":
    ft_seed_inventory("JEDEN", 3, "packets")
    ft_seed_inventory("JEDEN", 3, "grams")
    ft_seed_inventory("JEDEN", 3, "areaaaaa")
