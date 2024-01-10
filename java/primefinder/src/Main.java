import java.util.ArrayList;
import java.lang.Math;

public class Main
{
    public static void main(String[] args) {
        int limit = Integer.parseInt(args[0]);

        ArrayList<Integer> primes = new ArrayList<Integer>();
        ArrayList<Integer> cycles = new ArrayList<Integer>(); // Using arralist instead of int as temp. solution for SIGINT handler print

        var shutdownListener = new Thread(){
            public void run() {
                System.out.print(cycles.size() + " - " + primes.size());
            }
        };
        Runtime.getRuntime().addShutdownHook(shutdownListener);

        while(true) {
            primes.clear();
            calculatePrimes(limit, primes);
            cycles.add(0);
        }
    }

    public static void calculatePrimes(int limit, ArrayList<Integer> primes) {
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
