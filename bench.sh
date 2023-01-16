echo "Running Java benchmark..."

java FindPrimes.java

echo "Running Rust benchmark..."

./findprimes/target/release/findprimes

echo "Running python benchmark..."

python findprimes.py
