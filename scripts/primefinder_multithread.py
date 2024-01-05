#!/usr/bin/env python3

import concurrent.futures
import subprocess
import time
import os

# Global variable representing state of program. Used for progress bar.
BENCHMARK_PROGRESS = 0

# Global variable representing total amount of steps in program. Used for progress bar.
TOTAL_BENCHMARK_STEPS = 18

def compile_script(source_files):
    """
    Compile program.
    """
    global BENCHMARK_PROGRESS
    
    BENCHMARK_PROGRESS += 1
    #draw_pretty_progress(f"Compiling: {source_files}")
    subprocess.run(source_files, shell=True)


def run_script(script_command):
    """
    Time the execution of program.
    """
    global BENCHMARK_PROGRESS

    BENCHMARK_PROGRESS += 1
    #draw_pretty_progress(f"Running: {script_command}")

    start_time = time.time()
    subprocess.run(script_command, shell=True)
    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time


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

    execution_time = {"C++": 0,
                      "Java": 0,
                      "JavaScript": 0,
                      "Python": 0,
                      "Rust": 0}

    compile_commands = [
        "g++ -O3 c/findprimes.cpp -o c/findprimes",
        "javac java/primefinder/src/Main.java", 
        "cargo build --manifest-path rust/primefinder/Cargo.toml --release --quiet"]

    script_commands = [
        "./c/findprimes {}".format(max_num),
        "java -cp java/primefinder/src/ Main {}".format(max_num),
        "node javascript/findprimes.js {}".format(max_num),
        "python3 python/findprimes.py {}".format(max_num),
        "./rust/primefinder/target/release/primefinder -l {}".format(max_num)]

    # Compile all compiled languages
    with concurrent.futures.ProcessPoolExecutor() as executor:
        compile_script, compile_commands

    # Run all languages 3 times
    for i in range(3):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(run_script, script_commands))

        # Add result to language
        index = 0
        for language in execution_time: 
            execution_time[language] += results[index]
            index += 1

    # Print results
    for language in execution_time:
        print(f"{language}: Execution Time - {execution_time[language]/3:.2f} seconds")
        i += 1

