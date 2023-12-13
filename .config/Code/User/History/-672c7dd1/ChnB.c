#include <stdio.h>
#include <stdlib.h>

#define N 4000

int main() {
    FILE* fptr;
    int* array = (int*)malloc(N * sizeof(int));
    fptr = fopen("file.txt", "r");

    fclose(fptr);
}