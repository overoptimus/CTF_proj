# coding=utf-8
import binascii

with open('111.txt', 'rb') as f1, open('111.png', 'wb') as f2:
    text = f1.read()
    # img = binascii.a2b_hex(text)
    print(text.decode().strip('\n'))
    f2.write(text)
