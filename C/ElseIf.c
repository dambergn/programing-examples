#include <stdio.h>
// Doctors Office
// 1. add a patient
// 2. view a patient
// 3. search patients
// 4. exit

int main(){
  // menu options
  printf("Choose a menu option 1-4\n");
  printf("1. Add a patient\n");
  printf("2. view a patient\n");
  printf("3. Search for patient\n");
  printf("4. exit\n");

  int input;
  scanf("%d", &input);

  if(input == 1){
    printf("Adding a patient.\n");
  } else if (input == 2){
    printf("Viewing a patient.\n");
  } else if (input == 3){
    printf("Searching for patient.\n");
  } else if (input == 4){
    printf("Exiting program, Have a nice day!\n");
  } else {
    printf("That is not a valid option!");
  }

  return 0;
}