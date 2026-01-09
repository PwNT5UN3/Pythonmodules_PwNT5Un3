from alchemy.grimoire.validator import validate_ingrediants
from alchemy.grimoire.spellbook import record_spell


def circular_curse_break() -> None:
    print('\n=== Circular Curse Breaking ===\n')
    print('Testing ingrediant validation:')
    print("validate_ingrediants('fire air'): " +
          f"{validate_ingrediants('fire air')}")
    print("validate_ingrediants('dragon scales') " +
          f"{validate_ingrediants('dragon scales')}")
    print('\nTesting spell recording with validation:')
    print("record_spell('Fireball', 'fire air'): " +
          f"{record_spell('Fireball', 'fire air')}")
    print("record_spell('Dark Magic', 'shadow'): " +
          record_spell('Dark Magic', 'shadow'))
    print('\nTesting late import technique:')
    from alchemy.grimoire.spellbook import record_spell as rs
    print("record_spell('Lightning', 'air'): " +
          rs('Lightning', 'air'))
    print('\nCircular dependency curse avoided using late imports!')
    print('All spells processed safely!')


if __name__ == '__main__':
    circular_curse_break()
