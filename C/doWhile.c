#include <stdio.h>
#include <stdbool.h>
#include <unistd.h> // This is used for the sleep function
#include <ctype.h> // for isdigit() function
// DO: error checking for if is a number and not a character.

int main(){

  int input;
  do
  {
    //code
    //update
    printf("please enter a number 0 - 9: ");
    scanf("%d", &input);

    if(isdigit(input))
    {
      printf("Valid\n");
    } else {
      printf("%d is Not valid\n", input);
      printf("isdigit: %d\n", isdigit(input));
      // input = NULL;
    }
    

    sleep(3);
  } while (/*comparison*/ input < 0 || input > 9);

  return 0;
}