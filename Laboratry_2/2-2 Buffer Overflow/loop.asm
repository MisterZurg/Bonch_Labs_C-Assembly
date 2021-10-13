; loop creates infinity loop
section .text
global _start

_start:
    xor eax, eax
    cmp eax, 0x1
    jne _start
