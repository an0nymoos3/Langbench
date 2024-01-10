pub struct PrimeFinder {
    pub primes: Vec<i32>,
    pub num_cycles: i32,
}

impl PrimeFinder {
    /// Doesn't use new, only from to pre-allocate the capacity needed for Vec.
    pub fn new() -> Self {
        return Self { primes: Vec::new(), num_cycles: 0 }
    }

    pub fn set_capacity(&mut self, limit: i32) {
        let capacity: usize = f32::sqrt(limit as f32) as usize;
        self.primes.try_reserve(capacity).expect("Could not reserve extra capacity for Vec!");
    }
}
