from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str, x_start: int, y_start: int) -> np.array:
    """
    ft_zoom(path: str, x_start: int, y_start:int, x_end: int,
    y_end: int ) -> np.array
    take the image print its imformation and display it.
    """
    imageArray = ft_load(path)
    print(imageArray)
    # Extract the specified region
    r, g, b = imageArray[:, :, 0:1], imageArray[:, :, 1:2],
    imageArray[:, :, 2:3]
    gray = (0.2989 * r + 0.5870 * g + 0.1140 * b).astype(int)
    zoomed_region = gray[y_start:y_start+400, x_start:x_start+400]
    print("New shape after Transpose: ", gray.shape)
    print(gray)

    # plt.subplot(1, 1, 1)
    # plt.title('Zoomed Region')
    # plt.imshow(zoomed_region, cmap = 'gray')
    # plt.show()
    return zoomed_region


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """
    ft_rotate(img : np.array) rotate the image
    """
    if not isinstance(img, np.ndarray):
        return print("Can't rotate with img argument NULL")
    rotateimg = np.transpose(img, (1, 0, 2))
    print("New shape after Transpose2: ", rotateimg.shape)
    print(rotateimg)

    plt.subplot(1, 1, 1)
    plt.title('rotate')
    plt.imshow(rotateimg, cmap='gray')
    plt.show()
    return (rotateimg)


def main():
    ft_rotate(ft_zoom("./animal.jpeg", 450, 50))


if __name__ == "__main__":
    main()
