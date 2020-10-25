#include <stdio.h>

int main(){

  printf("How many times do you want to run the loop? :");
  int max;
  scanf("%d", &max);

  for (int i = 0; i < max; i++){
    printf("%d\n", i);
  }

  return 0;
}