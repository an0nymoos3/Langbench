# Default target when just typing 'make'
.DEFAULT_GOAL := all

go_build:
	go build -o bin/go_primefinder go/cmd/findprimes/main.go
 
rust_build:
	cargo build --manifest-path rust/primefinder/Cargo.toml --release --quiet
	cp rust/primefinder/target/release/rust_primefinder bin/
 
cpp_build:
	g++ -Ofast c/findprimes.cpp -o bin/cpp_findprimes

c_build:
	g++ -Ofast c/findprimes.c -o bin/c_findprimes

java_build:
	javac java/primefinder/src/Main.java

zig_build:
	zig build-exe -O ReleaseFast zig/findprimes.zig -femit-bin=bin/zig_primefinder -lc

# All build target
all: go_build rust_build cpp_build c_build java_build zig_build

clean:
	rm -rf bin/
	mkdir bin
