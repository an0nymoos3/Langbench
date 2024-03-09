use std::env;
use std::process::exit;

#[derive(Clone, Copy)]
struct HoldsRawPtr {
    num_cycles: *mut i32,
    primes: *mut Vec<i32>,
}

// By implementing the Send trait, we tell compiler that this type can be transferred between
// threads without violating safety. Whether it actually is safe is our responsibility
unsafe impl Send for HoldsRawPtr {}
// Sync trait tells compiler that `&T` is safe to share between threads
unsafe impl Sync for HoldsRawPtr {}

unsafe fn find_primes(limit: i32, raw_ptrs: &HoldsRawPtr) {
    (*raw_ptrs.primes).set_len(1); // Set length back to one (vec = [2]), without having to reset
                                   // all elements.

    for i in (3..limit).step_by(2) {
        // Look for all primes
        let mut is_prime: bool = true;
        let inner_limit: f32 = f32::sqrt(i as f32);

        // Only check against known primes
        for prime in (*raw_ptrs.primes).iter() {
            // Any number larger that sqrt(i) cannot divide i
            // evenly.
            if *prime as f32 > inner_limit {
                break;
            }

            // If remainder is 0, i is not prime
            if i % prime == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            (*raw_ptrs.primes).push(i);
        }
    }

    // Increase number of cycles successfully run
    *raw_ptrs.num_cycles += 1;
}

fn main() {
    // Get command line args
    let args: Vec<String> = env::args().collect::<Vec<String>>();
    let limit: i32;

    // Skip out of bounds check
    #[allow(unused_unsafe)]
    unsafe {
        limit = args.get_unchecked(1).parse::<i32>().unwrap();
    }

    // Prepare datastructures needed
    let mut primes: Vec<i32> = vec![2];
    let raw_ptrs: HoldsRawPtr = HoldsRawPtr {
        num_cycles: &mut 0,
        primes: &mut primes,
    };

    unsafe {
        // Set CTRL+C/Sigint handler
        ctrlc::set_handler(move || {
            let move_ptrs = raw_ptrs;
            print!("{} - {}", *move_ptrs.num_cycles, (*move_ptrs.primes).len());
            exit(1)
        })
        .expect("Error setting Ctrl-C handler");
    }

    // Run the algorithm over and over until interrupted
    loop {
        unsafe {
            find_primes(limit, &raw_ptrs);
        }
    }
}
