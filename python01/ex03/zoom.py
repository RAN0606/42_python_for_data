from load_image import ft_load
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt

def ft_zoom(path: str, x_start: int, y_start:int) -> np.array:
    """
    ft_zoom(path: str, x_start: int, y_start:int, x_end: int, y_end: int ) -> np.array
    take the image print its imformation and display it.
    """
    imageArray = ft_load(path)
    plt.imshow(img)


def main():
    ft_zoom("animal.jpeg", 0, 0)


if __name__ == "__main__":
    main()