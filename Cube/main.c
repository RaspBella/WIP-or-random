#include <stdio.h>
#include <string.h>

struct Faces
{
    char U[9];
    char L[9];
    char F[9];
    char R[9];
    char B[9];
    char D[10];
};

void print_faces (struct Faces faces) {
    printf(
        "\t%c %c %c\n\t%c %c %c\n\t%c %c %c\n\n%c %c %c\t%c %c %c\t%c %c %c\t%c %c %c\n%c %c %c\t%c %c %c\t%c %c %c\t%c %c %c\n%c %c %c\t%c %c %c\t%c %c %c\t%c %c %c\n\n\t%c %c %c\n\t%c %c %c\n\t%c %c %c\n",
        faces.U[0], faces.U[1], faces.U[2],
        faces.U[3], faces.U[4], faces.U[5],
        faces.U[6], faces.U[7], faces.U[8],
        faces.L[0], faces.L[1], faces.L[2], faces.F[0], faces.F[1], faces.F[2], faces.R[0], faces.R[1], faces.R[2], faces.B[0], faces.B[1], faces.B[2],
        faces.L[3], faces.L[4], faces.L[5], faces.F[3], faces.F[4], faces.F[5], faces.R[3], faces.R[4], faces.R[5], faces.B[3], faces.B[4], faces.B[5],
        faces.L[6], faces.L[7], faces.L[8], faces.F[6], faces.F[7], faces.F[8], faces.R[6], faces.R[7], faces.R[8], faces.B[6], faces.B[7], faces.B[8],
        faces.D[0], faces.D[1], faces.D[2],
        faces.D[3], faces.D[4], faces.D[5],
        faces.D[6], faces.D[7], faces.D[8]);
}

void U (struct Faces faces) {
    struct Faces new_faces = faces;

    /*new_faces.U = faces.U[6], faces.U[3], faces.U[0], faces.U[7], faces.U[4], faces.U[1], faces.U[8], faces.U[5], faces.U[2];*/
    char string[9];
    string[0], string[1], string[2], string[3], string[4], string[5], string[6], string[7], string[8] = faces.U[6], faces.U[3], faces.U[0], faces.U[7], faces.U[4], faces.U[1], faces.U[8], faces.U[5], faces.U[2];
    strcpy(new_faces.U, string);

    print_faces(new_faces);
}

int main () {
    struct Faces faces;

    strcpy(faces.U, "UUUUUUUUU");
    strcpy(faces.L, "LLLLLLLLL");
    strcpy(faces.F, "FFFFFFFFF");
    strcpy(faces.R, "RRRRRRRRR");
    strcpy(faces.B, "BBBBBBBBB");
    strcpy(faces.D, "DDDDDDDDD");

    print_faces(faces);

    U(faces);

    return 0;
}