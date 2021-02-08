#include <stdio.h>
#include <string.h>

#define	SUM_CARDS 52
#define SUN_SHAPES 4
#define SHAPE_CARDS 13

int main()
{
	int cards[SUN_SHAPES][SHAPE_CARDS] = {0}
	int i = 0;
	int j = 0;
	
	for(j = 0; J <= SUN_SHAPES; J++)
	{
		for(i = 0; i <= SHAPE_CARDS; ++i)
		{
			cards[j][i] = i;
		}
	}
}

