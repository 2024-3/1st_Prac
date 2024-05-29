#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    char input[10] = { 0 };
    int base = 0;
    int num = 0;
    int temp = 0;
    scanf("%d %d", &num, &base);
    int i = 0;
    while(1)
    {
        if (num >= pow(base, i)) // >=을 해야 base의 거듭제곱으로 나누어 떨어지는 경우와 그렇지 않은경우의 i가 동일
        {
            i++;
            continue;
        }
        else
            break;
    }
    
    int j = 0;
    while (i - 1>= 0)
    {
        temp = num / pow(base, i - 1);
        num -= temp * pow(base, i - 1);
        //printf("num : %d, temp : %d\n", num, temp);
        if (temp >= 10)
            input[j] = temp - 10 + 'A';
        else
            input[j] = temp + '0';
        i--;
        j++;
    }
    input[j] = '\0';
    puts(input);

    return 0;
}