# C programing
Basic C concepts tests
- https://www.tutorialspoint.com/cprogramming/c_basic_syntax.htm
- https://www.youtube.com/watch?v=CPjZKsUYSXg&list=PL_c9BZzLwBRKKqOc9TJz1pP0ASrxLMtp2

## Install GCC compiler (Ubuntu)
- gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)
- https://www.gnu.org/software/gcc/
```
sudo apt get install gcc
```

## To use
```
# -- to compile --
gcc hello.c

# -- to run --
./a.out
```
### compile and run with custom name
- gcc -o "custom_name" "file_to_compile"
```
gcc -o hello hello.c
./hello
```
### Simple run script
```
./compile.sh
#enter the name of the file you want to compile and run.
```

### Compile on linux to windows exe

```
sudo apt-get install mingw-w64

#Then you can create 32-bit Windows executable with:
i686-w64-mingw32-gcc -o hello32.exe hello.c

#And 64-bit Windows executable with:
x86_64-w64-mingw32-gcc -o hello64.exe hello.c
```
- note text based apps will need to be run from cmd prompt