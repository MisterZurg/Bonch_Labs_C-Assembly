; call_perl calls perl interpreter
global _start

_start              ; Data for code
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    push ax
    push 6c726570h
    push 2f6e6962h
    push 2f727375h
    push 2f2f2f2fh

    mov ebx, esp
    mov al, 0bh

    int 80h