#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <cstdlib>

void findprimes(int limit) {
    // Vector for storing primes
    std::vector<int> primes = {2};

    for (int i=2; i<limit; i++) {
        bool is_prime = true;
        double sqrt_i = std::sqrt(i);
        int size = primes.size();
        for (int j=0; j < size; j++) {
            if (primes.at(j) > sqrt_i) {
                break;
            }
            if (i % primes.at(j) == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime == true) {
            primes[size + 1] = i;
        }
    }
}

int main(int argc, char **argv) {
    int limit = strtol(argv[1], nullptr, 0); // Convert first argument to integer
    auto start = std::chrono::high_resolution_clock::now();
    
    findprimes(limit);

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "C++ execution time: " << duration.count() << "ms" << std::endl;

    return 0;
}