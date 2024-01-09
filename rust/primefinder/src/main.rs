use clap::Parser;
use std::process::exit;
use std::ptr;
use std::mem;
use std::alloc::{alloc, dealloc, handle_alloc_error, Layout};

/// A program that does things
#[derive(Parser, Debug)]
#[clap(version, about)]
struct Args {
    /// Minimum number of bytes
    #[clap(short)]
    limit: i32,
}

fn calc_primes(limit: i32, primes_vec: &mut Vec<i32>) {
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

unsafe fn on_exit(cycles_ptr: *const i32, primes_ptr: *const i32) {
    println!("{:?}, {:?}", *cycles_ptr, *primes_ptr);
    exit(1)     
}

fn main() {
    let limit: i32 = Args::parse().limit as i32;
    let mut cycles: i32 = 0;
    let length: usize = f32::sqrt(limit as f32) as usize;
    let mut primes: Vec<i32> = Vec::with_capacity(length);
    
    let mut primes_ptr: *const i32 = primes.as_ptr();
    let cycles_ptr: *const i32 = &cycles;

    // Start termination handler
    ctrlc::set_handler( move || {
        unsafe { on_exit(cycles_ptr, primes_ptr); }
    })
    .expect("Rust crashed! Failed to set termination handler!");

    loop {
        primes.push(2);
        calc_primes(limit, &mut primes);
        cycles += 1;
        primes.clear();
    }
}