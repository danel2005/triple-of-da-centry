#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BEST_OF 3

int start(void);
char finish(void);
char game(int difficulty);

/*
char game(int difficultyLevel);
char pcRand(int difficulty, int userChoice);
*/

int main()
{
	char play = ' ';
	int difficultyLevel = 0;
	char win = ' ';
	while(play != 'n')
	{
		difficultyLevel = start(); //Start
		
		/*
		win = game(difficultyLevel);
		*/
		
		win = game(difficultyLevel);
		
		if(win == 'w')
		{
			printf("  _______   _______    ____    __    ____ .______   \n /  _____| /  _____|   \\   \\  /  \\  /   / |   _  \\  \n|  |  __  |  |  __      \\   \\/    \\/   /  |  |_)  | \n|  | |_ | |  | |_ |      \\            /   |   ___/  \n|  |__| | |  |__| |       \\    /\\    /    |  |      \n \\______|  \\______|        \\__/  \\__/     | _|      ");
			printf("\n\nYou win the game!");
		}
		else
		{
			printf("\nYou lose the game...");
		}
		
		
		play = finish(); //Finish
	}
	printf("\nThanks for playing!"); //Greetings
	getchar();
	return 0;
}

int start(void)
{
	int difficultyLevel = 0;
	char agree = ' ';
	printf("Welcome to Rock Paper Scissors!\n");
	printf("The game is best of %d\n", BEST_OF);
	do{
		printf("0 - Easy\n1 - Hard\n2 - Impossible\n");
		printf("Choose your difficulty level: ");
		scanf("%d", &difficultyLevel);
		getchar();
		printf("\n");
		
		if(difficultyLevel == 0)
		{
			printf("You choosed easy difficulty level\n");
		}
		else if(difficultyLevel == 1)
		{
			printf("You choosed hard difficulty level\n");
		}
		else if(difficultyLevel == 2)
		{
			printf("You choosed impossible difficulty level\n");
		}
		else
		{
			printf("Wrong difficulty level!\n");
			printf("You get impossible difficulty level!");
			return 2;
		}
	}while(agree == 'y');
	
	return difficultyLevel;
}

char finish(void)
{
	char play = ' ';
	do //play again
	{
		printf("\nDo you want to play again? (y/n): ");
		scanf("%c", &play);
		getchar();
	}while((play != 'y') && (play != 'n'));
	if(play == 'y')
	{
		printf("\n\n");
	}
	return play;
}

char game(difficulty)
{
	srand(time(NULL));
	char win = ' ';
	int pcWins = 0;
	int userWins = 0;
	char userChoice = ' ';
	char pcChoice = ' ';
	int roundWinner = 3;
	int random = 0;
	while((pcWins <= BEST_OF / 2) && (userWins <= BEST_OF / 2))
	{
		do{
			printf("Enter your choice (r - Rock / p - Paper / s - Scissors): ");
			scanf("%c", &userChoice);
			getchar();
		}while((userChoice != 'r') && (userChoice != 'p') && (userChoice != 's'));
		if(difficulty == 2)
		{
			if(userChoice == 'r')
			{
				pcChoice = 'p';
			}
			
			if(userChoice == 'p')
			{
				pcChoice = 's';
			}
			
			if(userChoice == 's')
			{
				pcChoice = 'r';
			}
		}
		
		if(difficulty == 1)
		{
			random = rand() % 3;
			if(random == 0)
			{
				pcChoice = 'r';
			}
			
			if(random == 1)
			{
				pcChoice = 'p';
			}
			
			if(random == 2)
			{
				pcChoice = 's';
			}
		}
		
		if(difficulty == 0)
		{
			
		}
		
		if((userChoice == 'r') && (pcChoice == 'r'))
		{
			roundWinner = 2;
		}
		else if((userChoice == 'p') && (pcChoice == 'p'))
		{
			roundWinner = 2;
		}
		else if((userChoice == 's') && (pcChoice == 's'))
		{
			roundWinner = 2;
		}
		
		else if((userChoice == 'r') && (pcChoice == 'p'))
		{
			roundWinner = 0;
			pcWins++;
		}
		else if((userChoice == 'p') && (pcChoice == 's'))
		{
			roundWinner = 0;
			pcWins++;
		}
		else if((userChoice == 's') && (pcChoice == 'r'))
		{
			roundWinner = 0;
			pcWins++;
		}
		
		else if((userChoice == 'p') && (pcChoice == 'r'))
		{
			roundWinner = 1;
			userWins++;
		}
		else if((userChoice == 's') && (pcChoice == 'p'))
		{
			roundWinner = 1;
			userWins++;
		}
		else if((userChoice == 'r') && (pcChoice == 's'))
		{
			roundWinner = 1;
			userWins++;
		}
		
		
		if(roundWinner == 2)
		{
			printf("There is a tie!\nNo points at all\n\nScore:\nPC: %d\nUser: %d\n", pcWins, userWins);
		}
		else if(roundWinner == 0)
		{
			printf("One point to user!\nScore:\nPC: %d\nUser: %d\n", pcWins, userWins);
		}
		else
		{
			printf("One point to PC!\nScore:\nPC: %d\nUser: %d\n", pcWins, userWins);
		}
	}
	if(pcWins > userWins)
	{
		win = 'l';
	}
	else
	{
		win = 'w';
	}
	
	return win;
}

