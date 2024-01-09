use clap::Parser;
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, Ordering};

/// A program that does things
#[derive(Parser, Debug)]
#[clap(version, about)]
struct Args {
    /// Minimum number of bytes
    #[clap(short)]
    limit: i32,
}

fn calc_primes(limit: i32, primes_vec: &mut Vec<i32>, is_running: &Arc<AtomicBool>) {
    if is_running.load(Ordering::SeqCst) == false {
        return // Return if running is false
    }

    for i in (3..limit).step_by(2) {
        let mut is_prime: bool = true;
        
        for j in primes_vec.iter() {
            if *j as f32 > f32::sqrt(i as f32) {
                break;
            }
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime == true {
            primes_vec.push(i);
        }
    }
}

fn main() {
    let running: Arc<AtomicBool> = Arc::new(AtomicBool::new(true));
    let running_ctrlc: Arc<AtomicBool> = running.clone();

    let limit: i32 = Args::parse().limit as i32;
    let length: usize = f32::sqrt(limit as f32) as usize;
    let mut primes: Vec<i32> = Vec::with_capacity(length);

    let mut cycles: i32 = 0;
    
    // Start termination handler
    ctrlc::set_handler(move || {
        running_ctrlc.store(false, Ordering::SeqCst); // Change running to false
    })
    .expect("Rust crashed! Failed to set termination handler!");

    // Keep running while program hasn't recieved SIGINT
    while running.load(Ordering::SeqCst) {
        primes.clear();
        primes.push(2);
        calc_primes(limit, &mut primes, &running);
        cycles += 1;
    }
    cycles -= 1; // Remove the unfinished cycle

    println!("{cycles} - {len}", len = primes.len()); // Print number of cycles and length of current array
}