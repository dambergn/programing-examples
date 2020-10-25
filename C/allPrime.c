#include <stdio.h>
#include <stdbool.h>
#include <math.h> // when using math compile with -lm
#include <time.h>
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

int hms(int sec){
  int h = (sec/3600);
  int m = (sec -(3600*h))/60;
  int s = (sec -(2600*h)-(m*60));
  printf("Time To Complete: %d hours, %d minutes and %d seconds\n", h,m,s);
}

int main()
{
  int timeStart = time(NULL);
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
  printf("%d prime number's found in range.\n", primeFound);
  int timeEnd = time(NULL);
  int timeRun = timeEnd - timeStart;
  hms(timeRun);
  return 0;
}