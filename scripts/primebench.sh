echo "How long would you like to run for? [unit seconds]"
read max_num

# -- Java --
echo "Running Java benchmark..."

java java/FindPrimes.java $max_num > /dev/null
java java/FindPrimes.java $max_num > /dev/null
java java/FindPrimes.java $max_num

# - Rust --
echo "Compiling Rust benchmark..."
sleep 1

cd rust
cargo build --release --quiet
cd ..

echo "Running Rust benchmark..."
sleep 1

./rust/target/release/findprimes -l $max_num > /dev/null
./rust/target/release/findprimes -l $max_num > /dev/null
./rust/target/release/findprimes -l $max_num

# -- C++ --
echo "Compiling C++ benchmark"
sleep 1
g++ c/findprimes.cpp -o c/findprimes

echo "Running C++ benchmark"
sleep 1
./c/findprimes $max_num > /dev/null
./c/findprimes $max_num > /dev/null
./c/findprimes $max_num

# -- Python -- 
echo "Running python benchmark..."

python python/findprimes.py $max_num > /dev/null
python python/findprimes.py $max_num > /dev/null
python python/findprimes.py $max_num

# -- JavaScript --
echo "Running js benchmark..."
node /home/oharradine/projects/fun_stuff/javascript/findprimes.js $max_num > /dev/null
node /home/oharradine/projects/fun_stuff/javascript/findprimes.js $max_num > /dev/null
node /home/oharradine/projects/fun_stuff/javascript/findprimes.js $max_num
