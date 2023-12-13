#include <stdio.h>
#include <stdlib.h>

int main() {
    int* array = malloc(0);
    int num;
    scanf("%d", &num);
    int counter = 0;
    while (num != 0) {
        array = realloc(array, sizeof(int));
        array[counter] = num;
        counter++;
        scanf("%d", &num);
    }
}