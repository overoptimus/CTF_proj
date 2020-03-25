import re

text = ""

with open('/Users/optimus/CTF/CTYRPO/轮转机加密.txt', 'r') as f:
    text = f.read()

code = []

code = re.findall('<(.*)<', text)

# print(code)

for i in range(len(code)):
    code[i] = code[i].strip()

codetext = 'NFQKSEVOQOFNP'

codenum = '2,3,7,5,13,12,9,1,8,10,4,11,6'

codenum = codenum.split(',')

a = 0

for i in codenum:
    index = code[int(i) - 1].index(codetext[a])
    a += 1
    code[int(i) - 1] = code[int(i) - 1][index:] + code[int(i) - 1][:index]


for i in range(len(code[0])):
    str = ''
    print('第{}列为：'.format(i), end='')
    for j in codenum:
        str += code[int(j) - 1][i]
    print(str.lower())
