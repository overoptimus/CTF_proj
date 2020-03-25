import base64

text = ''
with open('./base64.txt', 'r') as f:
    text = f.read()

text = text.split('\n')
# print(text)
with open('decode_text.txt', 'w') as f:
    for i in text:
        decodetext = base64.b64decode(i)
        f.write(decodetext)
