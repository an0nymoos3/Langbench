use std::time::{Instant};
use clap::Parser;

/// A program that does things
#[derive(Parser, Debug)]
#[clap(version, about)]
struct Args {
    /// Minimum number of bytes
    #[clap(short)]
    limit: i32,
}

fn calc_primes(limit: i32) {
    let mut primes: Vec<i32> = Vec::new();
    primes.push(2);

    for i in 3..limit {
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
        if is_prime == true {
            primes.push(i);
        }
    }
}

fn main() {
    let args = Args::parse();
    let limit = args.limit as i32;
    
    let start = Instant::now();

    calc_primes(limit);
    
    let elapsed_time = start.elapsed().as_millis();

    println!("Rust exection time: {}ms", elapsed_time);
}