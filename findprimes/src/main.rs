use std::time::{Instant};


fn calc_primes() {
    // Create a vector with the lowest prime number
    let mut primes: Vec<i32> = vec![2];

    for i in 2..10000000 {
        let mut is_prime: bool = true;
        let sqrt_i = f64::sqrt(i as f64);
        
        for j in primes.iter() {
            if *j as f64 >  sqrt_i{
                break;
            }
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(i)
        }
    }
}

fn main() {
    let start = Instant::now();
    
    calc_primes();
    
    let elapsed_time = start.elapsed().as_millis();

    println!("Rust exection time: {}ms", elapsed_time);
}
