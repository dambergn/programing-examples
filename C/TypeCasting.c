#include <stdio.h>

int main(){
  int slices = 17;
  int people = 2;
  double halfThePizza = (double) (slices / people); // (double) -> unary
  printf("%f\n", halfThePizza);

  double c = 25/2 * 3;
  double d = 25/2 * 3.0;
  double e = (double) (25/2) * 3;

  printf("C: %f\n", c);
  printf("D: %f\n", d);
  printf("E: %f\n", e);
  return 0;
}