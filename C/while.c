#include <stdio.h>
#include <stdbool.h>

int main()
{
  // This type of while loop is just a for loop
  int i = 0;
  while (i < 10)
  {
    printf("%d", i);
    i++;
  }
  printf("\n");

  /*
  int condition = true;
  while(true)
  {
    do something
    if(condition met)
    {
      condition = false;
    }
  }
  */

  return 0;
}