import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
give_bmi(height: list[int | float],weight: list[int | float]) -> list[int |
float] take 2 lists of integers or floats in input and returns a list of BMI
values.
    """
    listbmi = []
    try:
        arH = np.array(height)
        arW = np.array(weight)
        listbmi = np.divide(arW, np.power(arH, 2)).tolist()
    except ValueError as e:
        print("give_bmi Error:", e)
    return (listbmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
apply_limit(bmi: list[int | float], limit: int) -> list[bool], accepts a list
of integers or floats and an integer representing a limit as parameters.
It returns a list of booleans (True if above the limit)
    """
    lists = []
    try:
        aBmi = np.array(bmi)
        lists = list(aBmi > limit)
    except TypeError as e:
        print("apply_limit TypeError: {}".format(e))
    return (lists)
