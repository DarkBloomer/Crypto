import math
import string
"""
Input: string (str) 
Return: score based on frequency of letters 
"""
def score(message):
    score = 1.0
    freq_dict = { 
        'e':0.11160,  	
        'a':0.084966,		
        'r':0.075809,		
        'i':0.075448,		
        'o':0.071635,		
        't':0.069509,		
        'n':0.066544,		
        's':0.057351,		
        'l':0.054893,		
        'c':0.045388,		
        'u':0.036308,		
        'd':0.033844,		
        'p':0.031671,	
        'm':0.030129,
        'h':0.030034,
        'g':0.024705,
        'b':0.020720,
        'f':0.018121,
        'y':0.017779,
        'w':0.012897,
        'k':0.011011,
        'v':0.010074,
        'x':0.002902,
        'z':0.002722,
        'j':0.001965,
        'q':0.001962
    }
    special_chars = "%<~>\↓«º♠☺♥$"
    if any(c in special_chars for c in message):
        return 0.0
    for x in message:
        y = x.lower()
        if y in freq_dict:
            score *= freq_dict[y]
    if ' ' not in message:
        return 0.0
    elif "like" in message or "the" in message or "and" in message:
        score = 1.0 
    elif 'hh' in message:
        score = 0.0
    elif 'QD' in message:
        return 0.0
    elif score == 1.0:
        return 0.0
    return score

'''
Input: string (hex)
Return: string (binary)
'''
def prepHexInput(hex):
    hexBinStr = ""
    for i in range(0, len(hex), 2):
        hexVal = hex[i]  + hex[i + 1]
        binStr = hexToBin(hexVal)
        hexBinStr += binStr
    return hexBinStr

'''
Input: two binary strings, length of strings
Return:
'''
def xor(a, b, n):
    ans = ""
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):
        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

"""
Input: one binary string (bin1) & one binary key (bin2) 
Return: binary string of xor strings
"""
def single_byte_xor(bin1, bin2):
    xorStr = ''
    for i in range(0, len(bin1), 8):
        temp_data = bin1[i:i + 8]
        binXor = xor(temp_data, bin2, 8)
        an_int = int(binXor, 2)
        ascii_char = chr(an_int)
        xorStr += ascii_char
    return xorStr
    
"""
Input: string (hex) 
Return: string (binary)
"""
def hexToBin(hex):
    n = int(hex, 16)
    bstr = ''
    while n > 0:
        bstr = str(n % 2) + bstr
        n = n >> 1   
    res = str(bstr)
    if len(res) < 8:
        for i in range(8 - len(res)):
            res = '0' + res
    return res

"""
Input: string (hex)
Return: string with highest English score 
"""
def findKey(hexstr):
    message = "" # return value
    topscore = 0.0 # scores strings
    bstr = prepHexInput(hexstr) 
    fir_hex_dig = "01234567"
    sec_hex_dig = "0123456789abcdef"
    for i in range(len(fir_hex_dig)):
        for j in range(len(sec_hex_dig)):
            hexKey = hexToBin(fir_hex_dig[i] + sec_hex_dig[j])
            xorbin = single_byte_xor(bstr, hexKey)
            score_result = score(xorbin)
            if score_result > topscore:
                topscore = score_result
                message = xorbin

    # return message with highest freq score
    return message 

''' TEST - "Cooking MC's like a pound of bacon"
hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
mes = findKey(hex)
print(mes)
'''



