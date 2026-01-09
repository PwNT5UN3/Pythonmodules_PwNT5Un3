def validate_ingrediants(ingredients: str) -> str:
    valid = ['fire', 'water', 'earth', 'air']
    ingrediant_list = ingredients.split(' ')
    ingrediant_list = [i for i in ingrediant_list if i not in valid]
    if len(ingrediant_list) != 0:
        return f'{ingredients} - INVALID'
    return f'{ingredients} - VALID'
