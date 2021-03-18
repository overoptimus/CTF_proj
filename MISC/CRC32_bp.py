from zlib import crc32
import random

char = '0123456789'
crc32_ = 'F678BB78'


def crc32_f(data):
    return hex(crc32(data) & 0xFFFFFFFF)[2:10]


while True:
    text = ''
    for i in range(8):
        text += char[random.randint(0, len(char) - 1)]
    if crc32_f(text.encode()) == crc32_:
        print(text)
        exit()
    else:
        print('not success!')
