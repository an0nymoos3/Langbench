import concurrent.futures
import subprocess
import time


def compile_script(source_files):
    subprocess.run(source_files, shell=True)


def run_script(script_command):
    start_time = time.time()
    subprocess.run(script_command, shell=True)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


if __name__ == "__main__":
    max_num = input("How high (max number) would you like to go? ")

    print("Compiling code!")
    time.sleep(1)

    compile_commands = [
        "javac java/primefinder/src/Main.java", 
        "cargo rust/primefinder/build --release --quiet", 
        "g++ -O3 c/findprimes.cpp -o c/findprimes"
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        compile_script, compile_commands

    print("Compilation complete, running code!")

    execution_time = [0, 0, 0, 0, 0]
    n = 0
    while n < 3:
        script_commands = [   
            "java -cp java/primefinder/src Main {}".format(max_num),   
            "./rust/primefinder/target/release/primefinder -l {}".format(max_num), 
            "./c/findprimes {}".format(max_num), 
            "python3 python/findprimes.py {}".format(max_num), 
            "node javascript/findprimes.js {}".format(max_num)             
        ]

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(run_script, script_commands))

        j = 0
        for run_time in results: 
            execution_time[j] += run_time
            j += 1
        
        n += 1
        print(n, " rounds completed!")

    
    time.sleep(1)
    languages = [
        "Java", 
        "Rust",
        "C++", 
        "Python", 
        "JavaScript"
    ]

    i = 0
    for run_time in execution_time:
        print(f"{languages[i]}: Execution Time - {run_time/n:.2f} seconds")
        i += 1

