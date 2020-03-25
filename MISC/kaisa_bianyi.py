s = 'afZ_r9VYfScOeO_UL^RWUc'

t = 5
m = ''


# def main():
#     for i in s:
#         print(i + "->" + str(ord(i)))
#     for i in m:
#         print(i + "->" + str(ord(i)))
def main():
    global t
    for i in s:
        print(chr(ord(i) + t), end='')
        t += 1
    print(m)


if __name__ == '__main__':
    main()


# 97   102   90   95
# 5    6     7    8
# 102  108   97   103