/*
char game(int difficultyLevel)
{
	srand(time(NULL));
	int random = 0;
	int userWins = 0;
	int pcWins = 0;
	int targetScore = 2;
	char userChoice = ' ';
	char pcChoice = ' ';
	
	while((userWins < targetScore) || (pcWins < targetScore))
	{
		printf("Enter your choice (r - Rock / p - Paper / s - Scissors): ");
		scanf("%c", &userChoice);
		pcChoice = pcRand(difficultyLevel, userChoice);
		if(pcChoice == userChoice)
		{
			printf("There is a tie\nNo points");
		}
		else if((pcChoice == 'r') && (userChoice == 'p'))
		{
			userChoice++;
			printf("Win for the user!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
		else if((pcChoice == 'p') && (userChoice == 's'))
		{
			userChoice++;
			printf("Win for the user!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
		else if((pcChoice == 's') && (userChoice == 'r'))
		{
			userChoice++;
			printf("Win for the user!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
		
		else if((userChoice == 'r') && (pcChoice == 'p'))
		{
			pcChoice++;
			printf("Win for the PC!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
		else if((userChoice == 'p') && (pcChoice == 's'))
		{
			pcChoice++;
			printf("Win for the PC!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
		else if((userChoice == 's') && (pcChoice == 'r'))
		{
			pcChoice++;
			printf("Win for the PC!\nUser choice: %c\nPC choice: %c", userChoice, pcChoice);
		}
	}
	
	if(userWins == targetScore)
	{
		return 'w';
	}
	else
	{
		return 'l';
	}
}

char pcRand(int difficulty, int userChoice)
{
	int random = 0;
	char pcChoice = ' ';
	switch (difficulty)
	{
		case 0:
		{
		random = rand() % 3;
		switch (userChoice)
		{
			case 0:
			{
				random = rand() % 2;
				switch (userChoice)
				{
					case 0:
					{
						pcChoice = 's';
						break;
					}
					
					case 1:
					{
						pcChoice = 'p';
						break;
					}
				}
				break;
			}
			
			case 1:
			{
				random = rand() % 2;
				switch (userChoice)
				{
					case 0:
					{
						pcChoice = 'r';
						break;
					}
					
					case 1:
					{
						pcChoice = 'p';
						break;
					}
				}
				break;
			}
				
			case 2:
			{
				random = rand() % 2;
				switch (userChoice)
				{
					case 0:
					{
						pcChoice = 's';
						break;
					}
					
					case 1:
					{
						pcChoice = 'r';
						break;
					}
				}
				break;
			}
		}
		break;
	}
		
		case (1):
		{
			random = rand() % 3;
			switch (userChoice)
			{
				case ('0'):
				{
					pcChoice = 'r';
					break;
				}
				
				case ('1'):
				{
					pcChoice = 'p';
					break;
				}
				
				case ('2'):
				{
					pcChoice = 's';
					break;
				}
			}
			break;
		}
		
		case (2):
		{
			switch (userChoice)
			{
				case ('r'):
				{
					pcChoice = 'p';
					break;
				}
				
				case ('p'):
				{
					pcChoice = 's';
					break;
				}
				
				case ('s'):
				{
					pcChoice = 'r';
					break;
				}
			}
			break;
		}
	}
	return pcChoice;
}
*/
