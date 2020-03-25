# coding=utf-8
from hashlib import md5

num = '101999966233'.encode()

print(md5(num).hexdigest())
