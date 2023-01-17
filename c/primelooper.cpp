#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>

int calc_primes(int time_limit) {
    // Vector for storing primes
    std::vector<int> primes = {2};
    int current_num = 3;

    time_t timestart = std::time(0);
    time_t timenow = time(0);    
    
    while ((timenow - timestart) < time_limit) {
        
        timenow = time(0);
        //auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

        bool is_prime = true;
        double sqrt_i = std::sqrt(current_num);
        
        for (int j = 0; j < primes.size(); j++) {
            if (primes.at(j) > sqrt_i) {
                break;
            }
            if (current_num % primes.at(j) == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime == true) {
            primes.push_back(current_num);
        }
        if (current_num >= 1000000) {
            current_num = 3;
        }
        else {
            current_num += 2;
        }
    }
    return primes.size();
}


int main(int argc, char **argv) {
    int time_limit = strtol(argv[1], nullptr, 0); // Convert first argument to integer
    
    int found_primes = calc_primes(time_limit);

    double cycles = found_primes / 78498;
    std::cout << "C++ ran: " << cycles << " cycles" << std::endl;

    return 0;
}