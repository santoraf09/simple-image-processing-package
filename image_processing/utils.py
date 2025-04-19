import matplotlib.pyplot as plt
import imageio.v2 as imageio

def read_image(path):
    return imageio.imread(path)

def plot_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def plot_result(img1, img2, result):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for ax, img, title in zip(axs, [img1, img2, result], ["Image 1", "Image 2", "Result"]):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis("off")
    plt.show()
