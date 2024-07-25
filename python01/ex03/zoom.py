from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str, x_start: int, y_start: int) -> np.array:

    """
    ft_zoom(path: str, x_start: int, y_start:int, x_end: int,
    y_end: int) -> np.array
    take the image print its imformation, zoom and display it.
    """
    try:
        imageArray = ft_load(path)
        print(imageArray)
        # Extract the specified region
        r, g, b = imageArray[:, :, 0:1], imageArray[:, :, 1:2], \
            imageArray[:, :, 2:3]
        gray = (0.2989 * r + 0.5870 * g + 0.1140 * b).astype(int)
        zoomed_region = gray[y_start:y_start+400, x_start:x_start+400]
        print("New shape after Transpose: ", zoomed_region .shape)
        print(gray)
        plt.subplot(1, 1, 1)
        plt.title('Zoomed Region')
        plt.imshow(zoomed_region, cmap='gray')
        plt.show()

        return zoomed_region
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    ft_zoom("animal.jpeg", 450, 70)


if __name__ == "__main__":
    main()
