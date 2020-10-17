#include <stdio.h>
// Takes in a number and returns how many dozen.
int main(){
    printf("The number of eggs for the day:");

    int eggs;
    scanf("%i", &eggs);

    // (double) eggs converst eggs from an intiger to a float
    double dozen = (double) eggs / 12;

    printf("You have %f dozen eggs.\n", dozen);

    return 0;
}