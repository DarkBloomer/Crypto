
"""Convert Hex string to Base64"""
import base64

HEX_STRING = '746865206b696420646f6e277420706c6179'

BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
print(BYTE_ARRAY)
BASE64_VAL = base64.b64encode(BYTE_ARRAY)
print(BASE64_VAL)
