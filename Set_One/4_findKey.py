'''
Challenge 4
'''
from xor import *

file1 = open(r'C:\Users\duckc\Code\Crypto\Set_One\chal4_Data.txt', 'r')
lines = file1.readlines()
crypt = []
for l in lines:
    mess = findKey(l.strip())
    crypt.append(mess)

topScore = 0.0
broken = ""
for c in crypt:
    sc = score(c)
    if sc > topScore:
        topScore = sc
        broken = c

print(repr(broken))