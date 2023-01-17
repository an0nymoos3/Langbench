echo "For how long would you like to benchmark each language? [unit seconds]"
read max_time

# -- Java --
echo "Running Java benchmark..."
#java java/FindPrimes.java $max_time

# - Rust --
echo "Compiling Rust benchmark..."
sleep 1

cd rust/primelooper/
cargo build --release --quiet
cd ../..

echo "Running Rust benchmark..."
sleep 1
./rust/primelooper/target/release/primelooper -l $max_time

# -- C++ --
echo "Compiling C++ benchmark"
#sleep 1
#g++ c/findprimes.cpp -o c/findprimes

echo "Running C++ benchmark"
#sleep 1
#./c/findprimes $max_time

# -- Python -- 
echo "Running python benchmark..."
python3 python/primelooper.py $max_time

# -- JavaScript --
echo "Running js benchmark..."
#node $(pwd)/javascript/findprimes.js $max_time
