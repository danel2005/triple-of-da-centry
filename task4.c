#include <stdio.h>
#include <string.h>

#define WORD_LEN 51
#define SUM_WORDS 10
#define SUM_LETTERS 26

int main(void)
{
	char words[SUM_WORDS][WORD_LEN] = {0};
	int usedWord[SUM_LETTERS] = {0};
	int wordLen[SUM_WORDS] = {0};
	int row = 0;
	int i = 0;
	int finish = 1;
	int col = 0;
	
	printf("Enter up to 10 words, try to make a pangram: \n");
	
	for(row = 0; ((row < SUM_WORDS) || (finish != 1)); row++)
	{
		fgets(words[row], WORD_LEN, stdin);
		words[row][strcspn(words[row], "\n")] = 0;
		wordLen[row] = strlen(words[row]);
	
		for(i = 0; i < wordLen[row]; i++)
		{
			usedWord[words[row][i] - 'a'] = 1;
		}
		for(int i = 0; i < SUM_LETTERS; i++)
		{
			if(usedWord[i] == 0)
			{
				finish = 0;
			}
		}
	}

	if(finish == 0) // if pangram wroted
	{
		printf("It's a pangram?\nNo");
	}
	else// if pangram not wroted
	{
		printf("It's a pangram?\nYes!");
	}
	
	
	return 0;
}



