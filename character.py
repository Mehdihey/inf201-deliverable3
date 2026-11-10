# Object-oriented game simulator
# Turid Torheim, NMBU, 2026
from items import Weapon
class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon|None =None) -> None: # Change here to take a weapon
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> int: 
        """Reduce this character's own HP. HP cannot go below 0.
        Args:
            amount (int): The amount of damage to take.
        Returns:
            int: The actual damage taken."""
        
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        hp_before = self._hp
        self._hp = max(self._hp - amount, 0) #HP can never drop below 0
        return hp_before - self._hp

    def heal(self, amount: int) -> int:
        """Increase this character's own hp, hp cannot exceed hp-max.
        Args: 
        amount: Amount of hp to restore 
        Returns:
            int: the HP actually restored"""

        if amount < 0:
            raise ValueError ("Heal amount cannot be negative")
        hp_before = self._hp
        self._hp = min(self._hp + amount, self.hp_max)
        return self._hp - hp_before 


    def attack(self, target) -> int:
        """Attack the target by asking it to take damage."""
        """Attack the target, uses the weapon's dice roll if a weapon is equipped, otherwise the character's base damage"""
        
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        return target.take_damage(damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def is_alive(self) -> bool:
        """read only property: true if the character is alive."""
        return self._hp > 0
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

if __name__ == "__main__":

    #Quick test
    a = Character("Alice")
    b = Character("Bob")

    a.attack(b)
    print(b.hp)
    a.attack(b)
    print(b.hp)

    b.heal(10)
    print(b.hp)

    b.heal(500)
    print(b.hp)

    b.take_damage(999)
    print(b.hp)
    print(b.is_alive)
    
    b.heal(1)
    print(b.is_alive)

    print(repr(b))

#Task 3:
from dice import Dice #only needed for this test
sword = Weapon("Sword", Dice(sides=8))
knight = Character("Knight", weapon = sword)
peasant = Character("Peasant") #no weapon
dummy = Character("Dummy")

print("Knight with sword (1-8):")
for _ in range(5):
    print(knight.attack(dummy)) # random 1-8 each time

print("Peasant without weapon (always 10):")

for _ in range(3):
    print(peasant.attack(dummy)) #allways 10

print(dummy.hp)
