import sys
#generates standard vigenere encryption table
table = []
for i in range(26):
    o = ""
    for e in range(26):
        o += chr((i+e) % 26 + 65)
    table.append(o)
#
def encode():
    text = sys.argv[2].upper()
    key = sys.argv[3].upper()
    encryptedtext=""
    for i in range(len(text)):
        print(ord(text[i]) - 65)
        encryptedtext += table[ord(text[i % len(text)]) - 65][ord(key[i % len(key)])-65]
    return(encryptedtext)
#
def decode():
    encryptedtext = sys.argv[2].upper()
    key = sys.argv[3].upper()
    text = ''
    for i in range(len(encryptedtext)):
        text += chr(table[ord(key[i % len(key)])-65].index(encryptedtext[i % len(encryptedtext)]) + 65)
    return(text)
#
def returnimproperargs():
    print('improper arguments given, please make sure your arguments are \n \npython filename [encode/decode] [text/encryptedtext] [key] \n \n')
#make sure all arguments present
try:
    sys.argv[1]
    sys.argv[2]
    sys.argv[3]
except:
    returnimproperargs()
#run arguments
if sys.argv[1] == 'encode':
    print(encode())
elif sys.argv[1] == 'decode':
    print(decode())
else:
    returnimproperargs()
