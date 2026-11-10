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


class Warrior(Character):
    """A defensive specialist whose armor reduces incoming damage """
    def __init__(self, name: str, hp_max: int = 100, damage:int = 10, weapon:Weapon | None = None, armor:int = 5) -> None:
        """
        Initialise the Warrior 
        
        Args:
            name, hp_max, damage, weapon: same as for charecter
            armor (int): Amount subtracted from every incoming hit

        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> int:
        """Reduce incoming damage by armor before applying it"""
        reduced = max(amount - self.armor, 0) #armor cannot turn a hit into healing
        return super().take_damage(reduced)
class Mage(Character):
    """ A resourse-based attacker that spends mana on double-damage spells"""
    def __init__(self, name:str, hp_max: int= 100, damage:int = 10, weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Initialise the mage
        
        Args:
            name, hp_max, damage, weapon: same as for character
            mana (int): starting mana points
            mana_max (int): maximum mana points
        """
        super().__init__(name, hp_max, damage, weapon)
        self._mana = mana #private, like_hp
        self.mana_max = mana_max

    @property
    def mana(self) -> int:
        """Read-omly property: current mana"""
        return self._mana

    def attack(self, target) -> int:
        """Cast a spell(double base damage, costs 10 mana) if enough mana,
         otherwise do a normal attack and regain5 mana """
        if self._mana >= 10:
            self._mana -= 10
            return target.take_damage(self.damage * 2) #Spell ignores weapon
        damage_dealt = super().attack(target) #normal attack, uses weapon if equipped
        self._mana = min(self._mana + 5, self.mana_max) #mana cannot exceed max
        return damage_dealt

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


# Task 4:Warrior test
tank = Warrior("Tank")
print(tank.armor) #Expected:5

peasant.attack(tank) #10 damage - 5 armor = 5
print(tank.hp) #Expected: 95

weak = Character("Weak", damage=3)
weak.attack(tank) # 3 - 5 -> 0 no healing
print(tank.hp) #Expected: 95 unchanged

tank.heal(5) #inherited from Character!
print(tank.hp) #Expected: 100
print(tank.is_alive) #Expected: True (also inherited)


# Task 3: Mage
staff = Weapon("Staff", Dice(sides=6))
merlin = Mage("Merlin", weapon=staff)
target = Character("Target, hp_max = 500") ##lots of HP

print(merlin.mana) #Expected: 30
for turn in range(1, 7):
    dealt = merlin.attack(target)
    print(f"Turn {turn}: dealt {dealt}, mana left {merlin.mana}")
