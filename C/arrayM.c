#include <stdio.h>

int main()
{
  int const myGradesY = 3;
  int const myGradesX = 2;
  // For some reason code will not compile using variable for size declaration.
  int myGrades[2][3] = {
    {12, 23, 45},
    {64, 78, 89}
  };

  printf("Colum2 Elemnet3: %d\n", myGrades[1][2]);

  printf("\n");
  printf("Printing all elements from Multi Array:\n");
  for (int i = 0; i < myGradesX; i++){
    for (int j = 0; j < myGradesY; j++){
      printf("%d ", myGrades[i][j]);
    }
    printf("\n"); // Makes printout like a table
  }
  printf("\n");
  return 0;
}