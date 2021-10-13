//
// Created by imenb on 10/13/2021.
//

// environment_variable_pointer finds the address of the environment variable.
# include <stdio.h>
# include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("Addres: %s: %p\n", argv[1], getenv(argv[1]));
    printf("%s = %s\n", argv[1], getenv(argv[1]));
    
    return 0;
}