#include <stdio.h>
#include <stdlib.h>

int main() {
    int* array = malloc(0);
    int num;
    scanf("%d", &num);
    while (num != 0) {
        array = realloc(array, sizeof(int));
        array[counter] = num;
        scanf("%d", &num);
    }
}