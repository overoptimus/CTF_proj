# coding=utf-8

from hashlib import md5

s = 'TASC?O3RJMV$WDJKX*ZM'
hash_part = 'E903'

for i in range(26):
    s1 = s.replace('?', chr(i + 65))
    for j in range(26):
        s2 = s1.replace('$', chr(j + 65))
        for k in range(26):
            # print i, j, k
            s3 = s2.replace('*', chr(k + 65))
            # print s3
            hash_var = md5(s3).hexdigest().upper()
            # print s
            if hash_var[:4] == 'E903':
                print hash_var
                break
