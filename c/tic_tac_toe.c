#include <stdio.h>
#include <stdlib.h>

struct empty_board
{
	char c1,c2,c3;
}board[3];

struct player
{
	char name[20];
	char playing;
}players[2];

int print_board(struct board;)
{
	printf("\tTic Tac Toe board:\n");
	for(int i=0;i<3;i++)
	{
		printf("\t%c\t%c\t%c\n",board[i].c1,board[i].c2,board[i].c3);
	}
}

int main(void)
{
	// init board
	board[0].c1='1';	//	1
	board[0].c2='2';	//	2
	board[0].c3='3';	//	3
	board[1].c1='4';	//	4
	board[1].c2='5';	//	5
	board[1].c3='6';	//	6
	board[2].c1='7';	//	7
	board[2].c2='8';	//	8
	board[2].c3='9';	//	9

	// getting names
	printf("Enter player one's name\n");
	scanf("%[^\n]%*c",&players[0].name);

	printf("Enter player two's name\n");
	scanf("%[^\n]%*c",&players[1].name);

	// setting x and o
	srand(time(NULL));
	int random_player = rand() % 2;

	printf("%s, Would you like to play as x or o\n",players[random_player].name);
	scanf(" %c",&players[random_player].playing);

	while(players[random_player].playing!='x' && players[random_player].playing!='o')
	{
		printf("%s, Please enter x or o\n",players[random_player].name);
		scanf(" %c",&players[random_player].playing);
	}
	if(random_player=0)
	{
		if(players[0].playing=='x')
		{
			players[1].playing='o';
		}
		else
		{
			players[1].playing='x';
		}
	}
	else
	{
		if(players[1].playing=='x')
		{
			players[0].playing='o';
		}
		else
		{
			players[0].playing='x';
		}
	}

	// init moves
	int move, used_moves[9] = {0};

	// start
	for(int turn=1; turn<10; turn++)
	{
		// clear screen
		system("clear");

		print_board(board);

		if(turn & 1)
		{
			printf("%s",players[0].name);
		}
		else
		{
			printf("%s",players[1].name);
		}

		printf("'s turn: ");
		scanf(" %d", &move);
/*
		if(used_moves[move-1]=0)
		{
			//set_board(move);
			printf("Not invalid");
		}
		else
		{
			printf("Invalid move");
		}
		used_moves[move-1]=1;
		print_board(board);
*/

		// start here
	}
}