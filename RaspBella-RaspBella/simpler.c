#include <stdlib.h>
#include <stdio.h>

struct letters{
    char letter;
};

int main(){
    struct letters letters[] = {'A', 'B', 'C'};

    printf("Letters:\n%c\n%c\n%c\n%s\n", letters[0], letters[1], letters[2], letters);

    return 0;
}