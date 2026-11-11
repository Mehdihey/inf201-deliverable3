# Battle class for the RPG battle simulator

from character import Character
"""manage turn-based combat between two character"""

class Battle:
    """Represents a battle between two characters"""
    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the battle

        Args:
            hero (Character): The hero character
            enemy (Character): The enemy character
        """
        self.hero = hero
        self.enemy = enemy
        self.round = 0 # number of rounds played so far

    def play_round(self) -> None:
        """Hero attacks enemy. If the enemy is still alive, it strikes back."""
        self.round += 1
        dealt = self.hero.attack(self.enemy)
        print(f"Round {self.round}: {self.hero.name} hits {self.enemy.name}"
            f" for {dealt} damage ({self.enemy.name}: {self.enemy.hp} HP left.")
        if self.enemy.is_alive: #a dead enemy cannot attack
            dealt = self.enemy.attack(self.hero)
            print(f"{self.enemy.name} hits {self.hero.name}"
                f" for {dealt} damage ({self.hero.name}: {self.hero.hp} HP left.)")

    def simulate_battle(self, max_rounds:int = 1000) -> Character | None:
        """
        Play rounds until one character is dead.
        Args:
            max_rounds (int): maximum number of rounds to play (default = 1000)
            Returns:
                Character | None: the winner, or None if no one won after max_rounds
        """
        while self.hero.is_alive and self.enemy.is_alive and self.round < max_rounds:
            self.play_round()
            # The loop stopped for one of two reasons. Which one?
        if self.hero.is_alive and self.enemy.is_alive:
            print(f"draw! NOBODY won after {self.round} rounds")
            return None
                            
            
        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"{winner.name} won after {self.round} rounds!"
              f"with {winner.hp} HP left!") 
        
        return winner

if __name__ == "__main__":
    #Quick test
    from character import Warrior, Mage
    from items import Weapon
    from dice import Dice

    #baattle 1: two basic characeters, no weapon
    print("=== Battle 1: Character vs Character ===")
    battle = Battle(Character("Hero"), Character("Villain")).simulate_battle()

    #Battle 2: warrior with sword vs mage with staff
    print("\n=== Battle 2: Warrior vs Mage ===")

    conan = Warrior("Conan", weapon=Weapon("Sword", Dice(sides=8)))
    merlin = Mage("Merlin", weapon=Weapon("Staff", Dice(sides=6)))

    #Battle 3: endless battle -> saftey limit

    print("\n=== Battle 3: two heavily armored warriors ===")
    tank1 = Warrior("Tank 1", armor =20)
    tank2 = Warrior("Tank 2", armor=20)

    Battle(tank1, tank2).simulate_battle(max_rounds=3)