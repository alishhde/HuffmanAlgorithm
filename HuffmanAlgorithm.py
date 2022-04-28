# Seyyedali Shohadaalhosseini
import matplotlib.image as mpimg
from numpy import array
from PIL import Image as im


def mainFunc():
    pixels_flattened = Read_input()


def Read_input(imagePath='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\img0-gray.jpg'):
    img_pixels_matrix = mpimg.imread(imagePath)
    print(img_pixels_matrix.shape)
    print(type(img_pixels_matrix))
    print(img_pixels_matrix[1].shape)
    return img_pixels_matrix


mainFunc()
