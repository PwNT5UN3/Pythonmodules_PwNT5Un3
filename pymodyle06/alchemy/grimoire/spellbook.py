def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingrediants
    verdict = validate_ingrediants(ingredients)
    if verdict == f'{ingredients} - VALID':
        return f'Spell recorded: {spell_name} ({verdict})'
    return f'Spell rejected: {spell_name} ({verdict})'
