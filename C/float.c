#include <stdio.h>

int main(){
    printf("How many dogs do you have?:");
    double dogs;

    // %lf used for reading decimal or scientific notation input
    scanf("%lf", &dogs);

    printf("%f\n%e\n%g\n", dogs, dogs, dogs);

    /* Conversion Characters
    ________________________
    %f - Decimal Notation
    %e - Scientific Notation
    %g - Auto Notation
       - < -4
       - >  5
    */
    return 0;
}