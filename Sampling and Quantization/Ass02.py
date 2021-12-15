import matplotlib.pyplot as plt
from skimage import io, color, util
from skimage.transform import rescale, resize, downscale_local_mean
from sklearn.cluster import KMeans

def sampling():
    img = io.imread("MrGenie.JPG")
    fig, axes = plt.subplots(nrows=2, ncols=3)
    ax = axes.ravel()
    ax[0].imshow(img)
    ax[0].set_title("Original")

    for k in range(5, 0, -1):
        print(k)
        img_resized = resize(img, (img.shape[0] // 2**k, img.shape[1] // 2**k),
                             anti_aliasing=True)
    
        ax[k].imshow(img_resized)
        ax[k].set_title("x"+ str(2**k))

    plt.tight_layout()
    plt.show()


def quantization():
    original = io.imread("MrGenie.JPG")
    fig, axes = plt.subplots(nrows=2, ncols=3)
    ax = axes.ravel()
    ax[5].imshow(original)
    ax[5].set_title("original")
    
    for k in range(1, 6, 1):
        n_colors = 2**k
        arr = original.reshape((-1, 3))
        kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(arr)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        less_colors = centers[labels].reshape(original.shape).astype('uint8')

        print(k-1)
        ax[k-1].imshow(less_colors)
        ax[k-1].set_title(str(n_colors) + " colors")

    plt.tight_layout()
    plt.show()
    
    
if __name__ == '__main__':
    x = int(input("Sampling Enter 1 | Quantization Enter 2: "))
    if x == 1:
        sampling()
    elif x == 2:
        print("program will take a while")
        quantization()
