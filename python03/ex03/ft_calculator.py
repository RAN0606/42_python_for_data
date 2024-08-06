class calculator:
    """
    a calculator class that is able to do calculations
    (addition, multiplication, subtraction, division) of vector with a scalar
    """
    def __init__(self, vector):
        """
        The constructor of the class ft_caculator.
        Initializes the calculator with the provided vector
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Addition of vector and scalar provided
        """
        self.vector = [elem + object for elem in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """
        Multiplication of vector and scalar provided
        """
        self.vector = [elem * object for elem in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        """
        Substraction of  scalar provided from vector.
        """
        self.vector = [elem - object for elem in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        """
        division of vector by scalar
        """

        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
