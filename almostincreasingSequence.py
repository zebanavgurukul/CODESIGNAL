def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    while elm < len(sequence):
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True
list = [1,3,2]
print almostIncreasingSequence(list)