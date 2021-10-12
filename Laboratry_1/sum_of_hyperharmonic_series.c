#include <stdio.h>

float sumHyperharmonicSereies(int n){
    float result = 0;
    for (int i = 1; i < n + 1; i++) {
        result += 1 / (float) (i * i);
    }
    printf("%f\n", result);
    return result;
}


int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    
    printf("Sum of the Series  %d = %f\n", n, sumHyperharmonicSereies(n));    
    return 0;
}