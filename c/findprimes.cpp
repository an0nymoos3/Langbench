#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <cstdlib>

void findprimes(int limit) {
    // Array for storing primes
    std::vector<int> primes;
    primes.push_back(2);

    for (int i = 3; i < limit; i += 2) {
        bool is_prime = true;
        double sqrt_i = std::sqrt(i);

        for (int prime: primes) {
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

int main(int argc, char **argv) {
    int limit = strtol(argv[1], nullptr, 0); // Convert first argument to integer
    findprimes(limit);

    return 0;
}