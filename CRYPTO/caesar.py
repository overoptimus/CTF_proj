a = 'oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}'
b = 'cyberpeace'
# kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz
#
# for i in range(len(a)):
#     d = ord(a[i]) - ord(b[i])
#     print(d)

# print(ord('z'))

flag = ''

for i in a:
    if i == '_':
        flag += '_'
    elif i == '{':
        flag += '{'
    elif i == '}':
        flag += '}'
    else:
        d = ord(i) - 12
        if d < 97:
            d = ord(i) + 14
        flag += chr(d)


print(flag)
