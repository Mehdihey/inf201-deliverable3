#Item classes for the RPG battle simylator
from dice import Dice
class Weapon:
    """Represents a weapon whose damge is determined by rolling a dice"""
    def __init__(self, name:str, damage_dice:Dice) -> None:
        """
        Initialise the weapon
        Args:
            name(stra):the name of the weapon
            damage_dice(Dice): the dice rolled to determine damage
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice and return the result"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of a weapon object"""
        return f"Weapon(name='{self.name}', damage_dice)={self.damage_dice})"


if __name__ == "__main__":
    #Quick test
    sword = Weapon("Sword", Dice(sides=8))
    dagger = Weapon("Dagger", Dice(sides=4))

    print(sword) 
    print(dagger)

    print(sword.roll_damage())
    print(dagger.roll_damage())