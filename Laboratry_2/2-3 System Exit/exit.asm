; exit calls for system exit
section .text
global _start

_start:
    xor eax, eax
    xor ebx, ebx
    
    mov al, 1h
    int 80h