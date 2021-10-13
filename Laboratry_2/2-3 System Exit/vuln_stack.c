//
// Created by imenb on 10/12/2021.
//

# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void foo(char *message) {
     char buf[100];
     printf("addr buf: %p\n", buf);
     printf("addr &message: %p\n", &message);
     strcpy(buf, message);
     printf("buf: %s\n", buf);
}

int main(int argc, char *argv[]) {
     if (argc != 2) {
         exit(1);
     }

     foo(argv[1]);

     return 0;
}