#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

// The user has to guess a number from 0-x
// Output weather or not the person is correct.

int main()
{
  // Generate a random number
  // pseudo random number generator
  // seed - from the clock
  int maxValue = 5;
  srand(time(NULL)); //
  int randomNumber = rand() % maxValue + 1;

  printf("%d\n", randomNumber);

  // modulus operator %
  // remainder of some division

  printf("Guess a number 0 - %d: ", maxValue);
  int input;
  scanf("%d", &input);

  printf("You guessed %d\n", input);
  printf("The correct answer was %d\n", randomNumber);

  if (input == randomNumber)
  {
    printf("You have guessed wisely!\n");
  }
  else
  {
    printf("You have guessed poorly!\n");
  }

  printf("Thank you for playing\n");
  return 0;
}