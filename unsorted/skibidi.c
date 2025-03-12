#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to generate all prime numbers up to n using the Sieve of Eratosthenes
void generatePrimes(int n, int** primes, int* primeCount) {
    bool* isPrime = (bool*)malloc((n + 1) * sizeof(bool));
    *primes = (int*)malloc((n + 1) * sizeof(int));
    
    for (int i = 0; i <= n; i++) {
        isPrime[i] = true;
    }
    
    isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime numbers

    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            (*primes)[(*primeCount)++] = i; // Store the prime number
            for (int j = 2 * i; j <= n; j += i) {
                isPrime[j] = false; // Mark as non-prime
            }
        }
    }

    free(isPrime);
}

// Recursive function to find sphenic numbers
void findSphenicNumbers(int* primes, int primeCount, int start, int product, int count,int n) {
    if (count == 3 && product <= n) { // If we have selected 3 distinct primes
        printf("%d ", product); // Print the sphenic number
        return;
    }

    for (int i = start; i < primeCount; i++) {
        // Recursively select primes and calculate product
        findSphenicNumbers(primes, primeCount, i + 1, product * primes[i], count + 1,n) ;
    }
}

int main() {
    int n;

    printf("Enter a natural number n: ");
    scanf("%d", &n);

    int* primes = NULL;
    int primeCount = 0;

    // Generate primes up to n
    generatePrimes(n, &primes, &primeCount);

    printf("Sphenic numbers from 1 to %d are: ", n);
    findSphenicNumbers(primes, primeCount, 0, 1, 0, n);
    printf("\n");

    free(primes); // Free allocated memory
    return 0;
}