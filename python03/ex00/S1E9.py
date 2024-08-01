from abc import ABC, abstractmethod


class Character(ABC):
    """
    docstring for Class Character:
    An abstract base class representing the character.
    This class cannot be instantiated directly."""

    @abstractmethod
    def __init__(self, firstname, is_alive=True):
        """
        docstring for Constructor of abstract class:
        This is a constructor from abstract class Character.
        """
        pass

    def die(self):
        """
        docstring for die method of abstract class
        This is a die methord of an abstract class Character
        """
        pass


class Stark(Character):
    """
    docstring for Class Stark:
    A class representing the Stark Character
    Inheritate the abstract class character.
    """
    def __init__(self, firstname, is_alive=True):
        """
        docstring for Constructor of class Stark:
        Stark character has been created
        """
        self.first_name = firstname
        self.is_alive = is_alive

    def die(self):
        """
        Docstring for die method of Class Stark:
        the character is die.
        """
        self.is_alive = False
