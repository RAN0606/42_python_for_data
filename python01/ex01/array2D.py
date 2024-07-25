import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(family: list, start: int, end: int) -> list
takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments.
You must use the slicing method.
    """
    try:
        familyArray = np.array(family)
        print("My shape is : ", familyArray.shape)
        newArray = familyArray[start:end]
        print("My new shape is : ", newArray.shape)

        return (newArray.tolist())
    except IndexError as e:
        print("Slice_me Index error: ", e)
    except ValueError as e:
        print("Slice_me Value error: ", e)
