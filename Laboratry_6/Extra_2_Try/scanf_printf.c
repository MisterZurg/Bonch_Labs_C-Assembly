//
// Created by MZ on 10/13/2021.
//

# include <stdio.h>

void foo() {
    char buf[100];
    scanf("%s", buf);
    printf("buf: '%s '\n", buf);
}


int main (int argc, char *argv[]) {
    foo();
    return 0;
}