#include <stdio.h>
#include <stdbool.h>

int main(){
  bool pizzaIsHealthy;
  int temp;
  printf("Do you belive in the power of Pizza? 1 is yes 0 is no: ");
  scanf("%d", &temp);
  pizzaIsHealthy = temp;
  if(pizzaIsHealthy){
    printf("Welcome to the Pizza party!\n");
  }

  return 0;
}