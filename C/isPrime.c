#include <stdio.h>
#include <stdbool.h>
#include <math.h>// when using math compile with -lm
// Take an imput numer from user.
// Calculate all prinme numbers from zero to user defined number.
// print out all the found prime numbers.
// Print how many prime numbers were found.

int main(){

  printf("Please enter a number to find prime numbers up to: ");

  int input = 0;
  scanf("%i", &input);

  bool isPrime = true;
  int primeFound = 0;

  for(int i = sqrt(input); i > 1; i--){
    if(input % i == 0){
      isPrime = false;
    }
  }
  if(isPrime){
      primeFound++;
      printf("\nIs Prime\n");
    } else {
      printf("\nNot Prime\n");
    }

  return 0;
}