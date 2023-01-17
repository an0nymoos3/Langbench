import time, math
import argparse

def findprimes(limit):
    primes = [2]
    for i in range(3, int(limit)):
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an upper limit to go to')
    args = parser.parse_args()

    start_time = time.time()
    findprimes(args.integers[0])
    end_time = time.time()

    print(f"Python execution time: {(end_time - start_time) * 1000}ms")


if __name__ == "__main__":
    main()