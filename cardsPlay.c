#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define	SUM_CARDS 52
#define SUM_SHAPES 4
#define SHAPE_CARDS 13

void cardsInArr(int cards[SUM_CARDS][SHAPE_CARDS]);


int main()
{
	int cards[SUM_SHAPES][SHAPE_CARDS] = {0};
	int shape[SUM_SHAPES] = {♥, ♦, ♣, ♠};
	cardsInArr(cards);
	
	
	int col = 0;
	int row = 0;
	for(row = 0; row < SUM_SHAPES; ++row)
	{
		for(col = 0; col < SHAPE_CARDS; ++col)
		{
			printf("%d ", cards[row][col]);
		}
		printf("%d \n", shape[row]);
	}
}

/*
the function puts every card in the array
input: array of the cards
output: none
*/
void cardsInArr(int cards[SUM_CARDS][SHAPE_CARDS])
{
	int col = 0;
	int row = 0;
	
	for(row = 0; row < SUM_SHAPES; ++row)
	{
		for(col = 0; col < SHAPE_CARDS; ++col)
		{
			cards[row][col] = col + 1;
		}
	}
}


