import sys

def mul_show_digits(n1, n2):
    return [n1 * n2] + [n1 * int(digit) for digit in str(n2)]

if __name__ == '__main__':
    n1 = int(sys.stdin.readline().strip())
    n2 = int(sys.stdin.readline().strip())
    
    results = mul_show_digits(n1, n2)

    for result in results[::-1]:
        print(result)





