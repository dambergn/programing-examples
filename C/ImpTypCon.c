#include <stdio.h>
// implicit Type Conversion
// https://en.cppreference.com/w/cpp/language/implicit_conversion

int main()
{
  // Implicit type conversion - promotion
  float x = 50.0f;

  print("%f", x); // printf takes a double
  // x is PROMOTED to a double

  return 0;
}