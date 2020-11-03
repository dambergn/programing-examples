#include <stdio.h>

int main(){
    //radius is the variable storage name.
    int radius;
    
    //printf to print to screen.
    printf("Please enter the radius of a circle to get the area:");
    
    // scanf to get data from user.
    // &raidus reqired if modifying the variable.
    // "%i" Conversion character intiger.
    scanf("%i", &radius);

    // double is used for non hole numbers. (floating point numbers)
    double area = 3.14159 * (radius * radius);

    // %f Conversion character for printing non hole numbers. (floating point numbers)
    // %i = radius | %f = area
    printf("The given radius of %i is an area of %f\n", radius, area);

    return 0;
}