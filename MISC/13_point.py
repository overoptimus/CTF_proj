def is_number(a):
    try:
        float(a)
        return True
    except Exception as e:
        return False


def main():
    s = 'synt{mur_VF_syn9_svtug1at}'
    p = ''
    for i in s:
        if i == '{' or i == '}' or i == '_' or is_number(i):
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
