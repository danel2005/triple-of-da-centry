#include <iostream>

int main()
{
	char str[1][5] = {"s"};
	for(int i = 0; i < 5; i++)
	{
		for(int j = 0; j < 1; j++)
		{
			std::cout << str[i][j] << " ";
		}
		std::cout << std::endl;
	}
	
	return 0;
}