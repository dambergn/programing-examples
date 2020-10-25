#include <stdio.h>
#include <stdbool.h>
#include <math.h> // when using math compile with -lm
// Take an imput numer from user.
// Calculate all prinme numbers from zero to user defined number.
// print out all the found prime numbers.
// Print how many prime numbers were found.

bool isPrime(int input)
{
  for (int i = sqrt(input); i > 1; i--)
  {
    if (input % i == 0)
    {
      return false;
    }
  }
  return true;
}

int main()
{

  printf("Please enter a number to find prime numbers up to: ");

  int input = 0;
  scanf("%i", &input);

  int primeFound = 0;
  for (int i = input; i > 1; i--)
  {
    bool prime = isPrime(i);
    if (prime)
    {
      primeFound++;
      printf("%d Is Prime\n", i);
    }
  }
  printf("%d prime number found in range.\n", primeFound);
  return 0;
}