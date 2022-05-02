# Seyyedali Shohadaalhosseini - alishhde
import math
from itertools import chain
from numpy import array
import matplotlib.pyplot
import matplotlib.image as mpimg


def main():
    print("Reading your Input image...")
    pixels_flattened, img_pixels_matrix = Read_input()

    print("Calculating Symbols and their frequencies...")
    symbols, frequencies = calculateThePixelsAndFrequency(pixels_flattened, img_pixels_matrix)
    symbolAndFrequency = connectSymbolsToFrequencies(symbols, frequencies)

    print("Encoding data...")
    codesOfData = huffmanEncoding(symbolAndFrequency)
    print("Data encoded.")

    codedDataSent = huffmanSendCodedData(img_pixels_matrix, codesOfData)

    print("Decoding data...")
    huffmanDecoding(codedDataSent, codesOfData)
    print("Data decoded.")

    entropy = sourceEntropy(frequencies)
    print("The Entropy is :", entropy)

    minimumAverage = minimumAverageNumberOfBit(codesOfData, symbolAndFrequency)
    print("This is Minimum Average Number Of Bit: ", minimumAverage)


def Read_input(imagePath='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\img0-gray.jpg'):
    img_pixels_matrix = mpimg.imread(imagePath)
    img_pixels_flattened = list(chain(*img_pixels_matrix))  # here we have flattened our list
    return img_pixels_flattened, img_pixels_matrix


def huffmanEncoding(symbolAndFrequency):
    symbolsCode = list()
    TreeNodes = list()
    rootNodes = list()
    c = 0
    while len(symbolAndFrequency) > 1:
        SortedSymbolFreq = sortTheDataBy(symbolAndFrequency)
        low, lower, symbolAndFrequency = returnTwoLowest(SortedSymbolFreq)
        lowestSum = low[1] + lower[1]
        if len(TreeNodes) > 0:
            rootNodes = [val[0] for val in TreeNodes]
        if str(low[0]) in rootNodes and str(lower[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(low[0]):
                    del TreeNodes[index_Counter]
                elif val[0] == str(lower[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append(["{}-{}".format(low[0], lower[0]), lowestSum])  # Append the new one
            symbolAndFrequency.append(["{}-{}".format(low[0], lower[0]), lowestSum])

            listToCheck = low[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = "0{}".format(symbolsCode[symbIndex][1])

            listToCheck = lower[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = "1{}".format(symbolsCode[symbIndex][1])

        elif str(low[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(low[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append(["{}-{}".format(low[0], lower[0]), lowestSum])  # Append the new one
            symbolAndFrequency.append(["{}-{}".format(low[0], lower[0]), lowestSum])

            listToCheck = low[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = "0{}".format(symbolsCode[symbIndex][1])

            symbolsCode.append(["{}".format(lower[0]), "1"])

        elif str(lower[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(lower[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append(["{}-{}".format(low[0], lower[0]), lowestSum])  # Append the new one
            symbolAndFrequency.append(["{}-{}".format(low[0], lower[0]), lowestSum])

            listToCheck = lower[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = "1{}".format(symbolsCode[symbIndex][1])

            symbolsCode.append(["{}".format(low[0]), "0"])

        else:
            symbolsCode.append(["{}".format(low[0]), "0"])
            symbolsCode.append(["{}".format(lower[0]), "1"])
            TreeNodes.append(["{}-{}".format(low[0], lower[0]), lowestSum])
            symbolAndFrequency.append(["{}-{}".format(low[0], lower[0]), lowestSum])
        c += 1
    return symbolsCode


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


def returnTwoLowest(SymbolFreq):
    low, lower = SymbolFreq[-2], SymbolFreq[-1]
    symbolAndFrequency = SymbolFreq[:-2]
    return low, lower, symbolAndFrequency


def huffmanSendCodedData(imageMatrix, codesOfData):
    dataSent = list()  # This list shapes must be (300, 302) as our main image is
    CodesIndexes = [ind[0] for ind in codesOfData]

    for eachline in imageMatrix:
        tempList = list()
        for eachValue in eachline:
            index = CodesIndexes.index(str(eachValue))
            tempList.append(codesOfData[index][1])
        dataSent.append(tempList)
    return dataSent


def huffmanDecoding(codedDataReceived, codesOfData):
    dataReceived = list()
    ValuesIndexes = [ind[1] for ind in codesOfData]

    for eachLine in codedDataReceived:
        tempList = list()
        for eachValue in eachLine:
            index = ValuesIndexes.index(str(eachValue))
            tempList.append(int(codesOfData[index][0]))
        dataReceived.append(tempList)

    return showTheDecodedData(dataReceived)


def showTheDecodedData(dataToShow):
    # First we convert it to the array
    dataArray = array(dataToShow)
    matplotlib.pyplot.imshow(dataArray, cmap='gray')
    matplotlib.pyplot.imsave("Huffman Image.jpg", dataArray, cmap='gray')
    matplotlib.pyplot.show()


def sourceEntropy(frequencies):
    entropy = 0
    for f in frequencies:
        entropy += f * math.log2(f)
    return entropy * (-1)


def minimumAverageNumberOfBit(codes, probability):
    minimumBit = 0
    for f in probability:
        for t in codes:
            if t[0] == str(f[0]):
                nBit = len(t[1])
                break
        minimumBit += nBit * f[1]
    return minimumBit


if __name__ == '__main__':
    main()
