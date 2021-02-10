#include <stdio.h>

#define WORD_LEN 51
#define SUM_WORDS 10
#define SUM_LETTERS 26

int main(void)
{
	char words[SUM_WORDS][WORD_LEN] = {0};
	int usedWord[26] = {0};
	int wordLen[SUM_WORDS] = {0};
	int row = 0;
	int i = 0;
	int finish = 0;
	int col = 0;
	
	printf("Enter up to 10 words, try to make a pangram: \n");
	
	for(row = 0; ((row < SUM_WORDS) || (finish != 1)); row++)
	{
		fgets(words[row], WORD_LEN, stdin);
		words[row][strcspn(words[row], "\n")] = 0;
		wordLen[row] = strlen(words[row]);
	
		finish = 1;
	
		for(i = 0; i < wordLen[row]; i++)
		{
			usedWord[words[row][i] - 'a' + 1] = 1;
		}
		/*
		for(i = 0; i < SUM_LETTERS; i++)
		{
			if(usedWord[i] == 0);
			{
				finish = 0;
			}
		}
		*/
	}
	
	finish = 1;
	if(finish == 1) // if pangram wroted
	{
		printf("It's a pangram?\nYes!");
	}
	
	if(finish == 0) // if pangram wasnt wroted
	{
		printf("It's a pangram?\nNo");
	}
	
	
	return 0;
}



