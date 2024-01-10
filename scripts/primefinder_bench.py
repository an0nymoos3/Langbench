#!/usr/bin/env python3

#import concurrent.futures
import subprocess
import time
import os
import signal
import math

# Global variable representing state of program. Used for progress bar.
BENCHMARK_PROGRESS = 0

# Global variable representing total amount of steps (seconds) in program. Used for progress bar.
TOTAL_BENCHMARK_STEPS = 9

def compile_lang(language, source_files) -> None:
    """
    Compile benchmark for specified programming language.
    """
    draw_pretty_progress(f"Compiling: {language}")
    subprocess.run(source_files, shell=True)


def benchmark_lang(language, script_command, max_time, total_primes) -> float:
    """
    Runs each language for the designated amount of time.
    Returns the number of cycles the program managed to run.
    """
    draw_pretty_progress(f"Running: {language}")

    proc = subprocess.Popen(args=script_command, stdout=subprocess.PIPE)
    time.sleep(max_time)
    proc.send_signal(signal.SIGINT) # Tell program to stop

    out = str(proc.communicate()[0]).strip("'").strip("b'") # Read program output (number of cycles completed and number of primes found during current cycle)

    (cycles, remainder) = out.split(" - ")
    result = float(cycles) + float(remainder) / float(total_primes)

    #print(cycles, ", ", remainder, ", ", total_primes)
    return result


def draw_pretty_progress(progress_text) -> None:
    """
    Draws progess bar to terminal.
    """
    global BENCHMARK_PROGRESS
    global TOTAL_BENCHMARK_STEPS

    os.system("clear")
    print(progress_text)

    BENCHMARK_PROGRESS += 1

    # Build the progress bar string.
    bar = "["
    for _ in range(BENCHMARK_PROGRESS - 1):
        bar += "=" * 2
    bar += ">"
    for _ in range(TOTAL_BENCHMARK_STEPS - 1 - BENCHMARK_PROGRESS):
        bar += " " * 2
    bar += "]"

    # Print progress bar
    print(bar)

def calc_total_nr_of_primes(limit) -> float:
    """
    Looks for prime numbers up to the limit.
    This benchmark is not meant to be run with limits above 100,000. Therefore 
    calculating the number of primes in Python should be fine despite the performance.
    """
    draw_pretty_progress("Calulating number of primes...")

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

    return len(primes)


if __name__ == "__main__":
    os.system("clear")
    max_num = input("How high (max number) would you like to go? ")
    max_time = float(input("How much time would you like to give each language? "))

    results = {"C++": 0.0,
               "Java": 0.0,
               "Python": 0.0,
               "Rust": 0.0}

    compile_commands = {
        "C++": "g++ -O3 c/findprimes.cpp -o c/findprimes",
        "Java": "javac java/primefinder/src/Main.java", 
        "Rust": "cargo build --manifest-path rust/primefinder/Cargo.toml --release --quiet"}

    benchmark_commands = {
        "C++" : ["./c/findprimes", max_num],
        "Java": ["java", "-cp", "java/primefinder/src/", "Main", max_num],
        "Python": ["python3", "python/findprimes.py", max_num],
        "Rust": ["./rust/primefinder/target/release/primefinder", "-l", max_num]}
    
    #"JavaScript": 0.0,
    #"JavaScript" : "node javascript/findprimes.js {}".format(max_num),

    #Calculate total number of primes as refrence for calulating what fraction of a 
    #cycle was completed when each language was sent SIGINT
    total_num_primes = calc_total_nr_of_primes(max_num)

    # Compile all the languages.
    for language in compile_commands:
        compile_lang(language, compile_commands[language])

    # Benchmark all the languages.
    for language in benchmark_commands:
        results[language] += benchmark_lang(language, benchmark_commands[language], max_time, total_num_primes)
        
    # Print results
    for language in results:
        print(f"{language}: Execution Time - {results[language]} cycles")

