#include <stdio.h>
// Arrays are statically allocated.
// Can not mix data types.

int main()
{
  // Method 1
  int myGrades[3];
  myGrades[0] = 10;
  myGrades[1] = 11;
  myGrades[2] = 14;
  //etc

 int myGrades2Length = 9;// array length must be statically declared.
  int myGrades2[] = {10,11,14,15,16,17,54,34,23};

  // index - 0 based number
  // element - piece of data
  // size - memory alocated for array

  // Accessing data from array
  
  printf("Single position.\n");
  printf("Array pos 4: %d\n", myGrades2[4]);
  // printf("Entire Array: %d\n", myGrades2); // This does not work

  printf("\n");
  printf("Printing contents of entire array.\n");
  for(int i = 0; i < myGrades2Length; i++){
    printf("Array pos %d: %d\n", i, myGrades2[i]);
  }


  return 0;
}