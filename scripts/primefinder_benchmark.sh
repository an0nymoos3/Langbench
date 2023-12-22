clear
echo "Note: All benchmarks are run 3 times to allow the program to 'warm up'."
echo "Make sure you have GNU/time installed on your system!"
sleep 1
echo "How high (max number) would you like to go?"
read max_num
clear

# -- Java --
echo "Compiling Java..."
cd java/primefinder/src/
javac Main.java

echo "Running Java benchmark..."
java Main $max_num > /dev/null
java Main $max_num > /dev/null
\time -o ../../../java.txt -f "%C\nTime: %e\n%P\n" java Main $max_num

cd ../../../

# - Rust --
echo "Compiling Rust benchmark..."
sleep 1

cd rust/primefinder/
cargo build --release --quiet
cd ../..

echo "Running Rust benchmark..."
sleep 1

./rust/primefinder/target/release/primefinder -l $max_num > /dev/null
./rust/primefinder/target/release/primefinder -l $max_num > /dev/null
\time -o rust.txt -f "%C\nTime: %e\n%P\n" ./rust/primefinder/target/release/primefinder -l $max_num

# -- C++ --
echo "Compiling C++ benchmark..."
sleep 1
g++ -O3 c/findprimes.cpp -o c/findprimes

echo "Running C++ benchmark..."
sleep 1
./c/findprimes $max_num > /dev/null
./c/findprimes $max_num > /dev/null
\time -o cpp.txt -f "%C\nTime: %e\n%P\n" ./c/findprimes $max_num

# -- Python -- 
echo "Running Python benchmark..."
python3 python/findprimes.py $max_num > /dev/null
python3 python/findprimes.py $max_num > /dev/null
\time -o python.txt -f "%C\nTime: %e\n%P\n" python3 python/findprimes.py $max_num

# -- JavaScript --
echo "Running JS benchmark..."
node $(pwd)/javascript/findprimes.js $max_num > /dev/null
node $(pwd)/javascript/findprimes.js $max_num > /dev/null
\time -o js.txt -f "%C\nTime: %e\n%P\n" node $(pwd)/javascript/findprimes.js $max_num

java=$(cat java.txt | grep Time)
rust=$(cat rust.txt | grep Time)
cpp=$(cat cpp.txt | grep Time)
py=$(cat python.txt | grep Time)
js=$(cat js.txt | grep Time)

javastring=${java:5:15}
ruststring=${rust:5:15}
cppstring=${cpp:5:15}
pystring=${py:5:15}
jsstring=${js:5:15}

clear
echo "Results: Java  |  Rust  |  C++  |  Python  |  JS  "
echo "Time:   $javastring    $ruststring    $cppstring    $pystring    $jsstring"