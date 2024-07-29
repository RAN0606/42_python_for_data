from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str, x_start: int, y_start: int) -> np.array:
    """
ft_zoom(path: str, x_start: int, y_start:int, x_end: int,
y_end: int ) -> np.array
take the image print its imformation and display it.
    """
    try:
        imageArray = ft_load(path)
        # Extract the specified region
        # r, g, b = imageArray[:, :, 0:1], imageArray[:, :, 1:2], \
        #     imageArray[:, :, 2:3]
        r, g, b = imageArray[:, :, 0], imageArray[:, :, 1], \
            imageArray[:, :, 2]
        gray = (0.2989*r + 0.5870*g
                + 0.1140 * b).astype(np.uint8)
        zoomed_region = gray[y_start:y_start+400, x_start:x_start+400]
        print("The shape of image is: ", zoomed_region.shape)
        print(gray)

        return zoomed_region
    except Exception as e:
        print(f"Error: {str(e)}")


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """
    ft_rotate(img : np.array) rotate the image
    """
    try:
        # rotateimg = np.transpose(img, (1, 0, 2))
        rotateimg = np.transpose(img, (1, 0))
        print("New shape after Transpose: ", rotateimg.shape)
        print(rotateimg)
        # arotateimg = rotateimg[:, :, 0]
        # print("New shape after Transpose: ", arotateimg.shape)
        # print(arotateimg)

        plt.subplot(1, 1, 1)
        plt.title('rotate')
        plt.imshow(rotateimg, cmap='gray')
        plt.show()
        return (rotateimg)
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    ft_rotate(ft_zoom("./animal.jpeg", 450, 50))


if __name__ == "__main__":
    main()
