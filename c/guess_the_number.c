#include <time.h>
#include <stdlib.h>

int main(void)
{
	srand(time(NULL));
	int guess;
	int random = rand() % 10;
	random+=1;

	printf("Guess the random number which is between 1 and 10\n");
	scanf("%d", &guess);

	if (random==guess)
	{
		printf("Lucky\n");
	}
	else
	{
		printf("Unlucky\n");
	}
}
