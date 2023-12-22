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
    let mut primes: Vec<i32> = vec![2];
 
    for i in (3..limit).step_by(2) {
        let mut is_prime: bool = true;
        let sqrt_i: f32 = f32::sqrt(i as f32);
        
        for j in primes.iter() {
            if *j as f32 >  sqrt_i{
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
    let limit: i32 = Args::parse().limit as i32;

    calc_primes(limit);
}