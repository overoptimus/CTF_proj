pList = range(10000000, 100000000)
with open('zip_pw.txt', 'w') as f:
    for i in pList:
        f.write(str(i) + '\n')
