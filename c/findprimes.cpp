#include <cmath>
#include <cstdlib>
#include <iostream>
#include <signal.h>
#include <vector>

std::vector<int> primes;
int cycles;

void findprimes(int limit, std::vector<int> &primes) {
  primes.push_back(2);

  for (int i = 3; i < limit; i += 2) {
    bool is_prime = true;
    double sqrt_i = std::sqrt(i);

    for (int prime : primes) {
      if (prime > sqrt_i) {
        break;
      }
      if (i % prime == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime == true) {
      primes.push_back(i);
    }
  }
}

void siginthandler(int param) {
  std::cout << cycles << " - " << primes.size();
  exit(1);
}

int main(int argc, char **argv) {
  int limit = strtol(argv[1], nullptr, 0); // Convert first argument to integer

  signal(SIGINT, siginthandler);

  while (true) {
    primes.clear();
    findprimes(limit, primes);
    cycles += 1;
  }

  return 0;
}
