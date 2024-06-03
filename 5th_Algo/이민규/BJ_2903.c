#include <stdio.h>

int main(void)
{
	int try_num = 0;
	int temp = 2;
	scanf("%d", &try_num);
	int i = 1;
	while (i <= try_num)
	{
		temp = temp * 2 - 1;
		i++;
	}
	printf("%d", temp * temp);
	return 0;
}