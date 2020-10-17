#include <stdio.h>

int main()
{
  printf("Converting ASCII between Characters and numerical Values.\n");
  char ASCII;
  printf("please enter a character: ");
  scanf("%c", &ASCII);

  printf("Char: %c\n", ASCII);
  printf("Int:  %i\n", ASCII);

  int integer;
  printf("Please enter and integer between 0 - 127: ");
  scanf("%i", &integer);
  printf("ASCII: %c\n", integer);

  //Math with ASCII:
  char mathz = 'A' + '\t';
  printf("A(65) + \\t(11) = %c(%d)\n", mathz, mathz);
  return 0;
}