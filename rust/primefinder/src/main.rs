use clap::Parser;
use once_cell::sync::Lazy;
use std::process::exit;

mod prime_finder;
use crate::prime_finder::PrimeFinder;

static mut PRIME_FINDER: Lazy<PrimeFinder> = Lazy::<PrimeFinder>::new(|| PrimeFinder::new());

/// A program that does things
#[derive(Parser, Debug)]
#[clap(version, about)]
struct Args {
    /// Minimum number of bytes
    #[clap(short)]
    limit: i32,
}

unsafe fn calc_primes(limit: i32) {
    for i in (3..limit).step_by(2) {
        let mut is_prime: bool = true;
        
        for j in PRIME_FINDER.primes.iter() {
            if *j as f32 > f32::sqrt(i as f32) {
                break;
            }
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime == true {
            PRIME_FINDER.primes.push(i);
        }
    }
}

fn main() {
    let limit: i32 = Args::parse().limit as i32;
    
    unsafe {
        PRIME_FINDER.set_capacity(limit);
    }

    // Start termination handler
    ctrlc::set_handler(move || {
        unsafe { 
            print!("{} - {}", PRIME_FINDER.num_cycles, PRIME_FINDER.primes.len());
            exit(1);
        }
    })
    .expect("Rust crashed! Failed to set termination handler!");


    unsafe {
        // Keep running while program hasn't recieved SIGINT
        loop {
            PRIME_FINDER.primes.clear();
            PRIME_FINDER.primes.push(2);
            calc_primes(limit);
            PRIME_FINDER.num_cycles += 1;
        }
    }
}