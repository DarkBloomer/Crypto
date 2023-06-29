
import base64
from xor import *
'''
Input: two strings
Return: edit distance (int)
'''
def editDis(str1, str2):
    binStr1 = ''.join(format(ord(x), '08b') for x in str1)
    binStr2 = ''.join(format(ord(x), '08b') for x in str2)
    dis = sum(xi != yi for xi, yi in zip(binStr1, binStr2))
    return dis

'''
Input: 
Return:
'''
def convertToBin():
    bin = ""
    # open data file and read through lines
    file1 = open(r'C:\Users\duckc\Code\Crypto\Set_One\chal6_Data.txt', 'r')
    lines = file1.readlines()
    # convert data to a binary str 
    for l in lines:
        l = l.encode("ascii")
        decoded = base64.decodebytes(l)
        binLine = "".join(["{:08b}".format(x) for x in decoded])
        bin += binLine
    return bin
    
'''
Input: two strings 
Return: keysize 
'''
def findKeySize(binStr):
    key, flag = 0, 1.0
    # for each key size -> calculate edit distance
    # find smallest edit distance
    for i in range(2,41):
        KEYSIZE = 8 * i
        firstByte = binStr[0 : KEYSIZE]
        secondByte = binStr[(KEYSIZE + 1) : (KEYSIZE + 1) + KEYSIZE ]
        edit = editDis(firstByte, secondByte) / KEYSIZE
        if edit < flag: 
            flag = edit
            key = KEYSIZE
    return key

'''
Input: 
Return: 
'''
def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

'''
Input: binary string of ciphertext & keysize 
Return: blocks of size keysize
'''
def makeBlocks(bin, keySize):
    blocks = []
    blockStr = ""
    # create blocks
    flag = 0
    for b in range(0, len(bin) - 8, 8):
        # define byte of binary
        blockStr = bin[b:(b + 24)] 
        flag += 1
        # break block into byte size
        if flag == (keySize / 8):
            blockLst = split_str(blockStr, 8)
            blocks.append(blockLst)
            flag = 0
            blockStr = ""
    return blocks

'''
Input: binary string of ciphertext & keysize 
Return: blocks of size keysize
'''
def transpose(blocks):
    trans = []
    t1, t2, t3 = "", "", ""
    for b in blocks:
       t1 += b[0] 
       t2 += b[1]
       t3 += b[2]
    trans.append(t1)
    trans.append(t2)
    trans.append(t3)
    return trans

# BROKEN!!!
def searchForKey(trans):
    key = ""
    for x in trans:
        mes, k = findKey(x) 
        print(x)
        print(mes)
        key += k
    return key

'''
    Break Repeating-Key XOR Encryption
'''
def breakRepeatingXOR():
    # convert data to binary
    binary = convertToBin()
    # find key size
    key_size = findKeySize(binary)

    blocks = makeBlocks(binary, key_size)

    transposed = transpose(blocks)

    key = searchForKey(transposed)
    print(key)



breakRepeatingXOR()






