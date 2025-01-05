const std = @import("std");
const ArrayList = std.ArrayList;
const FixedBufAllocator = std.heap.FixedBufferAllocator;
const c = @cImport({
    @cInclude("signal.h");
    @cInclude("unistd.h");
});

const SIGINT = 2; // Signal number for SIGINT

const PrimesBuffer = struct {
    len: usize,
    cycles: usize,
    buffer: ArrayList(u32),
};

var gpa = std.heap.GeneralPurposeAllocator(.{}){};
const allocator = gpa.allocator();
const buffer: ArrayList(u32) = ArrayList(u32).init(allocator);

var primes_buffer = PrimesBuffer{
    .len = 0,
    .cycles = 0,
    .buffer = buffer,
};

fn findprimes(limit: u32) !void {
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
    primes_buffer.cycles += 1;
}

fn handle_sigint(_: c_int) callconv(.C) void {
    const stdout = std.io.getStdOut().writer();
    errdefer std.process.exit(0);
    try stdout.print("{} - {}", .{ primes_buffer.cycles, primes_buffer.len });
    std.process.exit(0);
}

pub fn main() !void {
    // Create a sigaction struct to specify the signal handling behavior
    var sa: c.struct_sigaction = undefined;
    sa.__sigaction_handler.sa_handler = handle_sigint;
    sa.sa_flags = 0; // No special flags for simplicity
    _ = c.sigemptyset(&sa.sa_mask); // Clear the signal mask

    // Set the signal handler for SIGINT
    _ = c.sigaction(SIGINT, &sa, null);

    // Get commandline arguments
    const args_allocator = std.heap.page_allocator;
    var args = try std.process.argsWithAllocator(args_allocator);
    _ = args.skip();
    const limit_arg: []const u8 = args.next().?;
    const limit_u32: u32 = try std.fmt.parseInt(u32, limit_arg, 10);

    while (true) {
        try findprimes(limit_u32);
    }
}
