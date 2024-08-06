from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    docstring for Class of the King:
    A class representing the King
    Inheritate the Baratheon and Lannister Class.
    """

    def __init__(self, firstname, is_alive=True):
        """
        docstring for Constructor of class Baratheon:
        Baratheon character has been created
        """
        super().__init__(firstname, is_alive)

    def set_eyes(self, color):
        """
        class method for set the color of eyes
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        class method for set the color of hairs.
        """
        self.hairs = color

    def get_eyes(self) -> str:
        """
        class method for get the color of eyes
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        class method for get the color of hairs.
        """
        return self.hairs
