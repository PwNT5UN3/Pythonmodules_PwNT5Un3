class AchievementHunter:
    '''defines a user that can gain achievements'''

    unlock_count = {}
    all_players = set()

    def __init__(self, username: str) -> None:
        '''creates a new user'''
        self.achievements = set()
        self.username = username
        AchievementHunter.all_players.add(self)

    def unlock_achievement(self, achievement: str):
        '''
        adds an achievement to the users achievements
        and increasesthe global unlock counter
        '''
        self.achievements.add(achievement)
        try:
            AchievementHunter.unlock_count[achievement] += 1
        except KeyError:
            AchievementHunter.unlock_count[achievement] = 1

    def get_achievements(self):
        '''prints one users achievements'''
        print(f'Player {self.username} achievements: {self.achievements}')

    def compare_achievements(self, other):
        '''compares two users and what achievements both users have'''
        print('common achievements between ',
              f'{self.username} and {other.username}: ',
              f'{self.achievements.intersection(other.achievements)}')

    def get_missing_achievements(self):
        '''
        compares one users achievements to the global achievement pool
        for those the user hasnt unlocked yet
        '''
        all_achievements = self.achievements
        for user in AchievementHunter.all_players:
            all_achievements = all_achievements.union(user.achievements)
        print(f'Player {self.username} missing achievements: ',
              f'{all_achievements.difference(self.achievements)}')

    def get_unique_achievements(self):
        '''checks one users achievements for unique achievements'''
        unique = self.achievements
        for user in AchievementHunter.all_players:
            if user.username == self.username:
                continue
            unique = unique.difference(user.achievements)
        print(f'Player {self.username} unique achievements: {unique}')

    @classmethod
    def get_rarest_achievements(cls):
        '''checks all achievements for thos =e with the lowest unlock rate'''
        rarest = set()
        unlocks = min(cls.unlock_count.values())
        for achievement in cls.unlock_count.keys():
            if cls.unlock_count[achievement] == unlocks:
                rarest.add(achievement)
        if (unlocks == 1):
            print(f'Rarest Achievement ({unlocks} Player ',
                  f'({((unlocks / len(cls.all_players)) * 100):.2f}%)): ',
                  f'{rarest}')
        else:
            print(f'Rarest Achievements ({unlocks} Players ',
                  f'({((unlocks / len(cls.all_players)) * 100):.2f}%)): ',
                  f'{rarest}')

    @classmethod
    def get_most_common_achievements(cls):
        '''checks all achievements for thos =e with the highest unlock rate'''
        most_common = set()
        unlocks = max(cls.unlock_count.values())
        for achievement in cls.unlock_count.keys():
            if cls.unlock_count[achievement] == unlocks:
                most_common.add(achievement)
        if (len(most_common) == 1):
            print(f'Most common Achievement ({unlocks} Players ',
                  f'({((unlocks / len(cls.all_players)) * 100):.2f}%)): ',
                  f'{most_common}')
        else:
            print(f'Most common Achievements ({unlocks} Players ',
                  f'({((unlocks / len(cls.all_players)) * 100):.2f}%)): ',
                  f'{most_common}')

    @classmethod
    def get_all_unique_achievements(cls):
        '''checks all achievements for those that have only one unlock'''
        uniques = set()
        for achievement in cls.unlock_count.keys():
            if cls.unlock_count[achievement] == 1:
                uniques.add(achievement)
        print(f'All unique achievements: {uniques}')
        print(f'Total unique achievements {len(uniques)}')


def achievement_system_test():
    '''tests the achievement systemm '''
    print('=== Achievemt system test ===')
    alice = AchievementHunter('Alice')
    alice.unlock_achievement('first_kill')
    alice.unlock_achievement('first_killx2')
    bob = AchievementHunter('Bob')
    bob.unlock_achievement('first_kill')
    bob.unlock_achievement('level_10')
    alice.compare_achievements(bob)
    AchievementHunter.get_rarest_achievements()
    AchievementHunter.get_most_common_achievements()
    alice.get_achievements()
    alice.get_missing_achievements()
    alice.get_unique_achievements()


if __name__ == '__main__':
    achievement_system_test()
