# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions.

# Idea: use convolution with filter kernel with 1's for all the 8 positions.

# https://docs.opencv.org/4.x/db/dd1/tutorial_py_pip_install.html
# https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
# with open('example.txt') as f:
with open('input.txt') as f:
    matrix = []
    for line in f:
        line = line.strip()
        row = [1 if i == "@" else 0 for i in line]
        matrix.append(row)

    img = np.array(matrix, dtype=np.float32)

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], np.float32)

dst = cv.filter2D(img,-1,kernel, borderType=cv.BORDER_CONSTANT)

dst = (dst < 4) * img

# print(dst)
print(np.sum(dst))
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

