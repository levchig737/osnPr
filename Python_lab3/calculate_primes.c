void calculate_primes(int prime[], int n)
{
    /* Заменим 1 на 0 */
    prime[1] = 0;

    for (int i = 2; i < n; i++)
        prime[i] = 1;
    
    /* Алгоритм */
    for (int i=2; i<=n; i++)
    {
	if (prime[i] != 0)
	    {
	        for (int j=i*2; j<=n; j+=i)
	        prime[j] = 0;
	    prime[i] = 1;
	    }
    }
}
