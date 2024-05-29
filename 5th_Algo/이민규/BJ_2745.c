#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    char input[10] = { 0 };
    int base = 0;
    int result = 0;
    int temp = 0;
    scanf("%s %d", input, &base);
    int len = strlen(input);

    for (int i = 0; i < len; i++)
    {
        if (input[i] >= 'A' && input[i] <= 'Z')
            temp = input[i] - 'A' + 10;
        else
            temp = input[i] - '0';

        result += temp * pow(base, len - i - 1);
    }
    printf("%d", result);

    return 0;
}