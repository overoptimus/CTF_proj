'''
@Description: 
@Version: 2.0
@Author: 0pt1mus
@Date: 2020-02-18 11:55:04
@LastEditors: 0pt1mus
@LastEditTime: 2020-04-26 12:06:42
'''
import os
import zipfile


def extractFile(zFile, password):
    try:
        zFile.extractall(path=os.getcwd(), pwd=password)
    except Exception:
        return False
    else:
        return True


def main():
    zFile = zipfile.ZipFile('./1.zip')
    passFile = input('password file:')
    with open(passFile, 'r') as passf:
        for password in passf.readlines():
            password = password.strip()
            result = extractFile(zFile, password)
            if result:
                print('success:', result)
                break


if __name__ == '__main__':
    main()
