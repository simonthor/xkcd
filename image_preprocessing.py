import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from typing import Tuple


#%%
#TODO: turn image into grayscale?
def image_as_array(filename, size: Tuple[int, int] = (2000, 2000), insert='center'):
    """Read image and return as numpy array (standardzed size)"""
    size = np.asarray(size)
    raw_image_arr = imread(filename)

    if not (np.asarray(raw_image_arr.shape[:2]) <= size).all():
        return

    std_image = np.ones((*size, 3))
    if insert == 'center':
        half_padding = (size - np.asarray(raw_image_arr.shape[:2])) // 2
        std_image[half_padding[0]:half_padding[0]+raw_image_arr.shape[0], half_padding[1]:half_padding[1]+raw_image_arr.shape[1], :] = raw_image_arr[:, :, :3]
    elif insert == 'upper left':
        std_image[:raw_image_arr.shape[0], :raw_image_arr.shape[1], :] = raw_image_arr[:, :, :3]
    else:
        raise ValueError(f"Expected 'insert' to be 'center' or 'upper left' but got '{insert}'.")

    return std_image


#%%
if __name__ == '__main__':
    im = image_as_array(r'C:\Users\simon\Pictures\Saved Pictures\cms jet search.png')
    plt.imshow(im)
    plt.show()
