import base64

hex_string2 = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_string2 = bytes.fromhex(hex_string2)
print(base64.b64encode(bytes_string2))
