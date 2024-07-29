from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
ft_load(path: str) -> array:(you can return to the desired format)
loads an image, prints its format, and its pixels content in RGB format.
JPG and JPEG format, handle error with a clear error message.
    """

    try:
        with Image.open(path) as im:
            pixels_data = np.array(im)
            print(f"The shape of the image is: {pixels_data.shape}")
            return (pixels_data)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
