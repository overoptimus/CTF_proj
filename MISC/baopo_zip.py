import zipfile
import os


def extractFile(zFile, password):
    try:
        zFile.extractall(path=os.getcwd(), pwd=password)
    except Exception as e:
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
