def makeArrayConsecutive2(statues):
    statues.sort()
    difference = 0
    count = 0
    count_list = 1
    while count_list < len(statues):
        if statues[count_list]-statues[count] > 1:
            difference = difference + statues[count_list]-statues[count]-1
        count = count + 1
        count_list = count_list + 1
    return difference
list = [6, 2, 3, 8]
print makeArrayConsecutive2(list)