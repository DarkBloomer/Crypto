'''
Input: two strings
Return: edit distance (int)
'''
def editDis(str1, str2):
    binStr1 = ''.join(format(ord(x), '08b') for x in str1)
    binStr2 = ''.join(format(ord(x), '08b') for x in str2)
    dis = sum(xi != yi for xi, yi in zip(binStr1, binStr2))
    return dis

