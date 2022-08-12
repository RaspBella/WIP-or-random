#include <stdlib.h>
#include <stdio.h>

typedef struct Operating_System OS;

struct Operating_System{
    char* DE;
    char* browser;
    char* IDE;
};

struct Computer{
    OS* OS;
};

struct Programmer{
    char* name;
    int age;
    char** pronouns;
    char** favourite_languages;
    //desktop
    //laptop
};