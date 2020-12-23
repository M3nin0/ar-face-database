
import os
import glob

import numpy as np

from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize

OUT_SHAPE = (128, 128)

ar_database_images = glob.glob(os.path.join("ar_out", "*.jpeg"))
stack = np.zeros((
    len(ar_database_images), *OUT_SHAPE
))

for ar_image, idx in zip(ar_database_images, range(len(ar_database_images))):
    print(f"Processing image: {idx + 1}/{len(ar_database_images)}")
    image_arr = (rgb2gray(
        resize(imread(ar_image), OUT_SHAPE, anti_aliasing=True)
    ) * 100).astype(int)
    stack[idx, :, :] = image_arr

np.savez_compressed("ar_database_stacked_128x128", stack = stack)
