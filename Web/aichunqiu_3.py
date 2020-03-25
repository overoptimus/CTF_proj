import requests
url = 'http://1039ac48efb947dcb8997880eac874548537b73b97f24c8a.changame.ichunqiu.com/?value[]=ea'

s = requests.session()
r = s.get(url)
with open('1.txt', 'w') as f:
    for i in range(20):
        url = 'http://1039ac48efb947dcb8997880eac874548537b73b97f24c8a.changame.ichunqiu.com/?value[]=' + \
            str(r.text[0:2])
        r = s.get(url)
        f.write(r.text)
        # print(r.text)
