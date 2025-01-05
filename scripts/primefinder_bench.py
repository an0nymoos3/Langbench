#!/usr/bin/env python3

# import concurrent.futures
import subprocess
import time
import os
import sys
import signal
import math

# Global variable representing state of program. Used for progress bar.
BENCHMARK_PROGRESS = 0

# Global variable representing total amount of steps (seconds) in program. Used for progress bar.
TOTAL_BENCHMARK_STEPS = 0

# Default command line options
PROGRESS_BAR = True
PARALLELL = False


def print_help() -> None:
    os.system("clear")

    help_message = """ primefinder_bench.py [options]
Options: 
    -h  | --help       | Prints this message.
    -np | --no-progbar | Don't print the progressbar. 
    -p  | --parallell  | Run all benchmarks in parallell (if enough CPU threads are available) """

    print(help_message)


def parse_args() -> None:
    """
    Reads through command line args and sets proper options for the benchmarks.
    """
    global PROGRESS_BAR
    global PARALLELL

    for arg in sys.argv:
        if arg == "-h" or arg == "--help":
            print_help()
            exit(0)

        if arg == "-np" or arg == "--no-progbar":
            PROGRESS_BAR = False

        if arg == "-p" or arg == "--parallell":
            PARALLELL = True


def compile_lang(language, source_files) -> None:
    """
    Compile benchmark for specified programming language.
    """
    draw_pretty_progress(f"Compiling: {language}")
    subprocess.run(source_files, shell=True, stdout=subprocess.PIPE)


def benchmark_lang(language, script_command, max_time, total_primes) -> float:
    """
    Runs each language for the designated amount of time.
    Returns the number of cycles the program managed to run.
    """
    draw_pretty_progress(f"Running: {language}")

    proc = subprocess.Popen(args=script_command, stdout=subprocess.PIPE)

    time.sleep(max_time / 2)
    draw_pretty_progress(f"Running: {language}")
    time.sleep(max_time / 2)

    proc.send_signal(signal.SIGINT)  # Tell program to stop
    out = (
        str(proc.communicate()[0]).strip("'").strip("b'")
    )  # Read program output (number of cycles completed and number of primes found during current cycle)

    (cycles, remainder) = out.split(" - ")
    result = float(cycles) + float(remainder) / float(total_primes)
    return result


def draw_pretty_progress(progress_text) -> None:
    """
    Draws progess bar to terminal.
    """
    global BENCHMARK_PROGRESS
    global TOTAL_BENCHMARK_STEPS
    global PROGRESS_BAR

    if PROGRESS_BAR:
        os.system("clear")
        print(progress_text)

        BENCHMARK_PROGRESS += 1

        # Build the progress bar string.
        bar = "["
        for _ in range(BENCHMARK_PROGRESS - 1):
            bar += "="
        bar += ">"
        for _ in range(TOTAL_BENCHMARK_STEPS + 1 - BENCHMARK_PROGRESS):
            bar += " "
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
        for _, j in enumerate(primes):
            if j > sqrt_i:
                break

            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return len(primes)


if __name__ == "__main__":
    # Check commandline
    parse_args()

    # Ask user about benchmark
    os.system("clear")
    max_num = input("How high (max number) would you like to go? ")
    max_time = float(input("How much time would you like to give each language? "))

    # Containers needed to run the benchmarks
    results = {
        "C": 0.0,
        "C++": 0.0,
        "Go": 0.0,
        "Java": 0.0,
        "Python": 0.0,
        "Rust": 0.0,
        "Zig": 0.0,
    }
    compile_commands = {
        "C": "make c_build",
        "C++": "make cpp_build",
        "Go": "make go_build",
        "Java": "make java_build",
        "Rust": "make rust_build",
        "Zig": "make zig_build",
    }
    benchmark_commands = {
        "C": ["./bin/c_findprimes", max_num],
        "C++": ["./bin/cpp_findprimes", max_num],
        "Go": ["./bin/go_primefinder", max_num],
        "Java": ["java", "-cp", "java/primefinder/src/", "Main", max_num],
        "Python": ["python3", "python/findprimes.py", max_num],
        "Rust": ["./bin/rust_primefinder", max_num],
        "Zig": ["./bin/zig_primefinder", max_num],
    }

    # Set actual number of steps to run.
    TOTAL_BENCHMARK_STEPS = len(compile_commands) + len(benchmark_commands) * 2

    # Calculate total number of primes as refrence for calulating what fraction of a
    # cycle was completed when each language was sent SIGINT
    total_num_primes = calc_total_nr_of_primes(max_num)

    # Clear bin/
    os.system("make clean")
    os.system("clear")

    # Compile all the languages.
    for language in compile_commands:
        compile_lang(language, compile_commands[language])

    # Benchmark all the languages.
    for language in benchmark_commands:
        results[language] += benchmark_lang(
            language, benchmark_commands[language], max_time, total_num_primes
        )

    os.system("clear")
    print("-- Results --")
    # Print results
    for language in results:
        print(
            f"{language}: Execution Time - {results[language]/max_time:.3} cycles / second"
        )
