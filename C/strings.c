#include <stdio.h>
#include <string.h>

int main(){
    printf("Hello you!\n");
    printf("What is your name? :");
    // character array storage, 31 sigifies a maximum of 30 characters.
    char name[31];

    // Arrays do not require & before variable name.
    // Note: scanf can not use spaces.
    scanf("%s", name);

    printf("Well Hello %s!\n", name);

    // scanf will not take in spaces!
    printf("What is your favorite food?: ");
    char favFood[50];
    scanf("%49s", favFood);
    printf("%s\n", favFood);

    int charCount = 0;
    while(favFood[charCount] != '\0'){
        charCount++;
    }

    printf("The character count by while loop is %d\n", charCount);

    //or

    int charCount2 = strlen(favFood); // requires sting.h to be included

    printf("By stringLength: %d\n", charCount2);
    return 0;
}