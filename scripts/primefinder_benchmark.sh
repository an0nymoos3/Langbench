clear
echo "Note: All benchmarks are run 3 times to allow the program to 'warm up'."
echo "Make sure you have GNU/time installed on your system!"
sleep 1
echo "How high (max number) would you like to go?"
read max_num
clear

# -- Java --
clear
echo "Compiling Java..."
echo "[>                ]"
cd java/primefinder/src/
javac Main.java 

clear
echo "Running Java benchmark..."
echo "[=>               ]"
java Main $max_num > /dev/null

clear
echo "Running Java benchmark..."
echo "[==>              ]"
java Main $max_num > /dev/null

clear
echo "Running Java benchmark..."
echo "[===>             ]"
\time -o ../../../java.txt -f "%C\nTime: %e\n%P\n" java Main $max_num

cd ../../../

# - Rust --
clear
echo "Compiling Rust benchmark..."
echo "[====>            ]"
cd rust/primefinder/
cargo build --release --quiet
cd ../..

clear
echo "Running Rust benchmark..."
echo "[=====>           ]"
./rust/primefinder/target/release/primefinder -l $max_num > /dev/null

clear
echo "Running Rust benchmark..."
echo "[======>          ]"
./rust/primefinder/target/release/primefinder -l $max_num > /dev/null

clear
echo "Running Rust benchmark..."
echo "[=======>         ]"
\time -o rust.txt -f "%C\nTime: %e\n%P\n" ./rust/primefinder/target/release/primefinder -l $max_num

# -- C++ --
clear
echo "Compiling C++ benchmark..."
echo "[========>        ]"
g++ -O3 c/findprimes.cpp -o c/findprimes

clear
echo "Running C++ benchmark..."
echo "[=========>       ]"
./c/findprimes $max_num > /dev/null

clear
echo "Running C++ benchmark..."
echo "[==========>      ]"
./c/findprimes $max_num > /dev/null

clear
echo "Running C++ benchmark..."
echo "[===========>     ]"
\time -o cpp.txt -f "%C\nTime: %e\n%P\n" ./c/findprimes $max_num

# -- Python -- 
clear
echo "Running Python benchmark..."
echo "[============>    ]"
python3 python/findprimes.py $max_num > /dev/null

clear
echo "Running Python benchmark..."
echo "[=============>   ]"
python3 python/findprimes.py $max_num > /dev/null

clear
echo "Running Python benchmark..."
echo "[==============>  ]"
\time -o python.txt -f "%C\nTime: %e\n%P\n" python3 python/findprimes.py $max_num

# -- JavaScript --
clear
echo "Running JS benchmark..."
echo "[==============>  ]"
node $(pwd)/javascript/findprimes.js $max_num > /dev/null

clear
echo "Running JS benchmark..."
echo "[===============> ]"
node $(pwd)/javascript/findprimes.js $max_num > /dev/null

clear
echo "Running JS benchmark..."
echo "[================>]"
\time -o js.txt -f "%C\nTime: %e\n%P\n" node $(pwd)/javascript/findprimes.js $max_num

clear
echo "Compiling results"
echo "[=================]"
sleep 1

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