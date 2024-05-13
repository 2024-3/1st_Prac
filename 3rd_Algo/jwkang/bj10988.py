import sys

def ispalindrome(word):
    if word == word[::-1]:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    word = str(sys.stdin.readline().strip())
    ispalindrome(word)