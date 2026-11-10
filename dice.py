# Dice class for the RPG battlesimulator
##INF201, DELI3
from dbm import error
import random

class Dice:
    """Represents an n-sided dice (n >=2 )"""
    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the dice
        
        Args:
            sides (int): The number of sides on the dice (default = 6)
        """ 
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self._sides = sides

    @property
    def sides(self) -> int:
        """Read-only property: number of sides on the dice"""
        return self._sides
    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and sides"""
        return random.randint(1, self._sides)
    def __repr__(self) -> str:
        """Representation of a dice object"""
        return f"Dice(sides={self._sides})"
    def __call__(self) -> int:
        """Allow the dice ti be calles directly, e.g. f20()"""
        return self.roll()

if __name__ == "__main__":
    #Quick test
    d6 =Dice()
    d20 = Dice(sides=20)

    print(d6) #Expected output: Dice(sides=6)
    print(d20) #Expected output: Dice(sides=20)

    print(d6.roll()) #a random number between 1-6
    print(d20.roll()) #a random number 1-20
    print(d20()) #also a random number between 1-20


    
    try:
        bad =Dice(sides=1)
    except ValueError as error:
        print("Error:", error)

    
