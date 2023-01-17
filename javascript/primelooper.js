function main() {
    process.argv.forEach(function (val, index, array) {
        upperbound = val
    })

    let number_of_primes = getPrimes(upperbound);    
    let cycles = number_of_primes / 78498
    
    console.log("Javascript ran:", cycles, "cycles");
}

function getPrimes(time_limit) {
    let array_of_primes = Array();
    array_of_primes.push(2)
    let current_num = 3
    
    let start = new Date()
    let end = new Date()
    
    while ((end.getTime() - start.getTime()) < time_limit * 1000) {
    
        end = new Date()

        let is_prime = true;
        let sqrtOfI = Math.sqrt(current_num)
        
        for (let j = 0; j < array_of_primes.length; j++) {
            let element = array_of_primes[j];

            if (element > sqrtOfI) {
                break;
            }
            if(current_num % element == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime == true) {
            array_of_primes.push(current_num);
        }
        if (current_num >= 1000000) {
            current_num = 3;
        }
        else {
            current_num += 2;
        }
    }
    return array_of_primes.length
}

main();