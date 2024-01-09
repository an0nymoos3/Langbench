#!/usr/bin/env python3

#import concurrent.futures
import subprocess
import time
import os

# Global variable representing state of program. Used for progress bar.
BENCHMARK_PROGRESS = 0

# Global variable representing total amount of steps (seconds) in program. Used for progress bar.
TOTAL_BENCHMARK_STEPS = 25

def compile_lang(source_files) -> None:
    """
    Compile benchmark for specified programming language.
    """
    os.system("clear")
    print(f"Compiling: {source_files}")
    subprocess.run(source_files, shell=True)


def benchmark_lang(script_command, max_time) -> float:
    """
    Runs each language for the designated amount of time.
    Returns the number of cycles the program managed to run.
    """
    global BENCHMARK_PROGRESS

    BENCHMARK_PROGRESS += 1
    draw_pretty_progress(f"Running: {script_command}")

    proc = subprocess.Popen([], stdout=subprocess.PIPE)
    time.sleep(5.0)
    out = proc.communicate()[0]
    print(out)

    return out


def draw_pretty_progress(progress_text):
    """
    Draws progess bar to terminal.
    """
    global BENCHMARK_PROGRESS
    global TOTAL_BENCHMARK_STEPS

    os.system("clear")
    print(progress_text)

    # Build the progress bar string.
    bar = "["
    for _ in range(BENCHMARK_PROGRESS):
        bar += "="
    bar += ">"
    for _ in range(TOTAL_BENCHMARK_STEPS - BENCHMARK_PROGRESS):
        bar += " "
    bar += "]"

    # Print progress bar
    print(bar)


if __name__ == "__main__":
    os.system("clear")
    max_num = input("How high (max number) would you like to go? ")
    max_time = input("How much time would you like to give each language? ")

    results = {"C++": 0.0,
               "Java": 0.0,
               "JavaScript": 0.0,
               "Python": 0.0,
               "Rust": 0.0}

    compile_commands = [
        "g++ -O3 c/findprimes.cpp -o c/findprimes",
        "javac java/primefinder/src/Main.java", 
        "cargo build --manifest-path rust/primefinder/Cargo.toml --release --quiet"]

    benchmark_commands = {
        "C++" : "./c/findprimes {}".format(max_num),
        "Java": "java -cp java/primefinder/src/ Main {}".format(max_num),
        "JavaScript" : "node javascript/findprimes.js {}".format(max_num),
        "Python": "python3 python/findprimes.py {}".format(max_num),
        "Rust": "./rust/primefinder/target/release/primefinder -l {}".format(max_num)}

    # Compile all the languages.
    for compilation in compile_commands:
        compile_lang(compilation)

    # Benchmark all the languages.
    for language in benchmark_commands:
        benchmark_lang(benchmark_commands[language])
        
    # Print results
    for language in results:
        print(f"{language}: Execution Time - {results[language]:.2f} seconds")

