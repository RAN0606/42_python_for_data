# from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """

    try:
        inverted_array = np.subtract(255, array)

        # Image.fromarray(inverted_array).show()
        plt.title('Figure: invert')
        plt.imshow(inverted_array)
        plt.show()
        return inverted_array
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red color channel of the image.
    """
    try:
        red_pixel = array[:, :, 0]
        print(red_pixel)
        array_filtered = np.zeros_like(array)
        array_filtered[:, :, 0] = red_pixel
        # Image.fromarray(array_filtered).show()
        plt.title('Figure: red')
        plt.imshow(array_filtered)
        plt.show()
        return array_filtered

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green color channel of the image.
    """
    try:
        green_pixel = array[:, :, 1]
        array_filtered = np.zeros_like(array)
        array_filtered[:, :, 1] = green_pixel
        # Image.fromarray(array_filtered).show()
        plt.title('Figure: green')
        plt.imshow(array_filtered)
        plt.show()
        return array_filtered

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue color channel of the image.
    """
    try:
        blue_pixel = array[:, :, 2]
        array_filtered = np.zeros_like(array)
        array_filtered[:, :, 2] = blue_pixel
        # Image.fromarray(array_filtered).show()
        plt.title('Figure: blue')
        plt.imshow(array_filtered)
        plt.show()
        return array_filtered

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Transform rgb color to grey.
    """
    try:
        red_pixel = array[:, :, 0]
        green_pixel = array[:, :, 1]
        blue_pixel = array[:, :, 2]
        grey = (0.2989*red_pixel + 0.5870*green_pixel
                + 0.1140 * blue_pixel).astype(np.uint8)
        plt.title('Figure: grey')
        plt.imshow(grey, cmap='gray')
        plt.show()
        # Image.fromarray(grey, mode='L').show()
        return grey

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass
