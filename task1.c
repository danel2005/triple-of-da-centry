#include <stdio.h>
#include <string.h>

#define STRING_LENGHT 5

int scanStr(char str[]);

int main()
{
	char str[STRING_LENGHT] = {0};
	int stringLength = 0;
	printf("Enter string (max lenght 100 chars): ");
	stringLenght = scanStr(str);
	printf("%d\n", stringLenght);
	puts(str);
	
	return 0;
}


/*
the function scan the string and delete the spaces
input: string
output: number
*/
int scanStr(char str[])
{
	int i = 0;
	for(i = 0; i < STRING_LENGHT; i++)
	{
		scanf("%c", &str[i]);
		
		if(str[i] == '\n')
		{
			str[i] = 0;
			return i;
		}
		
		if(str[i] == ' ')
		{
			i = i - 1;
		}
	}
	return i;
}

