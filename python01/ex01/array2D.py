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
        print(familyArray.shape)
        newArray = familyArray[start:end]
        print(newArray.shape)

        return (newArray.tolist())
    except IndexError as e:
        print("Slice_me Index error: ", e)
