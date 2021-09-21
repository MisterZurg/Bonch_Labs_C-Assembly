; print non-negative number
section .bss
    s: resb 1

section .data
    WRITE_CODE equ 4
    STDOUT equ 1

section .text
; input argument: eax - printed symbol
print_symbol:
    mov [s], al
    mov eax, WRITE_CODE
    mov ebx, STDOUT
    mov ecx, s
    mov edx, 1
    int 0x80
    ret
; input argument: eax - printed symbol
print_number:
    cmp eax, 0
    jne plab1
    mov al, '0'
    call print_symbol
    jmp plab4
plab1:
    mov ebx, 10
    xor ecx, ecx
plab2:
    inc ecx
    xor edx, edx
    div ebx
    push edx
    cmp eax, 0
    jnz plab2
plab3:
    pop eax
    push ecx ; save ecx for loop
    add eax, '0'
    call print_symbol
    pop ecx ; restore ecx
    loop plab3
plab4:
    ret
