class Item:
    '''describes an Item'''
    def __init__(self, name: str, type: str, value: int, quality: str) -> None:
        '''makes an item'''
        self.name = name
        self.type = type
        self.value = value
        self.quality = quality


class InventoryMaster:
    '''describes a players inventory'''

    total_item_counts = {}
    all_item_quantities = {}
    all_players = []

    def __init__(self, owner: str) -> None:
        '''creates the inventory'''
        self.inventory = dict()
        self.inventory_indices = dict()
        self.owner = owner
        InventoryMaster.total_item_counts[owner] = 0
        InventoryMaster.all_players.append(self)

    def add_item_stack(self, new_item_stack: Item, quantity: int):
        '''adds multiple of the same item to an inventory'''
        for item in range(quantity):
            self.add_item(new_item_stack)

    def add_item(self, new_item: Item):
        '''adds one item to an inventory'''
        self.inventory[new_item] = self.inventory.get(new_item, 0) + 1
        self.inventory_indices[len(self.inventory_indices.keys())] = new_item
        InventoryMaster.total_item_counts[self.owner] += 1
        InventoryMaster.all_item_quantities[new_item] = \
            InventoryMaster.all_item_quantities.get(new_item, 0) + 1

    def inventory_breakdown(self):
        '''gives a detailed breakdown'''
        total_value = 0
        types = {}
        print(f"=== {self.owner}'s Inventory ===")
        for item in self.inventory.keys():
            item_count = self.inventory[item]
            print(f'{item.name} ({item.type}, {item.quality}): ',
                  f'{item_count}x @ {item.value} gold = ',
                  f'{item_count * item.value} gold')
            total_value += self.inventory.get(item) * item.value
            types[item.type] = types.get(item.type, 0) + item_count
        print(f'\nInventory Value: {total_value}')
        print('Item count: ',
              f'{InventoryMaster.total_item_counts.get(self.owner)} items')
        print('Categories: ', end='')
        for category in types.keys():
            print(f'{category}({types[category]}), ', end='')
        print(end='\n\n')

    def transfer_item(self, other, item: Item, quantity: int):
        '''transfers a quantity of an item from one player to another'''
        print('=== Transaction: ',
              f'{self.owner} gives {other.owner} {quantity} {item.name} ===')
        try:
            available = self.inventory[item]
        except KeyError:
            available = 0
        if available < quantity:
            print(f"Can't transfer {quantity} of {item.quality} {item.name}!")
            print(f"Not enough {item.quality} {item.name} owned!\n")
            return
        self.inventory[item] -= quantity
        other.inventory[item] = other.inventory.get(item, 0) + quantity
        print('=== Transaction successful ===')
        print('=== Updated Inventories ===')
        self.inventory_breakdown()
        other.inventory_breakdown()

    @classmethod
    def get_rarest_items(cls):
        '''checks wich items are the most rare'''
        item_counts = min(cls.all_item_quantities.values())
        rarest = set()
        for item in cls.all_item_quantities.keys():
            if cls.all_item_quantities.get(item) == item_counts:
                rarest.add(item.name)
        print('Rarest items: ', end='')
        for item in rarest:
            print(item, end=', ')
        print()

    @classmethod
    def get_highest_networth_player(cls):
        '''checks what player(s) have the highest net worth'''
        biggest_net_worth = 0
        forbes_list = set()
        for player in cls.all_players:
            net_worth = 0
            for item in player.inventory.keys():
                net_worth += player.inventory[item] * item.value
            if net_worth > biggest_net_worth:
                biggest_net_worth = net_worth
                forbes_list.clear()
                forbes_list.add(player.owner)
            elif net_worth == biggest_net_worth:
                forbes_list.add(player.owner)
        print(f'Most valuable inventorie(s) @ {biggest_net_worth}: ', end='')
        for name in forbes_list:
            print(name, end=' ')
        print()


def inventory_tester():
    '''tests the inventory system'''
    alice = InventoryMaster('alice')
    bob = InventoryMaster('bob')
    alice.add_item(Item('Sword', 'weapon', 100, 'legendary'))
    bob.add_item(Item('Magic ring', 'artifact', 345, 'legendary'))
    alice.add_item_stack(Item('Health potion', 'potion', 20, 'common'), 10)
    alice.add_item_stack(Item('Mana potion', 'potion', 25, 'common'), 5)
    alice.transfer_item(bob, alice.inventory_indices[0], 2)
    alice.transfer_item(bob, alice.inventory_indices[1], 2)
    alice.inventory_breakdown()
    print('\n=== Inventory Analytics ===')
    InventoryMaster.get_rarest_items()
    InventoryMaster.get_highest_networth_player()


if __name__ == '__main__':
    inventory_tester()
