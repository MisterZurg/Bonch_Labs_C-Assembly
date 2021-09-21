#include <stdio.h>

long int recursive_factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * recursive_factorial(n - 1);
}

long int iterative_factorial(int n) {
    int ans = 1;
    for (int i = 1; i <= n; i++ ){
        ans *= i;
    } 
    return ans;
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    
    printf("Recursive Factorial of %d = %ld\n", n, recursive_factorial(n));
    printf("Interative Factorial of %d = %ld\n", n, iterative_factorial(n));
    
    return 0;
}