def is_number(a):
    try:
        float(a)
        return True
    except Exception as e:
        print(e)
        return False


def main():
    s = 'synt{5pq1004q-86n5-46q8-o720-oro5on0417r1}'
    p = ''
    for i in s:
        if i == '{' or i == '}' or i == '-' or is_number(i):
            p += i
        elif i <= 'z' and i >= 'a':
            i = chr(ord(i) - 13)
            if i < 'a':
                i = chr(ord('z') - (ord('a') - ord(i)) + 1)
            p += i
        elif i <= 'Z' and i >= 'A':
            i = chr(ord(i) - 13)
            if i < 'A':
                i = chr(ord('Z') - (ord('A') - ord(i)) + 1)
            p += i

    print(p)


if __name__ == '__main__':
    main()
