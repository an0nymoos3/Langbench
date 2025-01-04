const std = @import("std");
const ArrayList = std.ArrayList;
const FixedBufAllocator = std.heap.FixedBufferAllocator;

const PrimesBuffer = struct {
    len: usize,
    buffer: ArrayList(u32),
};

fn findprimes(limit: u32, primes_buffer: *PrimesBuffer) !void {
    // Add 2 as the first prime
    primes_buffer.len = 1;
    try primes_buffer.buffer.append(2);

    for (3..limit) |i| {
        var is_prime: bool = true;
        const inner_limit = std.math.sqrt(limit);

        for (0..primes_buffer.len) |j| {
            const prime = primes_buffer.buffer.items[j];

            // Can no longer find new primes
            if (prime > inner_limit) {
                break;
            }

            // Found a prime
            if (i % prime == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            // Add newly discovered prime number
            try primes_buffer.buffer.append(@intCast(i));
            primes_buffer.len += 1;
        }
    }
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    const buffer: ArrayList(u32) = ArrayList(u32).init(allocator);

    var primes_buffer = PrimesBuffer{
        .len = 0,
        .buffer = buffer,
    };

    try findprimes(10000000, &primes_buffer);
}
