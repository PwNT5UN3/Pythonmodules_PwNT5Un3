def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "grams":
        print(f'{seed_type.capitalize()} seeds: {quantity} grams total')
    elif unit == "packets":
        print(f'{seed_type.capitalize()} seeds: {quantity} packets available')
    elif unit == "area":
        name = seed_type.capitalize()
        print(f'{name} seeds: covers {quantity} square meters')
    else:
        print('Unknown unit type')
