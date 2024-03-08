use std::env;
use std::process::exit;

#[derive(Clone, Copy)]
struct HoldsRawPtr {
    num_cycles: *const i32,
    primes: *mut Vec<i32>,
    primes_len: *mut usize,
}

// By implementing the Send trait, we tell compiler that this type can be transferred between
// threads without violating safety. Whether it actually is safe is our responsibility
unsafe impl Send for HoldsRawPtr {}
// Sync trait tells compiler that `&T` is safe to share between threads
unsafe impl Sync for HoldsRawPtr {}

unsafe fn find_primes(limit: i32, raw_ptrs: &HoldsRawPtr) {
    for i in (0..limit).step_by(2) {
        let mut is_prime: bool = true;
        let inner_limit: f32 = f32::sqrt(i as f32);

        for prime in raw_ptrs.primes.read().iter() {
            if *prime as f32 > inner_limit {
                break;
            }
            if i % prime == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            raw_ptrs.primes.read()[*raw_ptrs.primes_len - 1] = i;
            *raw_ptrs.primes_len += 1;
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect::<Vec<String>>();
    let limit: i32;

    // Skip out of bounds check
    #[allow(unused_unsafe)]
    unsafe {
        limit = args.get_unchecked(1).parse::<i32>().unwrap();
    }

    let mut primes: Vec<i32> = vec![2];

    let raw_ptrs: HoldsRawPtr = HoldsRawPtr {
        num_cycles: &0,
        primes: &mut primes,
        primes_len: &mut 1,
    };

    unsafe {
        ctrlc::set_handler(move || {
            let move_ptrs = raw_ptrs;
            print!(
                "{} - {}",
                move_ptrs.num_cycles.read(),
                move_ptrs.primes_len.read(),
            );
            exit(1)
        })
        .expect("Error setting Ctrl-C handler");
    }

    loop {
        unsafe {
            find_primes(limit, &raw_ptrs);
        }
    }
}
