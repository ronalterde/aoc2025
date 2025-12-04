import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
with open('example.txt') as f:
# with open('input.txt') as f:
    matrix = []
    for line in f:
        line = line.strip()
        row = [1 if i == "@" else 0 for i in line]
        matrix.append(row)

    img = np.array(matrix, dtype=np.float32)

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], np.float32)

dst = img
for _ in range(100):
    dst = cv.filter2D(dst, -1, kernel, borderType=cv.BORDER_CONSTANT)
    dst = (dst >= 4) * img
    print(np.sum(img) - np.sum(dst))

