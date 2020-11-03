#include <stdio.h>

int main(){

  printf("How many slices of pizza did yout eat (be honest): ");
  int slices;
  scanf("%d", &slices);
  int caloriesPerSlice = 250;

  switch(slices){
    case 1:
      printf("You are so skinny, have another!\n");
      break;
    case 2:
      printf("Over eathing is not recommeded.\n");
      break;
    case 3:
      printf("You ate your fill, now would be a good time to stop.\n");
      break;
    case 4:
      printf("I think wierd al as a song about you!\n");
      break;
    default:
      printf("I just cant even!\n");
      break;
  }

  printf("You had %d calories.\n", caloriesPerSlice * slices);

  return 0;
}