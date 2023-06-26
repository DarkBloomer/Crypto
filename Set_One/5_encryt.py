'''
Challenge 5
'''
from xor import *

"""
Input: string & encryption key 
Return: string encrypted (hex)
"""
def xorEncrypt(str1, key):
    enc1 = ""
    cnt = 0
    for x in str1:
        # convert string letter to binary
        bin1 = hexToBin(x.encode('utf-8').hex())
        print(bin1)
        # convert key char to binary
        binKey = hexToBin(key[cnt].encode('utf-8').hex())
        print(binKey)
        # XOR on binary string and key
        result = xor(bin1, binKey, len(bin1)) 
        # add XOR string to enc1
        enc1 += result
        cnt += 1
        if cnt == 3:
            cnt =0
    # convert binary string to hex
    encStr = '%0*X' % ((len(enc1) + 3) // 4, int(enc1, 2)) 
    # return string (hex)
    return encStr 

inStr2 = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

encrypt2 = xorEncrypt(inStr2, key)

print(" ")
print(encrypt2)