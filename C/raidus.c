#include <stdio.h>

int main(){
    //radius is the variable storage name.
    int radius;
    
    //printf to print to screen.
    printf("Please enter a number:");
    
    // scanf to get data from user.
    // &raidus reqired if modifying the variable.
    // "%i" Conversion character intiger
    scanf("%i", &radius);

    // double is used for non hole numbers. (floating point numbers)
    double area = 3.14159 * (radius * radius);

    // %f is used for printing non hole numbers. (floating point numbers)
    printf("The radius is %f\n", area);

    return 0;
}