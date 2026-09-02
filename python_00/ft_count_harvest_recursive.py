def ft_recursion(n: int) -> None:
    if (n == 1):
        return print("Day ", n)
    else:
        ft_recursion(n - 1)
        print("Day ", n)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_recursion(days)
    print("Harvest time!")
