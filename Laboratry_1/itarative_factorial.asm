; itarative_factorial implements algorithm 
; for itarative calculation factorial of n
%include "print.inc"
global _start

section .data               ; Data for code
    NUMBER equ 6
    EXIT_CODE equ 1
    RET_VAL equ 0

section .text               ; Program body
fac:
    mov eax, ebx
    cmp eax, 1
    je fac_lab1
    mov ecx, eax
    xor eax, eax
    mov al, 1

fac_lab2:
    cmp ecx, 1
    jbe fac_lab3
    mul ecx
    sub ecx, 1
    jmp fac_lab2

fac_lab1:
    mov eax, 1

fac_lab3:
    ret

_start:                     ; func main()
    mov ebx, NUMBER
    cmp ebx, 0
    jl lab1
    call fac
    call print_number
    mov eax, 10
    call print_symbol

lab1:
    mov eax, EXIT_CODE
    mov ebx, RET_VAL
    int 0x80
