#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    const int nsec = 5;

    while (1) {
        printf("%d: I'm alive and now I want to sleep for %d sec\n", getpid(), nsec);
        sleep (nsec);
    }

    return 0;
}