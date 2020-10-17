#include <stdio.h>

int main(){
    printf("Hello you!\n");
    printf("What is your name? :");
    // character array storage, 31 sigifies a maximum of 30 characters.
    char name[31];

    // Arrays do not require & before variable name.
    // Note: scanf can not use spaces.
    scanf("%s", name);

    printf("Well Hello %s!\n", name);
    return 0;
}