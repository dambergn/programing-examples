#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[]) {
    srand(time(NULL));
    printf("How many characters do you want in your password?\n");
    int desiredNumber;
    char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    scanf("%d", &desiredNumber);
    char password[desiredNumber];
    for(int i = 0; i < desiredNumber; i++){
        int random = rand() % strlen(alphabet);
        // printf("%d", random);
        password[i] = alphabet[random]; // password ith index will be random
        printf("%c", password[i]);
    }
    printf("\n");
    printf("Complete: %s\n", password);
    return 0;
}