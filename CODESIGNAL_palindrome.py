def checkPalindrome(inputString):
    j = -1
    i = 0
    while i < len(inputString):
        if inputString[i] == inputString[j]:
            sto = True
        else:
            return False
        i = i + 1
        j =  j - 1
    return sto
var = "aaabaaaa"
print checkPalindrome(var)
