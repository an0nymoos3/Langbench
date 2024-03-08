package main

import (
	"fmt"
	"math"
	"os"
	"os/signal"
	"strconv"
	"syscall"
)

func findprimes(limit int, num_cycles *int, primes *[]int) {
	*primes = []int{2}

	for i := 3; i <= limit; i += 2 {
		inner_limit := math.Sqrt(float64(i))
		is_prime := true

		for _, prime := range *primes {
			if float64(prime) > inner_limit {
				break
			}
			if i%int(prime) == 0 {
				is_prime = false
				break
			}
		}
		if is_prime {
			*primes = append(*primes, i)
		}
	}

	// Increment number of cycles
	*num_cycles += 1
}

func print_results(cycles int, num_primes int) {
	fmt.Print(cycles, " - ", num_primes)
}

func main() {
	num_cycles := 0
	primes := []int{}
	limit := os.Args[1] // Access first arg (that's not the program itself)

	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		print_results(num_cycles, len(primes))
		os.Exit(0)
	}()

	val, err := strconv.ParseInt(limit, 0, 64)
	if err != nil {
		panic(err)
	}

	for {
		findprimes(int(val), &num_cycles, &primes)
	}
}
