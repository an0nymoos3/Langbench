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

    primes = [2]
    for i in range(3, int(limit), 2):
        is_prime = True
        sqrt_i = math.sqrt(i)
        for _,j in enumerate(primes):
            if j > sqrt_i:
                break

            if i % j == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(i)


def signal_handler(sig, frame) -> None:
    """
    Handles SIGINT/ CTRL+C.
    """
    global primes
    global num_cycles

    print(f"{num_cycles} - {len(primes)}", end="")
    sys.exit(0)

def main():
    """
    main()
    """
    global primes
    global num_cycles

    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an upper limit to go to')
    args = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)

    while(True):
        primes.clear()
        findprimes(args.integers[0])
        num_cycles += 1


if __name__ == "__main__":
    main()