class GardenManager:
    '''defines a Gardener'''
    garden_count = 0
    gardens = []

    def __init__(self, owner: str):
        '''Creates a gardener object'''
        self.plants = []
        self.owner = owner
        GardenManager.gardens.append(self)
        self.stats = GardenManager.GardenStats()
        GardenManager.garden_count += 1

    class GardenStats:
        '''defines the nested statistic class'''
        def __init__(self):
            '''Creates a statistic'''
            self.plant_counter = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0
            self.garden_points = 0

    def add_plant(self, name: str, height: int):
        '''Creates and adds a regular plant to a garden'''
        self.plants.append(Plant(name, height))
        print(f"Added {name} to {self.owner}'s garden")
        self.stats.plant_counter += 1
        self.stats.regular_plants += 1
        self.stats.garden_points += height

    def add_flowering_plant(self, name: str, height: int, color: str):
        '''Creates and adds a flowering plant to a garden'''
        self.plants.append(FloweringPlant(name, height, color))
        print(f"Added {name} to {self.owner}'s garden")
        self.stats.plant_counter += 1
        self.stats.flowering_plants += 1
        self.stats.garden_points += height

    def add_flower(self, name: str, height: int, color: str, points: int):
        '''Creates and adds a full flower to a garden'''
        self.plants.append(PrizeFlower(name, height, color, points))
        print(f"Added {name} to {self.owner}'s garden")
        self.stats.plant_counter += 1
        self.stats.prize_flowers += 1
        self.stats.garden_points += points + height

    def grow_plants(self):
        '''This lets all plants grow by 1 cm'''
        print(f'{self.owner} is helping all plants grow...')
        for plant in self.plants:
            print(f'{plant.name} grew 1cm')
            plant.height += 1
            self.stats.garden_points += 1
            self.stats.total_growth += 1
        print('')

    def make_report(self):
        '''gives a report about a garden'''
        print(f"=== {self.owner}'s Garden Report")
        for plant in self.plants:
            print(f'- {plant.name}: {plant.height}cm')
        print(f'\nPlants added: {self.stats.plant_counter}')
        print(f'\nTotal growth: {self.stats.total_growth}cm')
        print('Plant types:')
        print(f'     {self.stats.regular_plants} regular')
        print(f'     {self.stats.flowering_plants} flowering')
        print(f'     {self.stats.prize_flowers} prize flowers\n')

    @classmethod
    def check_heights(cls):
        '''this checks all plants in a garden if they have a positive height'''
        print('Height validation test: ', end='')
        for garden in cls.gardens:
            for plant in garden.plants:
                if (plant.height < 0):
                    print('False')
                    return
        print('True')

    @classmethod
    def grade_gardens(cls):
        '''this grabs and prints all garden scores'''
        print('Garden scores - ', end='')
        index = 0
        for garden in cls.gardens:
            print(garden.owner, ': ', garden.stats.garden_points, end='')
            index += 1
            if index < GardenManager.garden_count:
                print(', ', end='')
        print('')

    @staticmethod
    def get_garden_count():
        '''this prints how many gardens exist'''
        print(f'Total gardens managed: {GardenManager.garden_count}')

    @staticmethod
    def create_garden_network(owners: list[str]) -> list:
        '''this makes a group of gardeners in bulk'''
        garden_owners = []
        for owner in owners:
            garden_owners.append(GardenManager(owner))
        return garden_owners


class Plant:
    '''defines a regular plant'''
    def __init__(self, name: str, height: int):
        '''makes a regular plant'''
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    '''defines a flowering plant'''
    def __init__(self, name: str, height: int, color: str):
        '''makes a flowering plant'''
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    '''defines a prize flower'''
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        '''makes a prize flower'''
        super().__init__(name, height, color)
        self.prize_points = prize_points


def test_manger():
    '''Tests the manger class and methods'''
    print('=== Garden Management System Demo ===\n')
    owners = ['Alice', 'Bob']
    owners = GardenManager.create_garden_network(owners)
    alice = owners[0]
    bob = owners[1]
    alice.add_plant('rose', 15)
    alice.add_flowering_plant('oak', 200, 'brown')
    alice.add_flower('tulip', 23, 'blue', 10)
    print('')
    alice.grow_plants()
    alice.make_report()
    bob.add_flowering_plant('potato', 15, 'yellow')
    GardenManager.check_heights()
    GardenManager.grade_gardens()
    GardenManager.get_garden_count()


if __name__ == '__main__':
    test_manger()

