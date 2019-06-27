def adjacentElementsProduct(inputArray):
    max = None
    i = 0
    j = 1
    while i < len(inputArray)-1:
        var = inputArray[i]*inputArray[j]
        if max < var:
            max = var
        i = i + 1
        j = j + 1
    return max
list_1 = [3,6,-2,-5,7,3]
print adjacentElementsProduct(list_1) 
