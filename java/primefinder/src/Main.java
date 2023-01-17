import java.util.ArrayList;
import java.lang.Math;

public class Main
{
    public static void main(String[] args) {
        int limit = Integer.parseInt(args[0]);
        final long startTime = System.currentTimeMillis();

        calculatePrimes(limit);

        final long endTime = System.currentTimeMillis();
        System.out.println("Java execution time: " + (endTime - startTime) + "ms");
    }

    public static void calculatePrimes(int limit) {
        // Create a vector to store known primes
        ArrayList<Integer> primes = new ArrayList<Integer>();
        primes.add(2); // Add first known prime

        for (int i=3; i < limit; i+=2) { // Iterate over all numbers from 2 to 10,000,000
            boolean isPrime = true;
            double sqrt_i = Math.sqrt(i);

            for (Integer prime : primes) {
                if (prime > sqrt_i) { // Max value to compare with (due to how math works)
                    break;
                }

                if (i % prime == 0) { // If its divisible by any already known prime
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(i); // Add to known primes
            }
        }
    }
}
