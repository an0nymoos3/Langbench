import math
import argparse
import signal
import sys

# Global variables to allow signal_handler to reach them.
primes = []
num_cycles = 0


def findprimes(limit) -> None:
    """
    Looks for prime numbers up to the limit.
    """
    global primes
    global num_cycles

    primes = [2]  # Reset the list of primes
    # Check all odd numbers as even numbers can't be prime
    for i in range(3, int(limit), 2):
        is_prime = True
        sqrt_i = math.sqrt(i)
        for _, j in enumerate(primes):  # Iterate over all already known primes
            # Exit if prime is larger than sqrt of i as it cannot divide evenly any longer.
            if j > sqrt_i:
                break

            # If j divides i, i isn't prime.
            if i % j == 0:
                is_prime = False
                break

        # Add new prime to list of primes
        if is_prime:
            primes.append(i)

    # Increment number of fully completed cycles
    num_cycles += 1


def signal_handler(sig, frame) -> None:
    """
    Handles SIGINT/ CTRL+C.
    """
    global primes
    global num_cycles

    # Print "number_cycles - current_length_of_primes"
    print(f"{num_cycles} - {len(primes)}", end="")
    sys.exit(0)


def main():
    """
    main()
    """

    # Get the upper limit from command line args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an upper limit to go to"
    )
    args = parser.parse_args()

    # Set CTRL+C/Sigint handler
    signal.signal(signal.SIGINT, signal_handler)

    # Keep running until program is manually interrupted
    while True:
        findprimes(args.integers[0])


if __name__ == "__main__":
    main()
