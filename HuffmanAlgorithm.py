# Seyyedali Shohadaalhosseini
from itertools import chain
import matplotlib.image as mpimg


def mainFunc():
    pixels_flattened, img_pixels_matrix = Read_input()
    symbols, frequencies = calculateThePixelsAndFrequency(pixels_flattened, img_pixels_matrix)
    symbolAndFrequency = connectSymbolsToFrequencies(symbols, frequencies)
    SortedSymbolFreq = sortTheDataBy(symbolAndFrequency)
    print(SortedSymbolFreq)


def Read_input(imagePath='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\img0-gray.jpg'):
    img_pixels_matrix = mpimg.imread(imagePath)
    # print(img_pixels_matrix)
    # print(img_pixels_matrix.shape)
    # print(type(img_pixels_matrix))
    # print(img_pixels_matrix[1].shape)
    img_pixels_flattened = list(chain(*img_pixels_matrix))  # here we have flattened our list
    # print(img_pixels_flattened)
    return img_pixels_flattened, img_pixels_matrix


def calculateThePixelsAndFrequency(img_pixels_flattened, img_pixels_matrix):
    symbols = list()
    frequencies = list()
    max_pixels = img_pixels_matrix.shape[0] * img_pixels_matrix.shape[1]  # To calculate the probability
    for pixel in img_pixels_flattened:
        if pixel in symbols:
            continue
        symbols.append(pixel)
        frequencies.append((img_pixels_flattened.count(pixel)) / max_pixels)
    return symbols, frequencies


def connectSymbolsToFrequencies(symbols, frequencies):
    connectList = list()
    if len(symbols) == len(frequencies):
        for index in range(len(symbols)):
            connectList.append([symbols[index], frequencies[index]])
    return connectList


def sortTheDataBy(data):
    data.sort(key=lambda x: x[1], reverse=True)
    return data


mainFunc()
