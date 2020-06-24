#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
	printf("Change: ");
	float change = get_float();
	change = round(change * 100);
	
	int coins = 0;
	while (change != 0)
	{

		if (change >= 25)
		{
			change -= 25;
			coins += 1;
		}
	
		else if (change >= 10 && change <= 25)
		{
			change -= 10;
			coins += 1;
		}

		else if (change >= 5 && change <= 10)
		{
			change -= 5;
			coins += 1;
		}

		else if (change >= 1 && change <= 5)
		{
			change -= 1;
			coins += 1;
		}
		
		else if (change < 0)
		{
			printf("Change: ");
			change = get_float();
			change = change * 100;
		}
	}
	printf("%i\n", coins);
	while (change <= 0)
	{
		break;
	}
}