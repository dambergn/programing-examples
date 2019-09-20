#!/bin/bash

echo "Which file would you like to compile and run?"
read file

echo "What would you like the output name of your file to be?"
read new_name

linux () {
  gcc -o $new_name $file
}

win32 () {
  i686-w64-mingw32-gcc -o $new_name.exe $file
}

win64 () {
  x86_64-w64-mingw32-gcc -o $new_name.exe $file
}

echo "Would you like to compile for Linux, Windows32, or Windows64?"
read option

if [ $option = "Linux" ]; then
  linux
  echo "Running compiled program"
  ./$new_name
fi

if [ $option = "Windows32" ]; then
  win32
  echo "Can not run windows executible on linux"
fi

if [ $option = "Windows64" ]; then
  win64
  echo "Can not run windows executible on linux"
fi

# echo "--compiling C code"
# gcc $file

# echo "--exicuting comiled code"
# ./a.out