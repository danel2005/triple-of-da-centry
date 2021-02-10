#include <iostream>
#include <math.h>
#include <iomanip>

unsigned int baranoliFunc(int n, int k) 
{
	int calcN = 1;
	int calcK = 1;
	int calcD = 1;
	int result = 1;

	for (int i = 1; i <= n; i++) calcN *= i;//n! זה מחשב את ה
	for (int i = 1; i <= k; i++) calcK *= i;//k! זה מחשב את ה
	for (int i = 1; i <= n - k; i++) calcD *= i;//(n - k)!

	result = calcK * calcD;
	result = calcN / result;

	return result;
}

double realCalc(float n, float k, float pr, bool DIY, int baranoliNum)
{
	double baranoli = 0.0f;
	double result = 0.0f;
	
	DIY ? baranoli = baranoliNum : baranoli = baranoliFunc(n, k);
	result = baranoli * pow(pr, k) * pow(1 - pr, n - k);
	
	return result;
}

void calc(float n, float k, float pr, bool DIY, int baranoliNum) {
	double baranoli = 0;
	double result = 0;
	
	DIY ? baranoli = baranoliNum : baranoli = baranoliFunc(n, k);
	
	std::cout << "k: " << (int)k << std::endl;	
	std::cout << "p^k = " << pow(pr, k) << std::endl;
	std::cout << "(1 - p)^(n - k) = " << pow(1 - pr, n - k) << std::endl;
	std::cout << "The result is: " << realCalc(n, k, pr, DIY, baranoliNum) << std::endl;
}

bool menu()
{
	float rangeK = 0;
	float rangeK2 = 0;
	float n = 0;
	float p = 0;
	float sum = 0;
	bool range = false;
	char answer = ' ';
	bool bronliDIY = false;
	int baranoliNum = 0;
	
	std::cout << "Enter n: ";
	std::cin >> n;
	std::cout << "is it a range:(y for yes)";//aviel
	std::cin >> answer;

	if(answer == 'y' || answer == 'Y')
	{
		range = true;
	}
	
	if(range)
	{
		std::cout << "Enter range of k: (seperate by ENTER)";
		std::cin >> rangeK;
		std::cin >> rangeK2;	
	}
	else 
	{
		std::cout << "Enter k:";
		std::cin >> rangeK;
		rangeK2 = rangeK;
	}
	
	std::cout << "Do you have the bronli value?(y for yes) ";
	std::cin >> answer;
	
	if(answer == 'y' || answer == 'Y')
	{
		bronliDIY = true;
		std::cout << "Enter da baranoli: ";
		std::cin >> baranoliNum;
	}
	
	if(rangeK > n || rangeK2 > n)
	{
		return false;
	}

	std::cout << "Enter p: ";
	std::cin >> p;
	
	for(int i = rangeK; i <= rangeK2; i++)
	{
		calc(n, i, p, bronliDIY, baranoliNum);
		std::cout << std::endl;
		sum += realCalc(n, i, p, bronliDIY, baranoliNum);
	}

	std::cout << "The sum of all the probilities is: " << std::fixed << std::setprecision(5) << sum;
	
	return true;
}

int main()
{
	if(!menu()) std::cerr << "ERROR! K CAN NEVER BE BIGGER THAN N!";
	
	return 0;
}
//g++ -o mathLazy.exe mathLazy.cpp