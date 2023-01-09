def neighbors(array,rowIndex,colIndex):
    if rowIndex == 0 and colIndex == 0:
        return array[rowIndex][1] + array[rowIndex + 1][0] + array[rowIndex + 1][1]
    elif rowIndex == 0 and colIndex == len(array[0]) - 1:
        return array[rowIndex][colIndex - 1] + array[rowIndex - 1][colIndex - 1] + array[rowIndex + 1][colIndex]
    elif rowIndex == len(array) - 1 and colIndex == 0:
        return array[rowIndex - 1][colIndex] + array[rowIndex - 1][1] + array[rowIndex][1]
    elif rowIndex == len(array) - 1 and colIndex == len(array[0]) - 1:
        return array[rowIndex - 1][colIndex - 1] + array[rowIndex - 1][colIndex] + array[rowIndex][colIndex - 1]
    elif rowIndex == 0:
        return array[rowIndex][colIndex -1] + array[rowIndex][colIndex + 1] + array[rowIndex + 1][colIndex - 1] + \
            array[rowIndex + 1][colIndex] + array[rowIndex + 1][colIndex + 1]
    elif colIndex == 0:
        return array[rowIndex - 1][colIndex] + array[rowIndex - 1][colIndex + 1] + array[rowIndex][colIndex + 1] + \
            array[rowIndex + 1][colIndex] + array[rowIndex + 1][colIndex + 1]
    elif colIndex == len(array[0]) - 1:
        return array[rowIndex - 1][colIndex - 1] + array[rowIndex - 1][colIndex] + array[rowIndex][colIndex - 1] + \
            array[rowIndex + 1][colIndex - 1] + array[rowIndex + 1][colIndex]
    elif rowIndex == len(array) - 1:
        return array[rowIndex - 1][colIndex - 1] + array[rowIndex - 1][colIndex] + array[rowIndex - 1][colIndex + 1] + \
            array[rowIndex][colIndex - 1] + array[rowIndex][colIndex + 1]
    else:
        return array[rowIndex - 1][colIndex - 1] + array[rowIndex - 1][colIndex] + array[rowIndex - 1][colIndex + 1] + \
            array[rowIndex][colIndex - 1] + array[rowIndex][colIndex + 1] + array[rowIndex + 1][colIndex -1] + \
            array[rowIndex + 1][colIndex] + array[rowIndex + 1][colIndex + 1]
 

    


 




array = [ [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 1] ]
bigArray = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1]
]
print(neighbors(bigArray,4,1))