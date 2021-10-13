//
// Created by imenb on 10/13/2021.
//

// vuln_heap is vulnerable to buffer overflow 
// in the memory area as a heap
# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void ptr(char *message){
    printf("message: %s\n", message);
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        exit(1);
    }

    char *buf = calloc(100, sizeof(char));
    unsigned long *f = malloc(4);
    *f = (unsigned long) ptr;

    printf("Buffer addres: %p\n", buf);
    printf("f addres: %p\n", f);

    strcpy(buf, argv[1]);
    ((void (*)(char*)) (*f))(buf);

    free(f);
    free(buf);
    
    return 0;
}