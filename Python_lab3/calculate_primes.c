#include<stdio.h>
void calculate_primes(int numbers[], int n)
{
    /* Заменим 1 на 0 */
    numbers[1] = 0;

    /* Алгоритм */
    for (int i=2; i<=n; i++)
    {
	    if (numbers[i] != 0)
	    {
	        for (int j=i*2; j<=n; j+=i)
	        numbers[j] = 0;
	    numbers[i] = 1;
	    }
    }
}


int main() {
    int prime[100];
    int n = 100;
    calculate_primes(prime, 100);
    for (int i = 0; i < 100; i++) {
        printf("%d %d\n", i, prime[i]);
    }
}
