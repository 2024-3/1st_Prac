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
    char mapping_string[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    while(num >= pow(base, i)) // >=을 해야 base의 거듭제곱으로 나누어 떨어지는 경우와 그렇지 않은경우의 i가 동일
        i++;

    while (i > 0)
    {
        temp = num / pow(base, i - 1);
        num -= temp * pow(base, i - 1);
        //printf("num : %d, temp : %d\n", num, temp);
        printf("%c", mapping_string[temp]);
        i--;
    }

    return 0;
}