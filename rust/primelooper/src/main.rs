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

fn calc_primes(time_limit: u128) -> usize{
    let mut primes: Vec<i32> = Vec::new();
    primes.push(2);

    let mut current_num: i32 = 3;

    let start: Instant = Instant::now();
    let mut elapsed_time = start.elapsed().as_millis();

    while elapsed_time < time_limit {

        elapsed_time = start.elapsed().as_millis();
        
        let mut is_prime: bool = true;
        let sqrt_num: f64 = f64::sqrt(current_num as f64);
        
        for j in primes.iter() {
            if *j as f64 >  sqrt_num{
                break;
            }
            if current_num % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime == true {
            primes.push(current_num);
        }

        if current_num >= 1000000 {
            current_num = 3
        }
        else {
            current_num += 2;
        }
    }
    return primes.len()
}

fn main() {
    let args: Args = Args::parse();
    let time_limit: u128 = (args.limit * 1000) as u128;

    let primes_found: usize = calc_primes(time_limit);

    let cycles: f64 = primes_found as f64 / 78498.0;
    println!("Rust ran: {} cycle(s)", cycles);
}
