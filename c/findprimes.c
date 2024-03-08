#include <math.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int num_cycles;
int *primes;
int primes_len = 1;

void findprimes(int limit) {
  primes_len = 1;
  primes[0] = 2;

  for (int i = 3; i <= limit; i += 2) {
    int inner_limit = (int)sqrt(i) + 1;
    bool is_prime = true;

    int j = 0;
    int prime;
    for (prime = primes[j]; j < primes_len; j++) {
      if (prime > inner_limit) {
        break;
      }

      if (i % prime == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      primes[primes_len] = i;
      primes_len += 1;
    }
  }

  num_cycles += 1;
}

void siginthandler() {
  printf("%d - %d\n", num_cycles, primes_len);
  exit(1);
}

int main(int argc, char **argv) {
  int array_size =
      atoi(argv[1]) / 2 + 1; // Worst case estimate for number of primes.

  int prime_arr[array_size];
  primes = prime_arr;

  signal(SIGINT, (__sighandler_t)siginthandler);

  while (true) {
    findprimes(atoi(argv[1]));
  }

  return 0;
}
