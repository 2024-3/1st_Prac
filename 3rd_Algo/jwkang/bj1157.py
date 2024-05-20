import sys

def count_alpa(word):
    alpas = list(set(word))
    friq = [word.count(alpa) for alpa in alpas]

    if friq.count(max(friq)) > 1:
        print('?')
    else:
        print(alpas[friq.index(max(friq))])


if __name__ == '__main__':
    word = str(sys.stdin.readline().strip().upper())
    count_alpa(word)

