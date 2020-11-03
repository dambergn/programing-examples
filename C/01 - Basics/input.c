#include <stdio.h>

int main(){
    // number is the variable storage name.
    int number;
    
    //printf to print to screen.
    printf("Please enter a number:");
    
    // scanf to get data from user.
    // &number reqired if modifying the variable.
    // "%i" Conversion character intiger
    scanf("%i", &number);

    printf("The number you entered is %i\n", number);
    return 0;
}