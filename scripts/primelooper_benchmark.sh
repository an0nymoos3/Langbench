echo "Note: All benchmarks are run 3 times to allow the program to 'warm up'."
echo "For how long would you like to benchmark each language? [unit seconds]"
read max_time

# -- Java --
echo "Running Java benchmark..."
java java/primelooper/src/Main.java $max_time

# - Rust --
echo "Compiling Rust benchmark..."
sleep 1

cd rust/primelooper/
cargo build --release --quiet
cd ../..

echo "Running Rust benchmark..."
./rust/primelooper/target/release/primelooper -l $max_time

# -- C++ --
echo "Compiling C++ benchmark"
#sleep 1
g++ -O3 c/primelooper.cpp -o c/primelooper

echo "Running C++ benchmark"
./c/primelooper $max_time

# -- Python -- 
echo "Running python benchmark..."
python3 python/primelooper.py $max_time

# -- JavaScript --
echo "Running js benchmark..."
node $(pwd)/javascript/primelooper.js $max_time
