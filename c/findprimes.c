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

  for (int i = 3; i < limit; i += 2) {
    int inner_limit = (int)sqrt(i);
    bool is_prime = true;

    int j = 0;
    for (int prime = primes[j]; j < primes_len; j++) {
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
  printf("%d - %d", num_cycles, primes_len);
  exit(1);
}

int main(int argc, char **argv) {
  int array_size =
      (int)*argv[1] /
      2; // Worst case estimate for number of primes. Assume argv[1] is large
         // enough that this wont ever fail, like with limit = 3

  printf("ARRAY_SIZE: %d", array_size);
  int prime_arr[array_size];
  primes = prime_arr;

  signal(SIGINT, (__sighandler_t)siginthandler);

  while (true) {
    findprimes(*argv[1]);
    // printf("PRIMES: %d\n", primes_len);
  }

  return 0;
}
