#!/usr/bin/env Compression_Analysis
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: PSNR.py
#@time: 2019/6/25 17:27
#@Ducument：https://www.python.org/doc/
#@desc:

import numpy as np
import math
import cv2


def Representational(r, b, g):
    return (0.299 * r + 0.287 * g + 0.114 * b)


def calculate(img):
    b, g, r = cv2.split(img)
    pixelAT = Representational(r, g, b)
    return pixelAT


def main():

    # loading images (original image and compressed image)

    original_image = cv2.imread('orignal_image.png',1)
    compressed_image = cv2.imread('compressed_image.png',1)

    height,width = original_image.shape[:2]

    originalPixelAt = calculate(original_image)
    compressedPixelAt = calculate(compressed_image)

    diff = originalPixelAt-compressedPixelAt
    error = np.sum(np.abs(diff)**2)

    # MSE
    error = error/(height*width)

    PSNR = -(10*math.log10(error/(255*255)))

    print("PSNR value is {}".format(PSNR))

if __name__ == '__main__':
    main()
