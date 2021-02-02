#include <stdio.h>
#include <string.h>
#define STRING_LENGTH 100

int deleteEnter(char str[]);

int main(void)
{
	int i = 0;
	char str[STRING_LENGTH] = {0};
	printf("Enter string (max length 100 chars): ");
	fgets(str, 100, stdin);
	str[strcspn(str, "\n")] = '\0';
	puts(str);
}

