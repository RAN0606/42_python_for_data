class calculator:
    """
    staticmethod class: these method can be called
    on the class itself without creating an instance
    of the class
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.
        """
        dot_product = 0.0
        for i in V1:  # Assuming V1 and V2 have the same length
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(float(i + V2[V1.index(i)]))
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(float(i - V2[V1.index(i)]))
        print(f"Sous Vector is: {result}")
