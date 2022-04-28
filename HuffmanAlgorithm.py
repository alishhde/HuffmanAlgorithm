# Seyyedali Shohadaalhosseini
from itertools import chain
import matplotlib.image as mpimg


def mainFunc():
    pixels_flattened, img_pixels_matrix = Read_input()
    symbols, frequencies = calculateThePixelsAndFrequency(pixels_flattened, img_pixels_matrix)
    symbolAndFrequency = connectSymbolsToFrequencies(symbols, frequencies)

    symbolsCode = list()
    TreeNodes = list()
    rootNodes = list()

    # This must go to the loop
    c = 0
    while len(symbolAndFrequency) > 1:
        SortedSymbolFreq = sortTheDataBy(symbolAndFrequency)
        low, lower, symbolAndFrequency = returnTwoLowest(SortedSymbolFreq)
        lowestSum = low[1] + lower[1]
        # print(low, lower)

        if len(TreeNodes) > 0:
            rootNodes = [val[0] for val in TreeNodes]

        # print("This is root", TreeNodes)
        if str(low[0]) in rootNodes and str(lower[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(low[0]):
                    del TreeNodes[index_Counter]
                elif val[0] == str(lower[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append([f"{low[0]}-{lower[0]}", lowestSum])  # Append the new one
            symbolAndFrequency.append([f"{low[0]}-{lower[0]}", lowestSum])

            listToCheck = low[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                # Find the symb
                # add the 0 to it
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = f"0{symbolsCode[symbIndex][1]}"

            listToCheck = lower[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                # Find the symb
                # add the 1 to it
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = f"1{symbolsCode[symbIndex][1]}"
            # print("Broke Here 1")
            # break

        elif str(low[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(low[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append([f"{low[0]}-{lower[0]}", lowestSum])  # Append the new one
            symbolAndFrequency.append([f"{low[0]}-{lower[0]}", lowestSum])

            # print(low[0])
            # print(type(low[0]))
            # print(len(low[0]))
            # print(listToCheck)
            # print(type(listToCheck))
            # print(symbolsCode)
            # print(symbolsIn_symbolsCode)
            listToCheck = low[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                # print(symb)
                # print(type(symb))
                # print(len(symb))

                # Find the symb
                # add the 0 to it
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = f"0{symbolsCode[symbIndex][1]}"

            symbolsCode.append([f"{lower[0]}", "1"])

            # print("Broke Here 2")
            # break
        elif str(lower[0]) in rootNodes:
            #  deleting the repeated node to replace with new one
            index_Counter = 0
            for val in TreeNodes:
                if val[0] == str(lower[0]):
                    del TreeNodes[index_Counter]
                index_Counter += 1
            TreeNodes.append([f"{low[0]}-{lower[0]}", lowestSum])  # Append the new one
            symbolAndFrequency.append([f"{low[0]}-{lower[0]}", lowestSum])

            listToCheck = lower[0].split("-")
            symbolsIn_symbolsCode = [s[0] for s in symbolsCode]
            for symb in listToCheck:
                # Find the symb
                # add the 0 to it
                symbIndex = symbolsIn_symbolsCode.index(symb)
                symbolsCode[symbIndex][1] = f"1{symbolsCode[symbIndex][1]}"

            symbolsCode.append([f"{low[0]}", "0"])

            # print("Broke Here 3")
            # break
        else:
            symbolsCode.append([f"{low[0]}", "0"])
            symbolsCode.append([f"{lower[0]}", "1"])
            TreeNodes.append([f"{low[0]}-{lower[0]}", lowestSum])
            symbolAndFrequency.append([f"{low[0]}-{lower[0]}", lowestSum])
        c += 1

    print("This is loop Counter: ", c)
    # print("This is Sorted Symbol, Freq: {}\n".format(SortedSymbolFreq))
    print("This is TreeNodes length: {}".format(len(TreeNodes)))
    print("This is TreeNodes", end="")
    c = 0
    for i in TreeNodes:
        if c % 1 == 0:
            print()
        print(i, end=" ")
        c += 1

    print("\n\nThis is SymbolCode length: {}".format(len(symbolsCode)), end="")
    print("\n\nThis is SymbolCode", end="")
    c = 0
    for i in symbolsCode:
        if c % 9 == 0:
            print()
        print(i, end=" ")
        c += 1

    # print(SortedSymbolFreq)
    # print("\n\n", symbolAndFrequency)


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


def returnTwoLowest(SymbolFreq):
    low, lower = SymbolFreq[-2], SymbolFreq[-1]
    symbolAndFrequency = SymbolFreq[:-2]
    return low, lower, symbolAndFrequency


mainFunc()
