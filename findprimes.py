import time, math

def findprimes():
    primes = [2]
    for i in range(2, 10_000_000):
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
    start_time = time.time()
    findprimes()
    end_time = time.time()

    print(f"Python execution time: {(end_time - start_time) * 1000}ms")


if __name__ == "__main__":
    main()