from S1E9 import Character


class Baratheon(Character):
    """docstring for Class of the family Baratheon:
    A class representing the Baratheon Family
    Inheritate the abstract class character.
    """

    def __init__(self, firstname, is_alive=True):
        """
        docstring for Constructor of class Baratheon:
        Baratheon character has been created
        """
        super().__init__(firstname, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"



#your code here
class Lannister(Character):
    """
    docstring for Class of the family Lannister:
    A class representing the Lannister Family
    Inheritate the abstract class character.
    """

    def __init__(self, firstname, is_alive=True):
        """
        docstring for Constructor of class Lannister:
        Lannister character has been created
        """
        super().__init__(firstname, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Create a Lannister character instance with custom is_alive status.
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance