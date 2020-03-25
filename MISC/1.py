# coding=utf-8

s = ''
with open('密文.txt', 'rb') as m, open('key.txt', 'rb') as k:
    m_txt = m.read()
    k_txt = k.read()
    print m_txt, k_txt
    zipper = zip(m_txt, k_txt)
    print zipper
    for i, j in zipper:
        s += chr(ord(i) ^ ord(j))
print s
