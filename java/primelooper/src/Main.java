import java.util.ArrayList;
import java.lang.Math;

public class Main
{
    public static void main(String[] args) {
        int time_limit = Integer.parseInt(args[0]);

        double found_primes = calculatePrimes(time_limit);
        double cycles = found_primes / 78498;

        System.out.println("Java ran: " + cycles + " cycle(s)");
    }

    public static double calculatePrimes(int time_limit) {
        time_limit *= 1000;
        // Create a vector to store known primes
        ArrayList<Integer> primes = new ArrayList<Integer>();
        primes.add(2); // Add first known prime
        int current_num = 3;

        final long startTime = System.currentTimeMillis();
        long endTime = System.currentTimeMillis();

        while ((endTime - startTime) < time_limit) {

            endTime = System.currentTimeMillis();

            boolean isPrime = true;
            double sqrt_i = Math.sqrt(current_num);

            for (Integer prime : primes) {
                if (prime > sqrt_i) { // Max value to compare with (due to how math works)
                    break;
                }

                if (current_num % prime == 0) { // If its divisible by any already known prime
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(current_num); // Add to known primes
            }
            if (current_num >= 1000000) {
                current_num = 3;
            }
            else {
                current_num += 2;
            }
        }
        return primes.size();
    }
}
