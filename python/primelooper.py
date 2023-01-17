import time, math
import argparse
from multiprocessing import cpu_count, Process, Queue

Q = Queue()

def findprimes(time_limit):
    primes = 0
    procs = []
    for _ in range(cpu_count()):  # Split load evenly across CPU cores
        p = Process(target=calc_primes, args=(time_limit,))
        p.start()
        procs.append(p)

    for _ in procs:
        print(Q.get())
        primes += Q.get()

    return primes


def calc_primes(time_limit):
    start_time = time.time()
    primes = [2]
    current_num = 3
    current_time = time.time()

    while (current_time - start_time) < time_limit:
        current_time = time.time()

        is_prime = True
        sqrt_num = math.sqrt(current_num)

        for _, j in enumerate(primes):
            if j > sqrt_num:
                break

            if current_num % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current_num)

        if current_num >= 1_000_000:
            current_num = 3
        else:
            current_num += 2

    Q.put(len(primes))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', metavar='N', type=int, nargs='+',
                    help='How long the benchmark goes on')
    args = parser.parse_args()

    primes_found = findprimes(args.time[0])

    print(f"Python ran: {primes_found / 78498} cycle(s)")


if __name__ == "__main__":
    main()