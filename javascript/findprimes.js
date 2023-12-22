function main() {
    process.argv.forEach(function (val, index, array) {
        upperbound = val
    })
    array_of_primes = getPrimes(upperbound);
}

function getPrimes(upperbound) {
    let array_of_primes = Array();
    array_of_primes.push(2)

    for (let i = 3; i < upperbound; i+=2) {
        let is_prime = true;
        let sqrtOfI = Math.sqrt(i)
        

        for (let j = 0; j < array_of_primes.length; j++) {
            let element = array_of_primes[j];

            if (element > sqrtOfI) {
                break;
            }
            if(i % element == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime == true) {
            array_of_primes.push(i);
        }
    }
}

main();