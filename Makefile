go_build:
	go build -o bin/go_primefinder go/cmd/findprimes/main.go
 
rust_build:
	MALLOC_CONF="thp:always,metadata_thp:always" cargo build --manifest-path rust/primefinder/Cargo.toml --release --quiet
	cp rust/primefinder/target/release/rust_primefinder bin/
 
cpp_build:
	g++ -O3 c/findprimes.cpp -o bin/cpp_findprimes

c_build:
	g++ -O3 c/findprimes.c -o bin/c_findprimes

java_build:
	javac java/primefinder/src/Main.java

clean:
	rm -rf bin/
	mkdir bin
