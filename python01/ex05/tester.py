from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def display_images(image_paths):
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # Create a 2x3 grid of subplots

    for i, img in enumerate(image_paths):
        ax = axes[i // 3, i % 3]  # Determine position in grid
        ax.imshow(img, cmap='gray')
        ax.set_title(f'Image {i+1}')
        ax.axis('off')  # Hide the axes

    plt.tight_layout()  # Adjust subplots to fit into figure area.
    plt.show()


def main():
    array = ft_load("landscape.jpg")
    # plt.title('Figure: original')
    # plt.imshow(array)
    # plt.show()
    # ft_invert(array)
    # ft_red(array)
    # ft_green(array)
    # ft_blue(array)
    # ft_grey(array)

    print(ft_invert.__doc__)
    image_paths = [
        array,
        ft_invert(array),
        ft_red(array),
        ft_green(array),
        ft_blue(array),
        ft_grey(array)
    ]
    display_images(image_paths)


# Example usage:



if __name__ == "__main__":
    main()
